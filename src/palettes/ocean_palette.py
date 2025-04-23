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

from palette import Palette

class OceanPalette(Palette):
    def __init__(self, num_colors):
        super().__init__(num_colors)
        
        # Create an ocean-themed palette
        self.colors = []
        
        # Divide the palette into 3 sections
        third = num_colors // 3
        
        # Dark blue to medium blue
        for i in range(third):
            r = 0
            g = min(128, int(i * 128 / third))
            b = min(255, 128 + int(i * 127 / third))
            self.colors.append(f'#{r:02x}{g:02x}{b:02x}')
        
        # Medium blue to cyan
        for i in range(third):
            r = 0
            g = min(255, 128 + int(i * 127 / third))
            b = 255
            self.colors.append(f'#{r:02x}{g:02x}{b:02x}')
        
        # Cyan to white
        for i in range(third, num_colors - 2 * third):
            r = min(255, int(i * 255 / third))
            g = 255
            b = 255
            self.colors.append(f'#{r:02x}{g:02x}{b:02x}')
        
    def get_color(self, n):
        return self.colors[n % len(self.colors)]
