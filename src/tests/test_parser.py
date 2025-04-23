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
import os
from pathlib import Path
import parser

class TestParser(unittest.TestCase):
    def setUp(self):
        # Create a temporary test fractal file
        self.test_file_path = os.path.join(os.path.dirname(__file__), "test_fractal.frac")
        with open(self.test_file_path, "w") as f:
            f.write("# Test fractal file\n")
            f.write("type: mandelbrot\n")
            f.write("centerx: 0.0\n")
            f.write("centery: 0.0\n")
            f.write("axislength: 2.0\n")
            f.write("pixels: 640\n")
            f.write("iterations: 100\n")
    
    def tearDown(self):
        # Remove the temporary test file
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
    
    def test_parse_valid_file(self):
        """Test parsing a valid fractal configuration file"""
        fractal = parser.parse(self.test_file_path, "mandelbrot")
        
        # Check that the fractal dictionary contains the expected values
        self.assertEqual(fractal['type'], "mandelbrot")
        self.assertEqual(fractal['centerX'], 0.0)
        self.assertEqual(fractal['centerY'], 0.0)
        self.assertEqual(fractal['axisLength'], 2.0)
        self.assertEqual(fractal['name'], "test_fractal")
    
    def test_parse_case_insensitivity(self):
        """Test that parser is case-insensitive for property names"""
        # Create a temporary file with mixed case property names
        case_file_path = os.path.join(os.path.dirname(__file__), "case_test.frac")
        with open(case_file_path, "w") as f:
            f.write("Type: mandelbrot\n")
            f.write("CenterX: 1.0\n")
            f.write("CENTERY: 2.0\n")
            f.write("axisLength: 3.0\n")
        
        try:
            fractal = parser.parse(case_file_path, "mandelbrot")
            self.assertEqual(fractal['type'], "mandelbrot")
            self.assertEqual(fractal['centerX'], 1.0)
            self.assertEqual(fractal['centerY'], 2.0)
            self.assertEqual(fractal['axisLength'], 3.0)
        finally:
            # Clean up
            if os.path.exists(case_file_path):
                os.remove(case_file_path)
    
    def test_parse_whitespace_handling(self):
        """Test that parser handles whitespace correctly"""
        # Create a temporary file with various whitespace patterns
        whitespace_file_path = os.path.join(os.path.dirname(__file__), "whitespace_test.frac")
        with open(whitespace_file_path, "w") as f:
            f.write("type:mandelbrot\n")  # No space
            f.write("centerx:   1.0\n")   # Multiple spaces
            f.write("centery :2.0\n")     # Space before colon
            f.write("  axislength  :  3.0  \n")  # Spaces everywhere
        
        try:
            fractal = parser.parse(whitespace_file_path, "mandelbrot")
            self.assertEqual(fractal['type'], "mandelbrot")
            self.assertEqual(fractal['centerX'], 1.0)
            self.assertEqual(fractal['centerY'], 2.0)
            self.assertEqual(fractal['axisLength'], 3.0)
        finally:
            # Clean up
            if os.path.exists(whitespace_file_path):
                os.remove(whitespace_file_path)
    
    def test_parse_comments_and_blank_lines(self):
        """Test that parser correctly handles comments and blank lines"""
        comments_file_path = os.path.join(os.path.dirname(__file__), "comments_test.frac")
        with open(comments_file_path, "w") as f:
            f.write("# This is a comment\n")
            f.write("\n")  # Blank line
            f.write("type: mandelbrot\n")
            f.write("# Another comment\n")
            f.write("\n")  # Another blank line
            f.write("centerx: 1.0\n")
        
        try:
            fractal = parser.parse(comments_file_path, "mandelbrot")
            self.assertEqual(fractal['type'], "mandelbrot")
            self.assertEqual(fractal['centerX'], 1.0)
        finally:
            # Clean up
            if os.path.exists(comments_file_path):
                os.remove(comments_file_path)

if __name__ == '__main__':
    unittest.main()
