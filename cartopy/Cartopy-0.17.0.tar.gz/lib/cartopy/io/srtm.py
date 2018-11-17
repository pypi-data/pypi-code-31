# (C) British Crown Copyright 2011 - 2018, Met Office
#
# This file is part of cartopy.
#
# cartopy is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cartopy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with cartopy.  If not, see <https://www.gnu.org/licenses/>.

"""
The Shuttle Radar Topography Mission (SRTM) is an international research
effort that obtained digital elevation models on a near-global scale from
56S to 60N, to generate the most complete high-resolution digital topographic
database of Earth prior to the release of the ASTER GDEM in 2009.

   - Wikipedia (August 2012)

"""

from __future__ import (absolute_import, division, print_function)

import os
import warnings

import numpy as np
import six

from cartopy import config
import cartopy.crs as ccrs
from cartopy.io import fh_getter, Downloader, RasterSource, LocatedImage


class _SRTMSource(RasterSource):
    """
    A source of SRTM data, which implements Cartopy's :ref:`RasterSource
    interface <raster-source-interface>`.

    """
    def __init__(self, resolution, downloader, max_nx, max_ny):
        """
        Parameters
        ----------
        resolution
            The resolution of SRTM to download, in integer arc-seconds.
            Data is available at resolutions of 3 and 1 arc-seconds.
        downloader: :class:`cartopy.io.Downloader` instance or None
            The downloader to use for the SRTM dataset. If None, the
            downloader will be taken using
            :class:`cartopy.io.Downloader.from_config` with ('SRTM',
            'SRTM{resolution}') as the target.
        max_nx
            The maximum number of x tiles to be combined when producing a
            wider composite for this RasterSource.
        max_ny
            The maximum number of y tiles to be combined when producing a
            taller composite for this RasterSource.

        """
        if resolution == 3:
            self._shape = (1201, 1201)
        elif resolution == 1:
            self._shape = (3601, 3601)
        else:
            raise ValueError(
                'Resolution is an unexpected value ({}).'.format(resolution))
        self._resolution = resolution

        #: The CRS of the underlying SRTM data.
        self.crs = ccrs.PlateCarree()

        #: The Cartopy Downloader which can handle SRTM data. Normally, this
        #: will be a :class:`SRTMDownloader` instance.
        self.downloader = downloader

        if self.downloader is None:
            self.downloader = Downloader.from_config(
                ('SRTM', 'SRTM' + str(resolution)))

        #: A tuple of (max_x_tiles, max_y_tiles).
        self._max_tiles = (max_nx, max_ny)

    def validate_projection(self, projection):
        return projection == self.crs

    def fetch_raster(self, projection, extent, target_resolution):
        """
        Fetch SRTM elevation for the given projection and approximate extent.

        """
        if not self.validate_projection(projection):
            raise ValueError(
                'Unsupported projection for the SRTM{} source.'.format(
                    self._resolution))

        min_x, max_x, min_y, max_y = extent
        min_x, min_y = np.floor([min_x, min_y])
        nx = int(np.ceil(max_x) - min_x)
        ny = int(np.ceil(max_y) - min_y)
        skip = False
        if nx > self._max_tiles[0]:
            warnings.warn(
                'Required SRTM{} tile count ({}) exceeds maximum ({}). '
                'Increase max_nx limit.'.format(self._resolution, nx,
                                                self._max_tiles[0]))
            skip = True
        if ny > self._max_tiles[1]:
            warnings.warn(
                'Required SRTM{} tile count ({}) exceeds maximum ({}). '
                'Increase max_ny limit.'.format(self._resolution, ny,
                                                self._max_tiles[1]))
            skip = True
        if skip:
            return []
        else:
            img, _, extent = self.combined(min_x, min_y, nx, ny)
            return [LocatedImage(np.flipud(img), extent)]

    def srtm_fname(self, lon, lat):
        """
        Return the filename for the given lon/lat SRTM tile (downloading if
        necessary), or None if no such tile exists (i.e. the tile would be
        entirely over water, or out of latitude range).

        """
        if int(lon) != lon or int(lat) != lat:
            raise ValueError('Integer longitude/latitude values required.')

        x = '%s%03d' % ('E' if lon >= 0 else 'W', abs(int(lon)))
        y = '%s%02d' % ('N' if lat >= 0 else 'S', abs(int(lat)))

        srtm_downloader = Downloader.from_config(
            ('SRTM', 'SRTM' + str(self._resolution)))
        params = {'config': config, 'resolution': self._resolution,
                  'x': x, 'y': y}

        # If the URL doesn't exist then we are over sea/north/south of the
        # limits of the SRTM data and we return None.
        if srtm_downloader.url(params) is None:
            return None
        else:
            return self.downloader.path(params)

    def combined(self, lon_min, lat_min, nx, ny):
        """
        Return an image and its extent for the group of nx by ny tiles
        starting at the given bottom left location.

        """
        bottom_left_ll = (lon_min, lat_min)
        shape = np.array(self._shape)
        img = np.zeros(shape * (ny, nx))

        for i, j in np.ndindex(nx, ny):
            x_img_slice = slice(i * shape[1], (i + 1) * shape[1])
            y_img_slice = slice(j * shape[0], (j + 1) * shape[0])

            try:
                tile_img, _, _ = self.single_tile(bottom_left_ll[0] + i,
                                                  bottom_left_ll[1] + j)
            except ValueError:
                img[y_img_slice, x_img_slice] = 0
            else:
                img[y_img_slice, x_img_slice] = tile_img

        extent = (bottom_left_ll[0], bottom_left_ll[0] + nx,
                  bottom_left_ll[1], bottom_left_ll[1] + ny)

        return img, self.crs, extent

    def single_tile(self, lon, lat):
        fname = self.srtm_fname(lon, lat)
        if fname is None:
            raise ValueError('No srtm tile found for those coordinates.')
        return read_SRTM(fname)


