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

# Define color palette classes for easy reference
class WHITE: c = '#FFFFFF'
class BLACK: c = '#000000'
class RED: c = '#FF0000'
class GREEN: c = '#00FF00'
class BLUE: c = '#0000FF'
class YELLOW: c = '#FFFF00'
class CYAN: c = '#00FFFF'
class MAGENTA: c = '#FF00FF'
class ORANGE: c = '#FFA500'
class PURPLE: c = '#800080'
class PINK: c = '#FFC0CB'
class LIME: c = '#00FF00'
class TEAL: c = '#008080'
class LAVENDER: c = '#E6E6FA'
class BROWN: c = '#A52A2A'
class MAROON: c = '#800000'
class NAVY: c = '#000080'
class OLIVE: c = '#808000'
class CORAL: c = '#FF7F50'
class CUSTARD: c = '#E1D89F'
class PISTACHIO: c = '#A8D786'
class MINT: c = '#6ECB8A'
class ELDERBERRY: c = '#4771B2'
class CONCORD_GRAPE: c = '#51419C'
class PLUM: c = '#7D387D'

# Original Mandelbrot palette
mandelbrot = [CUSTARD.c, '#E0DA9E', '#E0DC9C', '#DFDE9B', '#DEDF9A', '#DBDE98',
           '#D8DE97', '#D4DD96', '#D1DD94', '#CDDC93', '#CADC92', '#C6DB91',
           '#C3DB8F', '#BFDA8E', '#BCD98D', '#B8D98B', '#B4D88A', '#B0D889',
           '#ACD788', PISTACHIO.c,'#A4D685','#A0D684', '#9CD582', '#98D481',
           '#94D480', '#8FD37F', '#8BD37D', '#87D27C', '#82D17B', '#7ED17A',
           '#79D078', '#77D07A', '#76CF7C', '#75CF7E', '#73CE80', '#72CD83',
           '#71CD85', '#70CC87', MINT.c,    '#6DCB8C', '#6CCA8F', '#6BCA91',
           '#69C994', '#68C896', '#67C899', '#66C79C', '#65C79F', '#63C6A2',
           '#62C5A4', '#61C5A7', '#60C4AA', '#5FC3AD', '#5DC3B0', '#5CC2B3',
           '#5BC1B7', '#5AC1BA', '#59C0BD', '#57BFBF', '#56BABF', '#55B5BE',
           '#54B1BD', '#53ACBD', '#51A7BC', '#50A3BB', '#4F9EBB', '#4E99BA',
           '#4D94B9', '#4C8FB9', '#4A8AB8', '#4985B7', '#4880B7', '#487BB5',
           '#4876B4', ELDERBERRY.c,'#476CB1','#4668AF','#4663AE', '#465EAC',
           '#455AAB', '#4556A9', '#4551A8', '#444DA6', '#4449A5', '#4345A3',
           '#4543A2', '#4843A1', '#4B429F', '#4E429E', CONCORD_GRAPE.c,
           '#54419B', '#574199', '#594098', '#5C4096', '#5E3F95', '#613F94',
           '#633F92', '#653E91', '#673E8F', '#6A3D8E', '#6C3D8C', '#6D3C8B',
           '#6F3C8A', '#713C88', '#733B87', '#753B85', '#763A84', '#783A83',
           '#793981', '#7A3980', '#7C387E', PLUM.c]

