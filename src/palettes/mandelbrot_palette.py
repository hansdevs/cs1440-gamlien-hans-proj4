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

class MandelbrotPalette(Palette):
    def __init__(self, num_colors):
        super().__init__(num_colors)
        
        # Define color constants
        CUSTARD = '#E1D89F'
        PISTACHIO = '#A8D786'
        MINT = '#6ECB8A'
        ELDERBERRY = '#4771B2'
        CONCORD_GRAPE = '#51419C'
        PLUM = '#7D387D'
        
        # This color palette contains 111 color steps.
        self.colors = [CUSTARD, '#E0DA9E', '#E0DC9C', '#DFDE9B', '#DEDF9A', '#DBDE98',
                   '#D8DE97', '#D4DD96', '#D1DD94', '#CDDC93', '#CADC92', '#C6DB91',
                   '#C3DB8F', '#BFDA8E', '#BCD98D', '#B8D98B', '#B4D88A', '#B0D889',
                   '#ACD788', PISTACHIO,'#A4D685','#A0D684', '#9CD582', '#98D481',
                   '#94D480', '#8FD37F', '#8BD37D', '#87D27C', '#82D17B', '#7ED17A',
                   '#79D078', '#77D07A', '#76CF7C', '#75CF7E', '#73CE80', '#72CD83',
                   '#71CD85', '#70CC87', MINT,    '#6DCB8C', '#6CCA8F', '#6BCA91',
                   '#69C994', '#68C896', '#67C899', '#66C79C', '#65C79F', '#63C6A2',
                   '#62C5A4', '#61C5A7', '#60C4AA', '#5FC3AD', '#5DC3B0', '#5CC2B3',
                   '#5BC1B7', '#5AC1BA', '#59C0BD', '#57BFBF', '#56BABF', '#55B5BE',
                   '#54B1BD', '#53ACBD', '#51A7BC', '#50A3BB', '#4F9EBB', '#4E99BA',
                   '#4D94B9', '#4C8FB9', '#4A8AB8', '#4985B7', '#4880B7', '#487BB5',
                   '#4876B4', ELDERBERRY,'#476CB1','#4668AF','#4663AE', '#465EAC',
                   '#455AAB', '#4556A9', '#4551A8', '#444DA6', '#4449A5', '#4345A3',
                   '#4543A2', '#4843A1', '#4B429F', '#4E429E', CONCORD_GRAPE,
                   '#54419B', '#574199', '#594098', '#5C4096', '#5E3F95', '#613F94',
                   '#633F92', '#653E91', '#673E8F', '#6A3D8E', '#6C3D8C', '#6D3C8B',
                   '#6F3C8A', '#713C88', '#733B87', '#753B85', '#763A84', '#783A83',
                   '#793981', '#7A3980', '#7C387E', PLUM]
        
        # If we need more colors than we have, repeat the palette
        while len(self.colors) < num_colors:
            self.colors.extend(self.colors)
        
        # Trim to the exact number needed
        self.colors = self.colors[:num_colors]
        
    def get_color(self, n):
        return self.colors[n % len(self.colors)]
