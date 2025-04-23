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
import parser
from pathlib import Path

class TestFileHandling(unittest.TestCase):
    def setUp(self):
        # Create a test directory if it doesn't exist
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_files")
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create a test fractal file with absolute path
        self.abs_path_file = os.path.join(self.test_dir, "absolute_path.frac")
        with open(self.abs_path_file, "w") as f:
            f.write("type: mandelbrot\n")
            f.write("centerx: 1.0\n")
            f.write("centery: 2.0\n")
            f.write("axislength: 3.0\n")
    
    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.abs_path_file):
            os.remove(self.abs_path_file)
        
        # Try to remove the test directory (will only succeed if empty)
        try:
            os.rmdir(self.test_dir)
        except:
            pass
    
    def test_absolute_path_handling(self):
        """Test that the parser can handle absolute file paths"""
        fractal = parser.parse(self.abs_path_file)
        self.assertEqual(fractal['type'], "mandelbrot")
        self.assertEqual(fractal['centerx'], 1.0)
        self.assertEqual(fractal['centery'], 2.0)
        self.assertEqual(fractal['axislength'], 3.0)
        self.assertEqual(fractal['name'], "absolute_path")
    
    def test_file_not_found(self):
        """Test that the parser raises FileNotFoundError for non-existent files"""
        non_existent_file = os.path.join(self.test_dir, "does_not_exist.frac")
        with self.assertRaises(FileNotFoundError):
            parser.parse(non_existent_file)

if __name__ == '__main__':
    unittest.main()
