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
from julia import Julia
from palettes.mandelbrot_palette import MandelbrotPalette

class TestJulia(unittest.TestCase):
    def setUp(self):
        # Create a test fractal configuration
        self.test_config = {
            'name': 'test_julia',
            'type': 'julia',
            'centerX': 0.0,
            'centerY': 0.0,
            'axisLength': 4.0,
            'iterations': 78,
            'creal': -1.0125,
            'cimag': 0.275
        }
        self.fractal = Julia(self.test_config)
        self.palette = MandelbrotPalette(self.fractal.iterations)
        
    def test_julia_count(self):
        """Julia fractal algorithm outputs the expected counts at key locations"""
        # Test the iteration counts
        self.assertEqual(77, self.fractal.count(complex(0, 0)))
        self.assertEqual(0, self.fractal.count(complex(-0.751, 1.1075)))
        self.assertEqual(0, self.fractal.count(complex(-0.2, 1.1075)))
        self.assertEqual(9, self.fractal.count(complex(-0.750, 0.1075)))
        
    def test_julia_palette(self):
        """Julia palette contains the expected colors"""
        # Test the colors from the palette
        self.assertEqual('#E1D89F', self.palette.get_color(0))
        self.assertEqual('#E0DA9E', self.palette.get_color(1))
        self.assertEqual('#E0DC9C', self.palette.get_color(2))
        
    def test_palette_length(self):
        """Color palette contains the expected number of colors"""
        self.assertEqual(78, len(self.palette.colors))


if __name__ == '__main__':
    unittest.main()
