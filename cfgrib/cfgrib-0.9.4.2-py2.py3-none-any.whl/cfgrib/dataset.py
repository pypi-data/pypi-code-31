#
# Copyright 2017-2018 European Centre for Medium-Range Weather Forecasts (ECMWF).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors:
#   Alessandro Amici - B-Open - https://bopen.eu
#

from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import list, object, set, str

import collections
import logging
import pkg_resources
import typing as T
import warnings

import attr
import numpy as np

from . import cfmessage
from . import eccodes
from . import messages

LOG = logging.getLogger(__name__)

#
# Edition-independent keys in ecCodes namespaces. Documented in:
#   https://software.ecmwf.int/wiki/display/ECC/GRIB%3A+Namespaces
#
GLOBAL_ATTRIBUTES_KEYS = ['edition', 'centre', 'centreDescription', 'subCentre']

DATA_ATTRIBUTES_KEYS = [
    'paramId', 'shortName', 'units', 'name', 'cfName', 'cfVarName',
    'dataType', 'missingValue', 'numberOfPoints',
    'totalNumber',
    'typeOfLevel', 'NV',
    'stepUnits', 'stepType',
    'gridType', 'gridDefinitionDescription',
]

GRID_TYPE_MAP = {
    'regular_ll': [
        'Ni', 'iDirectionIncrementInDegrees', 'iScansNegatively',
        'longitudeOfFirstGridPointInDegrees', 'longitudeOfLastGridPointInDegrees',
        'Nj', 'jDirectionIncrementInDegrees', 'jPointsAreConsecutive', 'jScansPositively',
        'latitudeOfFirstGridPointInDegrees', 'latitudeOfLastGridPointInDegrees',
    ],
    'reduced_ll': [
        'Nj', 'jDirectionIncrementInDegrees', 'jPointsAreConsecutive', 'jScansPositively',
        'latitudeOfFirstGridPointInDegrees', 'latitudeOfLastGridPointInDegrees',
    ],
    'regular_gg': [
        'Ni', 'iDirectionIncrementInDegrees', 'iScansNegatively',
        'longitudeOfFirstGridPointInDegrees', 'longitudeOfLastGridPointInDegrees',
        'N', 'Nj',
    ],
    'lambert': [
        'LaDInDegrees', 'LoVInDegrees', 'iScansNegatively',
        'jPointsAreConsecutive', 'jScansPositively',
        'latitudeOfFirstGridPointInDegrees', 'latitudeOfSouthernPoleInDegrees',
        'longitudeOfFirstGridPointInDegrees', 'longitudeOfSouthernPoleInDegrees',
        'DyInMetres', 'DxInMetres', 'Latin2InDegrees', 'Latin1InDegrees', 'Ny', 'Nx',
    ],
    'reduced_gg': ['N', 'pl'],
    'sh': ['M', 'K', 'J'],
}
GRID_TYPE_KEYS = sorted(set(k for _, ks in GRID_TYPE_MAP.items() for k in ks))

ENSEMBLE_KEYS = ['number']
VERTICAL_KEYS = ['level']
DATA_TIME_KEYS = ['dataDate', 'dataTime', 'endStep']
REF_TIME_KEYS = ['time', 'step']

ALL_HEADER_DIMS = ENSEMBLE_KEYS + VERTICAL_KEYS + DATA_TIME_KEYS + REF_TIME_KEYS

ALL_KEYS = GLOBAL_ATTRIBUTES_KEYS + DATA_ATTRIBUTES_KEYS + GRID_TYPE_KEYS + ALL_HEADER_DIMS

COORD_ATTRS = {
    'time': {
        'units': 'seconds since 1970-01-01T00:00:00+00:00', 'calendar': 'proleptic_gregorian',
        'standard_name': 'forecast_reference_time', 'long_name': 'initial time of forecast',
    },
    'step': {
        'units': 'hours',
        'standard_name': 'forecast_period', 'long_name': 'time since forecast_reference_time',
    },
    'valid_time': {
        'units': 'seconds since 1970-01-01T00:00:00+00:00', 'calendar': 'proleptic_gregorian',
        'standard_name': 'time', 'long_name': 'time',
    },
    'latitude': {
        'units': 'degrees_north',
        'standard_name': 'latitude', 'long_name': 'latitude',
    },
    'longitude': {
        'units': 'degrees_east',
        'standard_name': 'longitude', 'long_name': 'longitude',
    },
    'isobaricInhPa': {
        'units': 'hPa', 'positive': 'down', 'stored_direction': 'decreasing',
        'standard_name': 'air_pressure', 'long_name': 'pressure',
    },
    'hybrid': {
        'units': '1', 'positive': 'down', 'long_name': 'hybrid level',
        'standard_name': 'atmosphere_hybrid_sigma_pressure_coordinate',
    },
    'number': {
        'units': '1',
        'standard_name': 'realization', 'long_name': 'ensemble member numerical id',
    }
}