# Original Phoenix palette
phoenix = ['#ffe4b5', '#ffe5b2', '#ffe7af', '#ffe8ac', '#ffeaa8', '#ffeca5',
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

# Additional color palettes
citrus = ['#FF4500', '#FF6347', '#FF7F50', '#FF8C00', '#FFA07A', '#FFB347', 
        '#FFC0CB', '#FFD700', '#FFDAB9', '#FFE4B5', '#FFEBCD', '#FFF8DC',
        '#FFFACD', '#FFFAF0', '#FFFFE0', '#FFFFF0', '#F0FFF0', '#E0FFFF',
        '#D8F8E8', '#CCFFCC', '#C0FFC0', '#B3FFB3', '#A6FFA6', '#99FF99',
        '#8CFF8C', '#80FF80', '#73FF73', '#66FF66', '#59FF59', '#4CFF4C',
        '#40FF40', '#33FF33', '#26FF26', '#19FF19', '#0CFF0C', '#00FF00',
        '#00FF0D', '#00FF1A', '#00FF26', '#00FF33', '#00FF40', '#00FF4D',
        '#00FF59', '#00FF66', '#00FF73', '#00FF80', '#00FF8C', '#00FF99',
        '#00FFA6', '#00FFB3', '#00FFC0', '#00FFCC', '#00FFD9', '#00FFE6',
        '#00FFF2', '#00FFFF', '#00F2FF', '#00E6FF', '#00D9FF', '#00CCFF',
        '#00BFFF', '#00B3FF', '#00A6FF', '#0099FF', '#008CFF', '#0080FF',
        '#0073FF', '#0066FF', '#0059FF', '#004CFF', '#0040FF', '#0033FF',
        '#0026FF', '#0019FF', '#000CFF', '#0000FF', '#0D00FF', '#1A00FF',
        '#2600FF', '#3300FF', '#4000FF', '#4D00FF', '#5900FF', '#6600FF',
        '#7300FF', '#8000FF', '#8C00FF', '#9900FF', '#A600FF', '#B300FF',
        '#BF00FF', '#CC00FF', '#D900FF', '#E600FF', '#F200FF', '#FF00FF',
        '#FF00F2', '#FF00E6', '#FF00D9', '#FF00CC', '#FF00BF', '#FF00B3',
        '#FF00A6', '#FF0099', '#FF008C', '#FF0080', '#FF0073', '#FF0066',
        '#FF0059', '#FF004C', '#FF0040', '#FF0033', '#FF0026', '#FF0019',
        '#FF000C', '#FF0000']

ocean = ['#000080', '#000C86', '#00198C', '#002693', '#003399', '#0040A0',
        '#004CA6', '#0059AD', '#0066B3', '#0073BA', '#0080C0', '#008CC7',
        '#0099CD', '#00A6D4', '#00B3DA', '#00BFE1', '#00CCE7', '#00D9EE',
        '#00E6F4', '#00F2FB', '#00FFFF', '#0CFFFF', '#19FFFF', '#26FFFF',
        '#33FFFF', '#40FFFF', '#4DFFFF', '#59FFFF', '#66FFFF', '#73FFFF',
        '#80FFFF', '#8CFFFF', '#99FFFF', '#A6FFFF', '#B3FFFF', '#BFFFFF',
        '#CCFFFF', '#D9FFFF', '#E6FFFF', '#F2FFFF', '#FFFFFF', '#FFF2FF',
        '#FFE6FF', '#FFD9FF', '#FFCCFF', '#FFBFFF', '#FFB3FF', '#FFA6FF',
        '#FF99FF', '#FF8CFF', '#FF80FF', '#FF73FF', '#FF66FF', '#FF59FF',
        '#FF4DFF', '#FF40FF', '#FF33FF', '#FF26FF', '#FF19FF', '#FF0CFF',
        '#FF00FF', '#F200FF', '#E600FF', '#D900FF', '#CC00FF', '#BF00FF',
        '#B300FF', '#A600FF', '#9900FF', '#8C00FF', '#8000FF', '#7300FF',
        '#6600FF', '#5900FF', '#4D00FF', '#4000FF', '#3300FF', '#2600FF',
        '#1900FF', '#0C00FF', '#0000FF', '#0000F2', '#0000E6', '#0000D9',
        '#0000CC', '#0000BF', '#0000B3', '#0000A6', '#000099', '#00008C',
        '#000080']

grayscale = ['#000000', '#080808', '#101010', '#181818', '#202020', '#282828',
          '#303030', '#383838', '#404040', '#484848', '#505050', '#585858',
          '#606060', '#686868', '#707070', '#787878', '#808080', '#888888',
          '#909090', '#989898', '#A0A0A0', '#A8A8A8', '#B0B0B0', '#B8B8B8',
          '#C0C0C0', '#C8C8C8', '#D0D0D0', '#D8D8D8', '#E0E0E0', '#E8E8E8',
          '#F0F0F0', '#F8F8F8', '#FFFFFF', '#F8F8F8', '#F0F0F0', '#E8E8E8',
          '#E0E0E0', '#D8D8D8', '#D0D0D0', '#C8C8C8', '#C0C0C0', '#B8B8B8',
          '#B0B0B0', '#A8A8A8', '#A0A0A0', '#989898', '#909090', '#888888',
          '#808080', '#787878', '#707070', '#686868', '#606060', '#585858',
          '#505050', '#484848', '#404040', '#383838', '#303030', '#282828',
          '#202020', '#181818', '#101010', '#080808', '#000000']

fire = ['#000000', '#180000', '#300000', '#480000', '#600000', '#780000',
      '#900000', '#A80000', '#C00000', '#D80000', '#F00000', '#F01800',
      '#F03000', '#F04800', '#F06000', '#F07800', '#F09000', '#F0A800',
      '#F0C000', '#F0D800', '#F0F000', '#F0F018', '#F0F030', '#F0F048',
      '#F0F060', '#F0F078', '#F0F090', '#F0F0A8', '#F0F0C0', '#F0F0D8',
      '#F0F0F0', '#D8F0F0', '#C0F0F0', '#A8F0F0', '#90F0F0', '#78F0F0',
      '#60F0F0', '#48F0F0', '#30F0F0', '#18F0F0', '#00F0F0', '#00D8F0',
      '#00C0F0', '#00A8F0', '#0090F0', '#0078F0', '#0060F0', '#0048F0',
      '#0030F0', '#0018F0', '#0000F0', '#0000D8', '#0000C0', '#0000A8',
      '#000090', '#000078', '#000060', '#000048', '#000030', '#000018',
      '#000000']

# Dictionary of all available palettes
palette_dict = {
    'mandelbrot': mandelbrot,
    'phoenix': phoenix,
    'citrus': citrus,
    'ocean': ocean,
    'grayscale': grayscale,
    'fire': fire
}

def get_palette(name):
    """
    Get a color palette by name.
    
    Args:
        name (str): Name of the palette to retrieve
        
    Returns:
        list: The requested color palette, or the default palette if not found
    """
    name = name.lower()
    if name in palette_dict:
        return palette_dict[name]
    
    # Return default palette based on first part of name
    if name.startswith('m'):
        return mandelbrot
    elif name.startswith('p'):
        return phoenix
    else:
        return mandelbrot  # Default to mandelbrot palette