class SRTM3Source(_SRTMSource):
    """
    A source of SRTM3 data, which implements Cartopy's :ref:`RasterSource
    interface <raster-source-interface>`.

    """
    def __init__(self, downloader=None, max_nx=3, max_ny=3):
        """
        Parameters
        ----------
        downloader: :class:`cartopy.io.Downloader` instance or None
            The downloader to use for the SRTM3 dataset. If None, the
            downloader will be taken using
            :class:`cartopy.io.Downloader.from_config` with ('SRTM', 'SRTM3')
            as the target.
        max_nx
            The maximum number of x tiles to be combined when
            producing a wider composite for this RasterSource.
        max_ny
            The maximum number of y tiles to be combined when
            producing a taller composite for this RasterSource.

        """
        super(SRTM3Source, self).__init__(resolution=3, downloader=downloader,
                                          max_nx=max_nx, max_ny=max_ny)


class SRTM1Source(_SRTMSource):
    """
    A source of SRTM1 data, which implements Cartopy's :ref:`RasterSource
    interface <raster-source-interface>`.

    """
    def __init__(self, downloader=None, max_nx=3, max_ny=3):
        """
        Parameters
        ----------
        downloader: :class:`cartopy.io.Downloader` instance or None
            The downloader to use for the SRTM1 dataset. If None, the
            downloader will be taken using
            :class:`cartopy.io.Downloader.from_config` with ('SRTM', 'SRTM1')
            as the target.
        max_nx
            The maximum number of x tiles to be combined when
            producing a wider composite for this RasterSource.
        max_ny
            The maximum number of y tiles to be combined when
            producing a taller composite for this RasterSource.

        """
        super(SRTM1Source, self).__init__(resolution=1, downloader=downloader,
                                          max_nx=max_nx, max_ny=max_ny)


def srtm(lon, lat):
    """
    Return (elevation, crs, extent) for the given longitude latitude.
    Elevation is in meters.
    """
    warnings.warn("This method has been deprecated. "
                  "See the \"What's new\" section for v0.12.")
    return SRTM3Source().single_tile(lon, lat)


def add_shading(elevation, azimuth, altitude):
    """Add shading to SRTM elevation data, using azimuth and altitude
    of the sun.

    Parameters
    ----------
    elevation
        SRTM elevation data (in meters)
    azimuth
        Azimuth of the Sun (in degrees)
    altitude
        Altitude of the Sun (in degrees)

    Return shaded SRTM relief map.
    """
    azimuth = np.deg2rad(azimuth)
    altitude = np.deg2rad(altitude)
    x, y = np.gradient(elevation)
    slope = np.pi/2. - np.arctan(np.sqrt(x*x + y*y))
    # -x here because of pixel orders in the SRTM tile
    aspect = np.arctan2(-x, y)
    shaded = np.sin(altitude) * np.sin(slope)\
        + np.cos(altitude) * np.cos(slope)\
        * np.cos((azimuth - np.pi/2.) - aspect)
    return shaded


