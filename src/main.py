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

import sys
from fractalfactory import fractal_factory
from palettefactory import palette_factory
from image import ImagePainter

def main():
    """
    Main function to process command line arguments and render fractals.
    
    Usage:
        main.py [FRACTAL_FILE|default [PALETTE_NAME]]
    """
    # Create the fractal object
    if len(sys.argv) > 1:
        f = fractal_factory(sys.argv[1])
    else:
        f = fractal_factory()
    
    # Create the palette object
    if len(sys.argv) > 2:
        p = palette_factory(sys.argv[2], f.iterations)
    else:
        p = palette_factory(None, f.iterations)
    
    # Create the image painter and render the fractal
    painter = ImagePainter()
    painter.paint(f, p)

if __name__ == "__main__":
    main()
