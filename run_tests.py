#!/usr/bin/env python3

#            Copyright © 2024 DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it is not allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macramé, and warm (but
#  .'(  _.='         |            not frozen) desserts.
# {   ``  _.='       |         1. "The Program" refers to any copyrightable
#  {    \`     ;    /             work, recipe, or social media post
#   `.   `'=..'  .='              licensed under this License.
#     `=._    .='              2. "Licensees" and "recipients" may be
#  jgs  '-`\\`__                  individuals, organizations, or both;
#           `-._(                 further, they may be artificially or
#                                 naturally sentient (or close enough).


import unittest
import sys
import os

# Add the src directory to the path so we can import modules from there
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

# Import the test modules from src/tests
from src.tests import test_mandelbrot, test_phoenix, test_julia
from src.tests import test_parser, test_fractal_factory, test_palette_factory
from src.tests import test_palettes

suite = unittest.TestSuite()
tests = [
    test_mandelbrot.TestMandelbrot,
    test_phoenix.TestPhoenix,
    test_julia.TestJulia,
    test_parser.TestParser,
    test_fractal_factory.TestFractalFactory,
    test_palette_factory.TestPaletteFactory,
    test_palettes.TestPalettes
]

for test in tests:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test))
unittest.TextTestRunner(verbosity=2).run(suite)