def fill_gaps(elevation, max_distance=10):
    """Fill gaps in SRTM elevation data for which the distance from
    missing pixel to nearest existing one is smaller than `max_distance`.

    This function requires osgeo/gdal to work.

    Parameters
    ----------
    elevation
        SRTM elevation data (in meters)
    max_distance
        Maximal distance (in pixels) between a missing point
        and the nearest valid one.

    Returns
    -------
    elevation
        SRTM elevation data with filled gaps.

    """
    warnings.warn("The fill_gaps function has been deprecated. "
                  "See the \"What's new\" section for v0.14.")
    # Lazily import osgeo - it is only an optional dependency for cartopy.
    from osgeo import gdal
    from osgeo import gdal_array

    src_ds = gdal_array.OpenArray(elevation)
    srcband = src_ds.GetRasterBand(1)
    dstband = srcband
    maskband = srcband
    smoothing_iterations = 0
    options = []
    gdal.FillNodata(dstband, maskband,
                    max_distance, smoothing_iterations, options,
                    callback=None)
    elevation = dstband.ReadAsArray()
    return elevation


def srtm_composite(lon_min, lat_min, nx, ny):
    warnings.warn("This method has been deprecated. "
                  "See the \"What's new\" section for v0.12.")
    return SRTM3Source().combined(lon_min, lat_min, nx, ny)


def read_SRTM(fh):
    """
    Read the array of (y, x) elevation data from the given named file-handle.

    Parameters
    ----------
    fh
        A named file-like as passed through to :func:`cartopy.io.fh_getter`.
        The filename is used to determine the extent of the resulting array.

    Returns
    -------
    elevation
        The elevation values from the SRTM file. Data is flipped
        vertically such that the higher the y-index, the further north the
        data. Data shape is automatically determined by the size of data read
        from file, and is either (1201, 1201) for 3 arc-second data or
        (3601, 3601) for 1 arc-second data.
    crs: :class:`cartopy.crs.CRS`
        The coordinate reference system of the extents.
    extents: 4-tuple (x0, x1, y0, y1)
        The boundaries of the returned elevation array.

    """
    fh, fname = fh_getter(fh, needs_filename=True)
    if fname.endswith('.zip'):
        from zipfile import ZipFile
        zfh = ZipFile(fh, 'rb')
        fh = zfh.open(os.path.basename(fname[:-4]), 'r')

    elev = np.fromfile(fh, dtype=np.dtype('>i2'))
    if elev.size == 12967201:
        elev.shape = (3601, 3601)
    elif elev.size == 1442401:
        elev.shape = (1201, 1201)
    else:
        raise ValueError(
            'Shape of SRTM data ({}) is unexpected.'.format(elev.size))

    fname = os.path.basename(fname)
    y_dir, y, x_dir, x = fname[0], int(fname[1:3]), fname[3], int(fname[4:7])

    if y_dir == 'S':
        y *= -1

    if x_dir == 'W':
        x *= -1

    return elev[::-1, ...], ccrs.PlateCarree(), (x, x + 1, y, y + 1)


read_SRTM3 = read_SRTM
read_SRTM1 = read_SRTM


def SRTM3_retrieve(lon, lat):
    """
    Return the path of a .hgt file for the given SRTM location.

    If no such .hgt file exists (because it is over the ocean)
    None will be returned.

    """
    warnings.warn("This method has been deprecated. "
                  "See the \"What's new\" section for v0.12.")
    return SRTM3Source().srtm_fname(lon, lat)


