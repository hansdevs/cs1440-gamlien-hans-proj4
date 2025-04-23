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
from palettes import mandelbrot_palette, phoenix_palette

class TestPalettes(unittest.TestCase):
    def test_mandelbrot_palette_contains_strings(self):
        """Test that the Mandelbrot palette contains only strings"""
        palette = mandelbrot_palette.MandelbrotPalette(100)
        for color in palette.colors:
            self.assertIsInstance(color, str)
    
    def test_phoenix_palette_contains_strings(self):
        """Test that the Phoenix palette contains only strings"""
        palette = phoenix_palette.PhoenixPalette(100)
        for color in palette.colors:
            self.assertIsInstance(color, str)

if __name__ == '__main__':
    unittest.main()
