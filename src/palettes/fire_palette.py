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

class FirePalette(Palette):
    def __init__(self, num_colors):
        super().__init__(num_colors)
        
        # Create a fire-themed palette
        self.colors = []
        
        # Divide the palette into 4 sections
        quarter = num_colors // 4
        
        # Black to red
        for i in range(quarter):
            r = min(255, int(i * 255 / quarter))
            g = 0
            b = 0
            self.colors.append(f'#{r:02x}{g:02x}{b:02x}')
        
        # Red to orange
        for i in range(quarter):
            r = 255
            g = min(165, int(i * 165 / quarter))
            b = 0
            self.colors.append(f'#{r:02x}{g:02x}{b:02x}')
        
        # Orange to yellow
        for i in range(quarter):
            r = 255
            g = min(255, 165 + int(i * 90 / quarter))
            b = 0
            self.colors.append(f'#{r:02x}{g:02x}{b:02x}')
        
        # Yellow to white
        for i in range(quarter, num_colors - 3 * quarter):
            r = 255
            g = 255
            b = min(255, int(i * 255 / quarter))
            self.colors.append(f'#{r:02x}{g:02x}{b:02x}')
        
    def get_color(self, n):
        return self.colors[n % len(self.colors)]
