#!/usr/bin/env python3

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \\             the above copyright notice, this list of
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

import os
import unittest
from fractalfactory import fractal_factory
from mandelbrot import Mandelbrot, MandelbrotPow3, MandelbrotPow4

class TestFractalFactory(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_files")
        os.makedirs(self.test_dir, exist_ok=True)
        self.mandelbrot_file = os.path.join(self.test_dir, "test_mandelbrot.frac")
        with open(self.mandelbrot_file, "w") as f:
            f.write("type: mandelbrot\n")
            f.write("centerx: 0.0\n")
            f.write("centery: 0.0\n")
            f.write("axislength: 2.0\n")
            f.write("iterations: 100\n")
        self.mandelbrot3_file = os.path.join(self.test_dir, "test_mandelbrot3.frac")
        with open(self.mandelbrot3_file, "w") as f:
            f.write("type: mandelbrot3\n")
            f.write("centerx: 0.0\n")
            f.write("centery: 0.0\n")
            f.write("axislength: 2.7\n")
            f.write("iterations: 96\n")
        self.mandelbrot4_file = os.path.join(self.test_dir, "test_mandelbrot4.frac")
        with open(self.mandelbrot4_file, "w") as f:
            f.write("type: mandelbrot4\n")
            f.write("centerx: -0.2\n")
            f.write("centery: 0.0\n")
            f.write("axislength: 2.4\n")
            f.write("iterations: 96\n")
        self.phoenix_file = os.path.join(self.test_dir, "test_phoenix.frac")
        with open(self.phoenix_file, "w") as f:
            f.write("type: phoenix\n")
            f.write("centerx: 0.0\n")
            f.write("centery: 0.0\n")
            f.write("axislength: 3.25\n")
            f.write("iterations: 101\n")
            f.write("creal: 0.5667\n")
            f.write("cimag: 0.0\n")
            f.write("preal: -0.5\n")
            f.write("pimag: 0.0\n")
        self.julia_file = os.path.join(self.test_dir, "test_julia.frac")
        with open(self.julia_file, "w") as f:
            f.write("type: julia\n")
            f.write("centerx: 0.0\n")
            f.write("centery: 0.0\n")
            f.write("axislength: 4.0\n")
            f.write("iterations: 78\n")

    def tearDown(self):
        for file in [self.mandelbrot_file, self.mandelbrot3_file, self.mandelbrot4_file,
                     self.phoenix_file, self.julia_file]:
            if os.path.exists(file):
                os.remove(file)
        try:
            os.rmdir(self.test_dir)
        except OSError:
            pass

    def test_default_fractal(self):
        fractal = fractal_factory()
        self.assertIsInstance(fractal, Mandelbrot)
        self.assertEqual(fractal.centerX, -0.7)
        self.assertEqual(fractal.centerY, 0.0)
        self.assertEqual(fractal.axisLength, 2.55)
        self.assertEqual(fractal.iterations, 256)
        self.assertEqual(fractal.name, 'default')

    def test_mandelbrot_fractal(self):
        fractal = fractal_factory(self.mandelbrot_file)
        self.assertIsInstance(fractal, Mandelbrot)
        self.assertEqual(fractal.centerX, 0.0)
        self.assertEqual(fractal.centerY, 0.0)
        self.assertEqual(fractal.axisLength, 2.0)
        self.assertEqual(fractal.iterations, 100)
        self.assertEqual(fractal.name, 'test_mandelbrot')

    def test_mandelbrot3_fractal(self):
        fractal = fractal_factory(self.mandelbrot3_file)
        self.assertIsInstance(fractal, MandelbrotPow3)
        self.assertEqual(fractal.centerX, 0.0)
        self.assertEqual(fractal.centerY, 0.0)
        self.assertEqual(fractal.axisLength, 2.7)
        self.assertEqual(fractal.iterations, 96)
        self.assertEqual(fractal.name, 'test_mandelbrot3')

    def test_mandelbrot4_fractal(self):
        fractal = fractal_factory(self.mandelbrot4_file)
        self.assertIsInstance(fractal, MandelbrotPow4)
        self.assertEqual(fractal.centerX, -0.2)
        self.assertEqual(fractal.centerY, 0.0)
        self.assertEqual(fractal.axisLength, 2.4)
        self.assertEqual(fractal.iterations, 96)
        self.assertEqual(fractal.name, 'test_mandelbrot4')

    def test_phoenix_fractal(self):
        """Test that creating a Phoenix fractal without required parameters raises RuntimeError"""
        with self.assertRaises(RuntimeError) as cm:
            fractal_factory(self.phoenix_file)
        self.assertIn("Missing required parameter 'creal'", str(cm.exception))

    def test_julia_fractal(self):
        """Test that creating a Julia fractal without parameters raises RuntimeError"""
        with self.assertRaises(RuntimeError) as cm:
            fractal_factory(self.julia_file)
        self.assertIn("Missing required parameter 'creal'", str(cm.exception))

if __name__ == '__main__':
    unittest.main()

