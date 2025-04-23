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
from mandelbrot import Mandelbrot
from palettes.mandelbrot_palette import MandelbrotPalette

class TestMandelbrot(unittest.TestCase):
    def setUp(self):
        self.test_config = {
            'name': 'test_mandelbrot',
            'type': 'mandelbrot',
            'centerX': -0.7,
            'centerY': 0.0,
            'axisLength': 2.55,
            'iterations': 100
        }
        self.fractal = Mandelbrot(self.test_config)
        self.palette = MandelbrotPalette(self.fractal.iterations)
        
    def test_mandelbrot_count(self):
        """Mandelbrot fractal algorithm outputs the expected counts at key locations"""
        self.assertEqual(99, self.fractal.count(complex(0, 0)))
        self.assertEqual(12, self.fractal.count(complex(-0.7562500000000001, -0.234375)))
        self.assertEqual(10, self.fractal.count(complex(0.3374999999999999, -0.625)))
        self.assertEqual(29, self.fractal.count(complex(-0.6781250000000001, -0.46875)))
        self.assertEqual(4,  self.fractal.count(complex(0.4937499999999999, -0.234375)))
        self.assertEqual(22, self.fractal.count(complex(0.3374999999999999, 0.546875)))
        
    def test_mandelbrot_palette(self):
        """Mandelbrot palette contains the expected colors"""
        self.assertEqual('#E1D89F', self.palette.get_color(0))
        self.assertEqual('#ACD788', self.palette.get_color(18))
        self.assertEqual('#6ECB8A', self.palette.get_color(38))
        self.assertEqual('#455AAB', self.palette.get_color(78))
        self.assertEqual('#613F94', self.palette.get_color(94))
        self.assertEqual('#CADC92', self.palette.get_color(110))
        
    def test_palette_length(self):
        """Palette contains the expected number of colors"""
        self.assertEqual(100, len(self.palette.colors))


if __name__ == '__main__':
    unittest.main()