class SRTMDownloader(Downloader):
    """
    Provide a SRTM download mechanism.

    """
    FORMAT_KEYS = ('config', 'resolution', 'x', 'y')

    _SRTM_BASE_URL = ('https://e4ftl01.cr.usgs.gov/MEASURES/'
                      'SRTMGL{resolution}.003/2000.02.11/')
    _SRTM_LOOKUP_CACHE = os.path.join(os.path.dirname(__file__),
                                      'srtm.npz')
    _SRTM_LOOKUP_MASK = np.load(_SRTM_LOOKUP_CACHE)['mask']
    """
    The SRTM lookup mask determines whether keys such as 'N43E043' are
    available to download.

    """
    def __init__(self,
                 target_path_template,
                 pre_downloaded_path_template='',
                 ):
        # adds some SRTM defaults to the __init__ of a Downloader
        # namely, the URL is determined on the fly using the
        # ``SRTMDownloader._SRTM_LOOKUP_MASK`` array
        Downloader.__init__(self, None,
                            target_path_template,
                            pre_downloaded_path_template)

    def url(self, format_dict):
        warnings.warn('SRTM requires an account set up and log in to access. '
                      'Use of this Downloader is likely to fail with HTTP 401 '
                      'errors.')

        # override the url method, looking up the url from the
        # ``SRTMDownloader._SRTM_LOOKUP_MASK`` array
        lat = int(format_dict['y'][1:])
        # Change to co-latitude.
        if format_dict['y'][0] == 'N':
            colat = 90 - lat
        else:
            colat = 90 + lat

        lon = int(format_dict['x'][1:4])
        # Ensure positive.
        if format_dict['x'][0] == 'W':
            lon = 360 - lon

        if SRTMDownloader._SRTM_LOOKUP_MASK[lon, colat]:
            return (SRTMDownloader._SRTM_BASE_URL +
                    u'{y}{x}.SRTMGL{resolution}.hgt.zip').format(**format_dict)
        else:
            return None

    def acquire_resource(self, target_path, format_dict):
        from zipfile import ZipFile

        target_dir = os.path.dirname(target_path)
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)

        url = self.url(format_dict)

        srtm_online = self._urlopen(url)
        zfh = ZipFile(six.BytesIO(srtm_online.read()), 'r')

        zip_member_path = u'{y}{x}.hgt'.format(**format_dict)
        member = zfh.getinfo(zip_member_path)
        with open(target_path, 'wb') as fh:
            fh.write(zfh.open(member).read())

        srtm_online.close()
        zfh.close()

        return target_path

    @staticmethod
    def _create_srtm_mask(resolution, filename=None):
        """
        Return a NumPy mask of available lat/lon.

        This is slow as it must query the SRTM server to identify the
        continent from which the tile comes. Hence a NumPy file with this
        content exists in ``SRTMDownloader._SRTM_LOOKUP_CACHE``.

        The NumPy file was created with::

            import cartopy.io.srtm as srtm
            import numpy as np
            np.savez_compressed(srtm.SRTMDownloader._SRTM_LOOKUP_CACHE,
                                mask=srtm.SRTMDownloader._create_srtm_mask(3))

        """
        # lazy imports. In most situations, these are not
        # dependencies of cartopy.
        from bs4 import BeautifulSoup
        if filename is None:
            from six.moves.urllib.request import urlopen
            url = SRTMDownloader._SRTM_BASE_URL.format(resolution=resolution)
            with urlopen(url) as f:
                html = f.read()
        else:
            with open(filename) as f:
                html = f.read()

        mask = np.zeros((360, 181), dtype=np.bool)

        soup = BeautifulSoup(html)

        for link in soup('a'):
            name = str(link.text).strip()
            if name[0] in 'NS' and name.endswith('.hgt.zip'):
                lat = int(name[1:3])
                # Change to co-latitude.
                if name[0] == 'N':
                    colat = 90 - lat
                else:
                    colat = 90 + lat

                lon = int(name[4:7])
                # Ensure positive.
                if name[3] == 'W':
                    lon = 360 - lon

                mask[lon, colat] = True

        return mask

    @classmethod
    def default_downloader(cls):
        """
        Return a typical downloader for this class. In general, this static
        method is used to create the default configuration in cartopy.config

        """
        default_spec = ('SRTM', 'SRTMGL{resolution}', '{y}{x}.hgt')
        target_path_template = os.path.join('{config[data_dir]}',
                                            *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)
        return cls(target_path_template=target_path_template,
                   pre_downloaded_path_template=pre_path_template)


# add a generic SRTM downloader to the config 'downloaders' section.
config['downloaders'].setdefault(('SRTM', 'SRTM3'),
                                 SRTMDownloader.default_downloader())
config['downloaders'].setdefault(('SRTM', 'SRTM1'),
                                 SRTMDownloader.default_downloader())
