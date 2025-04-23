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
import image

class TestImage(unittest.TestCase):
    def test_status_bar_format(self):
        """Test that the status bar is formatted correctly"""
        # Test at 0% complete
        status = image.status_bar(512, 0)
        self.assertEqual(status, '[  0%                                  ]')
        
        # Test at 50% complete
        status = image.status_bar(256, 0)
        self.assertEqual(status, '[ 50% =================                ]')
        
        # Test at 100% complete
        status = image.status_bar(0, 0)
        self.assertEqual(status, '[100% =================================]')

if __name__ == '__main__':
    unittest.main()
