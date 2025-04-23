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

class GrayscalePalette(Palette):
    def __init__(self, num_colors):
        super().__init__(num_colors)
        
        # Create a grayscale palette
        self.colors = []
        
        # Generate a gradient from black to white and back
        half_colors = num_colors // 2
        
        # Black to white
        for i in range(half_colors):
            v = min(255, int(i * 255 / half_colors))
            self.colors.append(f'#{v:02x}{v:02x}{v:02x}')
        
        # White to black
        for i in range(half_colors, num_colors):
            v = min(255, int((num_colors - i) * 255 / half_colors))
            self.colors.append(f'#{v:02x}{v:02x}{v:02x}')
        
    def get_color(self, n):
        return self.colors[n % len(self.colors)]
