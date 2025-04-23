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

from palettes.mandelbrot_palette import MandelbrotPalette
from palettes.phoenix_palette import PhoenixPalette
from palettes.grayscale_palette import GrayscalePalette
from palettes.fire_palette import FirePalette
from palettes.ocean_palette import OceanPalette
from palettes.citrus_palette import CitrusPalette

def palette_factory(name=None, num_colors=256):
    """
    Create a palette object based on the given name and number of colors.
    
    Args:
        name (str, optional): Name of the palette to create. If None, a default palette is created.
        num_colors (int): Number of colors in the palette.
    
    Returns:
        Palette: A concrete subclass of Palette
        
    Raises:
        NotImplementedError: If the palette name is not supported
    """
    if name is None:
        print("palette_factory: creating default color palette")
        return MandelbrotPalette(num_colors)
    
    name = name.lower()
    
    if name == 'mandelbrot':
        return MandelbrotPalette(num_colors)
    elif name == 'phoenix':
        return PhoenixPalette(num_colors)
    elif name == 'grayscale':
        return GrayscalePalette(num_colors)
    elif name == 'fire':
        return FirePalette(num_colors)
    elif name == 'ocean':
        return OceanPalette(num_colors)
    elif name == 'citrus':
        return CitrusPalette(num_colors)
    else:
        raise NotImplementedError(f"Unsupported palette '{name}'")