class DatasetBuildError(ValueError):
    def __str__(self):
        return str(self.args[0])


def enforce_unique_attributes(index, attributes_keys, filter_by_keys={}):
    # type: (messages.FileIndex, T.Sequence[str], dict) -> T.Dict[str, T.Any]
    attributes = collections.OrderedDict()  # type: T.Dict[str, T.Any]
    for key in attributes_keys:
        values = index[key]
        if len(values) > 1:
            error_message = "multiple values for unique key, try re-open the file with one of:"
            fbks = []
            for value in values:
                fbk = {key: value}
                fbk.update(filter_by_keys)
                fbks.append(fbk)
                error_message += "\n    filter_by_keys=%r" % fbk
            raise DatasetBuildError(error_message, fbks)
        if values and values[0] not in ('undef', 'unknown'):
            attributes['GRIB_' + key] = values[0]
    return attributes


@attr.attrs(cmp=False)
class Variable(object):
    dimensions = attr.attrib(type=T.Tuple[str, ...])
    data = attr.attrib(type=np.ndarray)
    attributes = attr.attrib(default={}, type=T.Dict[str, T.Any], repr=False)

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        equal = (self.dimensions, self.attributes) == (other.dimensions, other.attributes)
        return equal and np.array_equal(self.data, other.data)


def expand_item(item, shape):
    expanded_item = []
    for i, size in zip(item, shape):
        if isinstance(i, list):
            expanded_item.append(i)
        elif isinstance(i, np.ndarray):
            expanded_item.append(i.tolist())
        elif isinstance(i, slice):
            expanded_item.append(list(range(i.start or 0, i.stop or size, i.step or 1)))
        elif isinstance(i, int):
            expanded_item.append([i])
        else:
            raise TypeError("Unsupported index type %r" % type(i))
    return tuple(expanded_item)


@attr.attrs()
class OnDiskArray(object):
    stream = attr.attrib()
    shape = attr.attrib(type=T.Tuple[int, ...])
    offsets = attr.attrib(repr=False, type=T.Dict[T.Tuple[T.Any, ...], T.List[int]])
    missing_value = attr.attrib()
    geo_ndim = attr.attrib(default=1, repr=False)
    dtype = np.dtype('float32')

    def build_array(self):
        """Helper method used to test __getitem__"""
        # type: () -> np.ndarray
        array = np.full(self.shape, fill_value=np.nan, dtype='float32')
        with open(self.stream.path) as file:
            for header_indexes, offset in self.offsets.items():
                # NOTE: fill a single field as found in the message
                message = self.stream.message_from_file(file, offset=offset[0])
                values = message.message_get('values', eccodes.CODES_TYPE_DOUBLE)
                array.__getitem__(header_indexes).flat[:] = values
        array[array == self.missing_value] = np.nan
        return array

    def __getitem__(self, item):
        assert isinstance(item, tuple), "Item type must be tuple not %r" % type(item)
        assert len(item) == len(self.shape), "Item len must be %r not %r" % (self.shape, len(item))

        header_item = expand_item(item[:-self.geo_ndim], self.shape)
        array_field_shape = tuple(len(l) for l in header_item) + self.shape[-self.geo_ndim:]
        array_field = np.full(array_field_shape, fill_value=np.nan, dtype='float32')
        with open(self.stream.path) as file:
            for header_indexes, offset in self.offsets.items():
                try:
                    array_field_indexes = []
                    for it, ix in zip(header_item, header_indexes):
                        array_field_indexes.append(it.index(ix))
                except ValueError:
                    continue
                # NOTE: fill a single field as found in the message
                message = self.stream.message_from_file(file, offset=offset[0])
                values = message.message_get('values', eccodes.CODES_TYPE_DOUBLE)
                array_field.__getitem__(tuple(array_field_indexes)).flat[:] = values

        array = array_field[(Ellipsis,) + item[-self.geo_ndim:]]
        array[array == self.missing_value] = np.nan
        for i, it in reversed(list(enumerate(item[:-self.geo_ndim]))):
            if isinstance(it, int):
                array = array[(slice(None, None, None),) * i + (0,)]
        return array


GRID_TYPES_DIMENSION_COORDS = ('regular_ll', 'regular_gg')
GRID_TYPES_2D_NON_DIMENSION_COORDS = ('lambert', 'albers', 'polar_stereographic')
GRID_TYPES_1D_NON_DIMENSION_COORDS = ('reduced_ll', 'reduced_gg')


