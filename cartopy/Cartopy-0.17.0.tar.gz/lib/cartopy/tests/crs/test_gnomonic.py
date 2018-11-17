# (C) British Crown Copyright 2018, Met Office
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
Tests for the Gnomonic coordinate system.

"""

from __future__ import (absolute_import, division, print_function)

import numpy as np
from numpy.testing import assert_almost_equal
import pytest

import cartopy.crs as ccrs


def check_proj4_params(crs, other_args):
    expected = other_args | {'proj=gnom', 'no_defs'}
    pro4_params = set(crs.proj4_init.lstrip('+').split(' +'))
    assert expected == pro4_params


def test_default():
    gnom = ccrs.Gnomonic()
    other_args = {'ellps=WGS84', 'lon_0=0.0', 'lat_0=0.0'}
    check_proj4_params(gnom, other_args)

    assert_almost_equal(np.array(gnom.x_limits),
                        [-5e7, 5e7])
    assert_almost_equal(np.array(gnom.y_limits),
                        [-5e7, 5e7])


@pytest.mark.parametrize('lat', [-10, 0, 10])
@pytest.mark.parametrize('lon', [-10, 0, 10])
def test_central_params(lat, lon):
    gnom = ccrs.Gnomonic(central_latitude=lat, central_longitude=lon)
    other_args = {'lat_0={}'.format(lat), 'lon_0={}'.format(lon),
                  'ellps=WGS84'}
    check_proj4_params(gnom, other_args)

    assert_almost_equal(np.array(gnom.x_limits),
                        [-5e7, 5e7])
    assert_almost_equal(np.array(gnom.y_limits),
                        [-5e7, 5e7])


def test_grid():
    # USGS Professional Paper 1395, pg 168, Table 26
    globe = ccrs.Globe(ellipse=None,
                       semimajor_axis=1.0, semiminor_axis=1.0)
    gnom = ccrs.Gnomonic(globe=globe)
    geodetic = gnom.as_geodetic()

    other_args = {'a=1.0', 'b=1.0', 'lon_0=0.0', 'lat_0=0.0'}
    check_proj4_params(gnom, other_args)

    assert_almost_equal(np.array(gnom.x_limits),
                        [-5e7, 5e7])
    assert_almost_equal(np.array(gnom.y_limits),
                        [-5e7, 5e7])

    lats, lons = np.mgrid[0:90:10, 0:90:10].reshape((2, -1))
    expected_x = np.tile(
        [0.0000, 0.1763, 0.3640, 0.5774, 0.8391, 1.1918, 1.7321, 2.7475,
         5.6713],
        9)
    expected_y = np.array([
        [5.6713, 2.7475, 1.7321, 1.1918, 0.8391, 0.5774, 0.3640, 0.1763, 0],
        [5.7588, 2.7899, 1.7588, 1.2101, 0.8520, 0.5863, 0.3696, 0.1790, 0],
        [6.0353, 2.9238, 1.8432, 1.2682, 0.8930, 0.6144, 0.3873, 0.1876, 0],
        [6.5486, 3.1725, 2.0000, 1.3761, 0.9689, 0.6667, 0.4203, 0.2036, 0],
        [7.4033, 3.5866, 2.2610, 1.5557, 1.0954, 0.7537, 0.4751, 0.2302, 0],
        [8.8229, 4.2743, 2.6946, 1.8540, 1.3054, 0.8982, 0.5662, 0.2743, 0],
        [11.3426, 5.4950, 3.4641, 2.3835, 1.6782, 1.1547, 0.7279, 0.3527, 0],
        [16.5817, 8.0331, 5.0642, 3.4845, 2.4534, 1.6881, 1.0642, 0.5155, 0],
        [32.6596, 15.8221, 9.9745, 6.8630, 4.8322, 3.3248, 2.0960, 1.0154, 0],
    ])[:, ::-1].T.ravel()

    # Test all quadrants; they are symmetrical.
    for lon_sign in [1, -1]:
        for lat_sign in [1, -1]:
            result = gnom.transform_points(geodetic,
                                           lon_sign * lons, lat_sign * lats)
            assert_almost_equal(result[:, 0], lon_sign * expected_x, decimal=4)
            assert_almost_equal(result[:, 1], lat_sign * expected_y, decimal=4)


def test_sphere_transform():
    # USGS Professional Paper 1395, pp 319 - 320
    globe = ccrs.Globe(semimajor_axis=1.0, semiminor_axis=1.0,
                       ellipse=None)
    gnom = ccrs.Gnomonic(central_latitude=40.0, central_longitude=-100.0,
                         globe=globe)
    geodetic = gnom.as_geodetic()

    other_args = {'a=1.0', 'b=1.0', 'lon_0=-100.0', 'lat_0=40.0'}
    check_proj4_params(gnom, other_args)

    assert_almost_equal(np.array(gnom.x_limits),
                        [-5e7, 5e7])
    assert_almost_equal(np.array(gnom.y_limits),
                        [-5e7, 5e7])

    result = gnom.transform_point(-110.0, 30.0, geodetic)
    assert_almost_equal(result, np.array([-0.1542826, -0.1694739]))

    inverse_result = geodetic.transform_point(result[0], result[1], gnom)
    assert_almost_equal(inverse_result, [-110.0, 30.0])
