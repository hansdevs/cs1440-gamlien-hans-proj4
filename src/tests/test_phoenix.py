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
from phoenix import Phoenix
from palettes.phoenix_palette import PhoenixPalette

class TestPhoenix(unittest.TestCase):
    def setUp(self):
        # Create a test fractal configuration
        self.test_config = {
            'name': 'test_phoenix',
            'type': 'phoenix',
            'centerX': 0.0,
            'centerY': 0.0,
            'axisLength': 3.25,
            'iterations': 101,
            'creal': 0.5667,
            'cimag': 0.0,
            'preal': -0.5,
            'pimag': 0.0
        }
        self.fractal = Phoenix(self.test_config)
        self.palette = PhoenixPalette(self.fractal.iterations)
        
    def test_phoenix_count(self):
        """Phoenix fractal algorithm outputs the expected counts at key locations"""
        # Test the iteration counts
        self.assertEqual(5, self.fractal.count(complex(0, 0)))
        self.assertEqual(2, self.fractal.count(complex(-0.751, 1.1075)))
        self.assertEqual(3, self.fractal.count(complex(-0.2, 1.1075)))
        self.assertEqual(1, self.fractal.count(complex(-0.750, 0.1075)))
        
    def test_phoenix_palette(self):
        """Phoenix palette contains the expected colors"""
        # Test the colors from the palette
        self.assertEqual('#ffe4b5', self.palette.get_color(0))
        self.assertEqual('#ffeca5', self.palette.get_color(5))
        self.assertEqual('#7eff47', self.palette.get_color(35))
        self.assertEqual('#00277a', self.palette.get_color(100))
        
    def test_palette_length(self):
        """Color palette contains the expected number of colors"""
        self.assertEqual(101, len(self.palette.colors))


if __name__ == '__main__':
    unittest.main()
