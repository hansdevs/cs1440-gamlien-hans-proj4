#!/usr/bin/env python3

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.


import unittest
from palettefactory import palette_factory
from palettes.mandelbrot_palette import MandelbrotPalette
from palettes.phoenix_palette import PhoenixPalette
from palettes.grayscale_palette import GrayscalePalette
from palettes.fire_palette import FirePalette
from palettes.ocean_palette import OceanPalette
from palettes.citrus_palette import CitrusPalette

class TestPaletteFactory(unittest.TestCase):
    def test_default_palette(self):
        """Test that the default palette is created correctly"""
        palette = palette_factory(None, 100)
        self.assertIsInstance(palette, MandelbrotPalette)
        self.assertEqual(len(palette), 100)
    
    def test_mandelbrot_palette(self):
        """Test that a Mandelbrot palette is created correctly"""
        palette = palette_factory('mandelbrot', 100)
        self.assertIsInstance(palette, MandelbrotPalette)
        self.assertEqual(len(palette), 100)
    
    def test_phoenix_palette(self):
        """Test that a Phoenix palette is created correctly"""
        palette = palette_factory('phoenix', 100)
        self.assertIsInstance(palette, PhoenixPalette)
        self.assertEqual(len(palette), 100)
    
    def test_grayscale_palette(self):
        """Test that a Grayscale palette is created correctly"""
        palette = palette_factory('grayscale', 100)
        self.assertIsInstance(palette, GrayscalePalette)
        self.assertEqual(len(palette), 100)
    
    def test_fire_palette(self):
        """Test that a Fire palette is created correctly"""
        palette = palette_factory('fire', 100)
        self.assertIsInstance(palette, FirePalette)
        self.assertEqual(len(palette), 100)
    
    def test_ocean_palette(self):
        """Test that an Ocean palette is created correctly"""
        palette = palette_factory('ocean', 100)
        self.assertIsInstance(palette, OceanPalette)
        self.assertEqual(len(palette), 100)
    
    def test_citrus_palette(self):
        """Test that a Citrus palette is created correctly"""
        palette = palette_factory('citrus', 100)
        self.assertIsInstance(palette, CitrusPalette)
        self.assertEqual(len(palette), 100)
    
    def test_case_insensitivity(self):
        """Test that palette names are case-insensitive"""
        palette1 = palette_factory('MANDELBROT', 100)
        palette2 = palette_factory('mandelbrot', 100)
        self.assertIsInstance(palette1, MandelbrotPalette)
        self.assertIsInstance(palette2, MandelbrotPalette)
    
    def test_unsupported_palette(self):
        """Test that an unsupported palette raises NotImplementedError"""
        with self.assertRaises(NotImplementedError):
            palette_factory('unsupported', 100)


if __name__ == '__main__':
    unittest.main()
