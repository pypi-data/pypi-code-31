# -*- coding: utf-8 -*-
import pickle
import socket
import tempfile
import unittest
from contextlib import suppress
from copy import copy
from copy import copy
from math import radians
from pathlib import Path

import numpy as np

from crystals import Atom
from crystals import Crystal
from crystals import Lattice
from crystals.affine import rotation_matrix
from crystals.affine import transform


def connection_available():
    """ Returns whether or not an internet connection is available """
    with suppress(OSError):
        try:
            socket.create_connection(("www.google.com", 80))
        except:
            return False
        else:
            return True
    return False


class TestSpglibMethods(unittest.TestCase):
    def test_symmetry_graphite(self):
        """ Test that Crystal.symmetry() works correctly for graphite """
        c = Crystal.from_database("C")
        info = c.symmetry()

        supposed = {
            "international_number": 194,
            "hall_number": 488,
            "international_symbol": "P6_3/mmc",
            "international_full": "P 6_3/m 2/m 2/c",
            "hall_symbol": "-P 6c 2c",
            "pointgroup": "D6h",
        }

        self.assertDictEqual(info, supposed)

    def test_primitive_for_builtins(self):
        """ Test that all built-in crystal have a primitive cell """
        for name in Crystal.builtins:
            with self.subTest(name):
                c = Crystal.from_database(name)
                prim = c.primitive(symprec=0.1)
                self.assertLessEqual(len(prim), len(c))

    def test_primitive_uniqueness(self):
        """ Test that the primitive cell of a primitive cell is itself """
        for name in Crystal.builtins:
            with self.subTest(name):
                c = Crystal.from_database(name)
                prim = c.primitive(symprec=0.1)
                prim2 = prim.primitive(symprec=0.1)
                self.assertIs(prim, prim2)


class TestCrystalSpecialMethods(unittest.TestCase):
    def test_str_vs_repr(self):
        """ Test that str and repr are workign as expected """
        for name in Crystal.builtins:
            with self.subTest(name):
                c = Crystal.from_database(name)

                # If small crystal, repr and str should be the same
                if len(c) <= 10:
                    self.assertEqual(repr(c), str(c))
                else:
                    self.assertNotEqual(repr(c), str(c))


class TestCrystalRotations(unittest.TestCase):
    def setUp(self):
        self.crystal = Crystal.from_database(next(iter(Crystal.builtins)))

    def test_crystal_equality(self):
        """ Tests that Crystal.__eq__ is working properly """
        self.assertEqual(self.crystal, self.crystal)

        cryst2 = copy(self.crystal)
        cryst2.transform(
            2 * np.eye(3)
        )  # This stretches lattice vectors, symmetry operators
        self.assertFalse(self.crystal is cryst2)
        self.assertNotEqual(self.crystal, cryst2)

        cryst2.transform(0.5 * np.eye(3))
        self.assertEqual(self.crystal, cryst2)

    def test_trivial_rotation(self):
        """ Test rotation by 360 deg around all axes. """
        unrotated = copy(self.crystal)
        r = rotation_matrix(radians(360), [0, 0, 1])
        self.crystal.transform(r)

        self.assertEqual(self.crystal, unrotated)

    def test_identity_transform(self):
        """ Tests the trivial identity transform """
        transf = copy(self.crystal)
        transf.transform(np.eye(3))
        self.assertEqual(self.crystal, transf)

    def test_one_axis_rotation(self):
        """ Tests the crystal orientation after rotations. """
        unrotated = copy(self.crystal)
        self.crystal.transform(rotation_matrix(radians(37), [0, 1, 0]))
        self.assertNotEqual(unrotated, self.crystal)
        self.crystal.transform(rotation_matrix(radians(-37), [0, 1, 0]))
        self.assertEqual(unrotated, self.crystal)

    def test_wraparound_rotation(self):
        cryst1 = copy(self.crystal)
        cryst2 = copy(self.crystal)

        cryst1.transform(rotation_matrix(radians(22.3), [0, 0, 1]))
        cryst2.transform(rotation_matrix(radians(22.3 - 360), [0, 0, 1]))
        self.assertEqual(cryst1, cryst2)


class TestCrystalConstructors(unittest.TestCase):
    def test_builtins(self):
        """ Test that all names in Crystal.builtins build without errors,
        and that Crystal.source is correctly recorded. """
        for name in Crystal.builtins:
            with self.subTest(name):
                c = Crystal.from_database(name)

                self.assertIn(name, c.source)

    def test_builtins_wrong_name(self):
        """ Test that a name not in Crystal.builtins will raise a ValueError """
        with self.assertRaises(ValueError):
            c = Crystal.from_database("___")

    @unittest.skipUnless(connection_available(), "Internet connection is required.")
    def test_from_pdb(self):
        """ Test Crystal.from_pdb constructor """
        c = Crystal.from_pdb("1fbb")
        self.assertIn("1fbb", c.source)

    @unittest.skipUnless(connection_available(), "Internet connection is required.")
    def test_from_cod(self):
        """ Test building a Crystal object from the COD """
        # revision = None and latest revision should give the same Crystal
        c = Crystal.from_cod(1521124)
        c2 = Crystal.from_cod(1521124, revision=176429)

        self.assertEqual(c, c2)

    @unittest.skipUnless(connection_available(), "Internet connection is required.")
    def test_from_cod_new_dir(self):
        """ Test that a cache dir is created by Crystal.from_cod """
        with tempfile.TemporaryDirectory() as temp_dir:
            download_dir = Path(temp_dir) / "test_cod"
            self.assertFalse(download_dir.exists())
            c = Crystal.from_cod(1521124, download_dir=download_dir)
            self.assertTrue(download_dir.exists())


if __name__ == "__main__":
    unittest.main()
