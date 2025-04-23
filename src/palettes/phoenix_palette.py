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

class PhoenixPalette(Palette):
    def __init__(self, num_colors):
        super().__init__(num_colors)
        
        # Original Phoenix palette
        self.colors = ['#ffe4b5', '#ffe5b2', '#ffe7af', '#ffe8ac', '#ffeaa8', '#ffeca5',
                '#ffeea2', '#fff09f', '#fff39c', '#fff699', '#fff996', '#fffc92',
                '#ffff8f', '#fbff8c', '#f8ff89', '#f4ff86', '#f0ff83', '#ebff80',
                '#e7ff7d', '#e2ff79', '#deff76', '#d8ff73', '#d3ff70', '#ceff6d',
                '#c8ff6a', '#c2ff67', '#bcff63', '#b6ff60', '#b0ff5d', '#a9ff5a',
                '#a3ff57', '#9cff54', '#94ff51', '#8dff4d', '#86ff4a', '#7eff47',
                '#76ff44', '#6eff41', '#66ff3e', '#5dff3b', '#54ff37', '#4cff34',
                '#43ff31', '#39ff2e', '#30ff2b', '#28ff29', '#25ff2d', '#21ff31',
                '#1eff34', '#1bff39', '#18ff3d', '#15ff41', '#12ff46', '#0fff4b',
                '#0cff50', '#08ff55', '#05ff5b', '#02ff60', '#00fe66', '#00fb6d',
                '#00f873', '#00f579', '#00f17f', '#00ee84', '#00eb8a', '#00e88f',
                '#00e594', '#00e299', '#00df9e', '#00dba2', '#00d8a6', '#00d5aa',
                '#00d2ae', '#00cfb2', '#00ccb6', '#00c9b9', '#00c5bc', '#00c2bf',
                '#00bdbf', '#00b4bc', '#00abb9', '#00a3b6', '#009bb3', '#0092af',
                '#008bac', '#0083a9', '#007ba6', '#0074a3', '#006da0', '#00669d',
                '#005f9a', '#005996', '#005293', '#004c90', '#00468d', '#00418a',
                '#003b87', '#003684', '#003080', '#002b7d', '#00277a', '#002277']
        
        # If we need more colors than we have, repeat the palette
        while len(self.colors) < num_colors:
            self.colors.extend(self.colors)
        
        # Trim to the exact number needed
        self.colors = self.colors[:num_colors]
        
    def get_color(self, n):
        return self.colors[n % len(self.colors)]