def build_geography_coordinates(
        index,  # type: messages.FileIndex
        encode_cf,  # type: T.Sequence[str]
        log=LOG,  # type: logging.Logger
):
    # type: (...) -> T.Tuple[T.Tuple[str, ...], T.Tuple[int, ...], T.Dict[str, Variable]]
    first = index.first()
    geo_coord_vars = collections.OrderedDict()  # type: T.Dict[str, Variable]
    grid_type = index.getone('gridType')
    if 'geography' in encode_cf and grid_type in GRID_TYPES_DIMENSION_COORDS:
        geo_dims = ('latitude', 'longitude')  # type: T.Tuple[str, ...]
        geo_shape = (index.getone('Nj'), index.getone('Ni'))  # type: T.Tuple[int, ...]
        latitudes = np.array(first['distinctLatitudes'])
        geo_coord_vars['latitude'] = Variable(
            dimensions=('latitude',), data=latitudes, attributes=COORD_ATTRS['latitude'].copy(),
        )
        if latitudes[0] > latitudes[-1]:
            geo_coord_vars['latitude'].attributes['stored_direction'] = 'decreasing'
        geo_coord_vars['longitude'] = Variable(
            dimensions=('longitude',), data=np.array(first['distinctLongitudes']),
            attributes=COORD_ATTRS['longitude'],
        )
    elif 'geography' in encode_cf and grid_type in GRID_TYPES_2D_NON_DIMENSION_COORDS:
        geo_dims = ('y', 'x')
        geo_shape = (index.getone('Ny'), index.getone('Nx'))
        try:
            geo_coord_vars['latitude'] = Variable(
                dimensions=('y', 'x'), data=np.array(first['latitudes']).reshape(geo_shape),
                attributes=COORD_ATTRS['latitude'],
            )
            geo_coord_vars['longitude'] = Variable(
                dimensions=('y', 'x'), data=np.array(first['longitudes']).reshape(geo_shape),
                attributes=COORD_ATTRS['longitude'],
            )
        except KeyError:
            log.warning('No latitudes/longitudes provided by ecCodes for gridType=%r', grid_type)
    else:
        geo_dims = ('values',)
        geo_shape = (index.getone('numberOfPoints'),)
        # add secondary coordinates if ecCodes provides them
        try:
            latitude = first['latitudes']
            geo_coord_vars['latitude'] = Variable(
                dimensions=('values',), data=np.array(latitude),
                attributes=COORD_ATTRS['latitude'],
            )
            longitude = first['longitudes']
            geo_coord_vars['longitude'] = Variable(
                dimensions=('values',), data=np.array(longitude),
                attributes=COORD_ATTRS['longitude'],
            )
        except KeyError:
            log.warning('No latitudes/longitudes provided by ecCodes for gridType=%r', grid_type)
    return geo_dims, geo_shape, geo_coord_vars


def encode_cf_first(data_var_attrs, encode_cf=('parameter', 'time')):
    coords_map = ENSEMBLE_KEYS[:]
    if 'parameter' in encode_cf:
        if 'GRIB_cfName' in data_var_attrs:
            data_var_attrs['standard_name'] = data_var_attrs['GRIB_cfName']
        if 'GRIB_name' in data_var_attrs:
            data_var_attrs['long_name'] = data_var_attrs['GRIB_name']
        if 'GRIB_units' in data_var_attrs:
            data_var_attrs['units'] = data_var_attrs['GRIB_units']
    if 'time' in encode_cf:
        coords_map.extend(REF_TIME_KEYS)
    else:
        coords_map.extend(DATA_TIME_KEYS)
    coords_map.extend(VERTICAL_KEYS)
    return coords_map


