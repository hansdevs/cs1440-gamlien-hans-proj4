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

from pathlib import Path

def parse(fname, default_type=None):
    """
    Parse a fractal configuration file into a dictionary.
    
    Args:
        fname (str): Path to the fractal configuration file
        default_type (str, optional): Default fractal type if not specified in file
        
    Returns:
        dict: Dictionary containing the fractal configuration
        
    Raises:
        RuntimeError: If the file has syntax errors
        FileNotFoundError: If the file cannot be opened
    """
    props = {}
    with open(fname) as f:
        for lineno, line in enumerate(f, start=1):
            raw = line.strip()
            if not raw or raw.startswith('#'):
                continue

            if ':' not in raw or raw.count(':') != 1:
                raise RuntimeError(f"Parse error at line {lineno} of {fname}: wrong number of tokens\n{line.rstrip()}")

            key_part, val_part = raw.split(':', 1)
            key = key_part.strip().lower()
            value_str = val_part.strip()

            if not key or not value_str:
                raise RuntimeError(f"Parse error at line {lineno} of {fname}: missing key or value\n{line.rstrip()}")

            if key in ('centerx', 'centery', 'axislength'):
                try:
                    value = float(value_str)
                except ValueError:
                    value = value_str
            elif key in ('pixels', 'iterations'):
                try:
                    value = int(value_str)
                except ValueError:
                    value = value_str
            else:
                value = value_str

            props[key] = value

    result = {}

    fractal_type = props.get('type', default_type)
    if fractal_type is not None:
        result['type'] = fractal_type

    if 'centerx' in props:
        result['centerX'] = props['centerx']
    if 'centery' in props:
        result['centerY'] = props['centery']
    if 'axislength' in props:
        result['axisLength'] = props['axislength']
    if 'pixels' in props:
        result['pixels'] = props['pixels']
    if 'iterations' in props:
        result['iterations'] = props['iterations']

    result['name'] = Path(fname).stem
    return result