def build_variable_components(index, encode_cf=(), filter_by_keys={}, log=LOG):
    data_var_attrs_keys = DATA_ATTRIBUTES_KEYS[:]
    data_var_attrs_keys.extend(GRID_TYPE_MAP.get(index.getone('gridType'), []))
    data_var_attrs = enforce_unique_attributes(index, data_var_attrs_keys, filter_by_keys)
    coords_map = encode_cf_first(data_var_attrs, encode_cf)

    coord_name_key_map = {}
    coord_vars = collections.OrderedDict()
    for coord_key in coords_map:
        values = index[coord_key]
        if len(values) == 1 and values[0] == 'undef':
            log.info("missing from GRIB stream: %r" % coord_key)
            continue
        coord_name = coord_key
        if 'vertical' in encode_cf and coord_key == 'level' and \
                'GRIB_typeOfLevel' in data_var_attrs:
            coord_name = data_var_attrs['GRIB_typeOfLevel']
            coord_name_key_map[coord_name] = coord_key
        attributes = COORD_ATTRS.get(coord_name, {}).copy()
        data = np.array(sorted(values, reverse=attributes.get('stored_direction') == 'decreasing'))
        dimensions = (coord_name,)
        if len(values) == 1:
            data = data[0]
            dimensions = ()
        coord_vars[coord_name] = Variable(dimensions=dimensions, data=data, attributes=attributes)

    header_dimensions = tuple(d for d, c in coord_vars.items() if c.data.size > 1)
    header_shape = tuple(coord_vars[d].data.size for d in header_dimensions)

    geo_dims, geo_shape, geo_coord_vars = build_geography_coordinates(index, encode_cf)
    dimensions = header_dimensions + geo_dims
    shape = header_shape + geo_shape
    coord_vars.update(geo_coord_vars)

    offsets = collections.OrderedDict()
    for header_values, offset in index.offsets:
        header_indexes = []  # type: T.List[int]
        for dim in header_dimensions:
            header_value = header_values[index.index_keys.index(coord_name_key_map.get(dim, dim))]
            header_indexes.append(coord_vars[dim].data.tolist().index(header_value))
        offsets[tuple(header_indexes)] = offset
    missing_value = data_var_attrs.get('missingValue', 9999)
    data = OnDiskArray(
        stream=index.filestream, shape=shape, offsets=offsets, missing_value=missing_value,
        geo_ndim=len(geo_dims),
    )

    if 'time' in coord_vars and 'time' in encode_cf:
        # add the 'valid_time' secondary coordinate
        step_data = coord_vars['step'].data if 'step' in coord_vars else np.array(0.)
        dims, time_data = cfmessage.build_valid_time(
            coord_vars['time'].data, step_data,
        )
        attrs = COORD_ATTRS['valid_time']
        coord_vars['valid_time'] = Variable(dimensions=dims, data=time_data, attributes=attrs)

    data_var_attrs['coordinates'] = ' '.join(coord_vars.keys())
    data_var = Variable(dimensions=dimensions, data=data, attributes=data_var_attrs)
    dims = collections.OrderedDict((d, s) for d, s in zip(dimensions, data_var.data.shape))
    return dims, data_var, coord_vars


def dict_merge(master, update):
    for key, value in update.items():
        if key not in master:
            master[key] = value
        elif master[key] == value:
            pass
        else:
            raise DatasetBuildError("key present and new value is different: "
                                    "key=%r value=%r new_value=%r" % (key, master[key], value))


def build_dataset_components(
        stream, indexpath='{path}.{short_hash}.idx', filter_by_keys={}, errors='ignore',
        encode_cf=('parameter', 'time', 'geography', 'vertical'), log=LOG,
):
    filter_by_keys = dict(filter_by_keys)
    index = stream.index(ALL_KEYS, indexpath=indexpath).subindex(filter_by_keys)
    param_ids = index['paramId']
    dimensions = collections.OrderedDict()
    variables = collections.OrderedDict()
    for param_id, short_name, var_name in zip(param_ids, index['shortName'], index['cfVarName']):
        var_index = index.subindex(paramId=param_id)
        dims, data_var, coord_vars = build_variable_components(
            var_index, encode_cf, filter_by_keys,
        )
        if 'parameter' in encode_cf and var_name not in ('undef', 'unknown'):
            short_name = var_name
        vars = collections.OrderedDict([(short_name, data_var)])
        vars.update(coord_vars)
        try:
            dict_merge(dimensions, dims)
            dict_merge(variables, vars)
        except ValueError:
            if errors == 'ignore':
                log.exception("skipping variable: paramId==%r shortName=%r", param_id, short_name)
            else:
                raise
    attributes = enforce_unique_attributes(index, GLOBAL_ATTRIBUTES_KEYS, filter_by_keys)
    cfgrib_ver = pkg_resources.get_distribution("cfgrib").version
    eccodes_ver = eccodes.codes_get_api_version()
    encoding = {
        'source': stream.path,
        'filter_by_keys': filter_by_keys,
        'encode_cf': encode_cf,
    }
    open_text = ', '.join('%s=%r' % it for it in encoding.items())
    attributes['history'] = 'GRIB to CDM+CF via ' \
        'cfgrib-%s/ecCodes-%s with %s' % (cfgrib_ver, eccodes_ver, open_text)
    return dimensions, variables, attributes, encoding


@attr.attrs()
class Dataset(object):
    """
    Map a GRIB file to the NetCDF Common Data Model with CF Conventions.
    """
    dimensions = attr.attrib(type=T.Dict[str, int])
    variables = attr.attrib(type=T.Dict[str, Variable])
    attributes = attr.attrib(type=T.Dict[str, T.Any])
    encoding = attr.attrib(type=T.Dict[str, T.Any])


def open_file(path, grib_errors='ignore', **kwargs):
    """Open a GRIB file as a ``cfgrib.Dataset``."""
    if 'mode' in kwargs:
        warnings.warn("the `mode` keyword argument is ignored and deprecated", FutureWarning)
        kwargs.pop('mode')
    stream = messages.FileStream(path, message_class=cfmessage.CfMessage, errors=grib_errors)
    return Dataset(*build_dataset_components(stream, **kwargs))
