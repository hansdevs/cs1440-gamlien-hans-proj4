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

from mandelbrot import Mandelbrot, MandelbrotPow3, MandelbrotPow4
from phoenix import Phoenix
from julia import Julia
from parser import parse

def fractal_factory(fname=None):
    """
    Create a fractal object based on the given file name.
    
    Args:
        fname (str, optional): Path to a fractal configuration file. If None or 'default',
                              a default Mandelbrot fractal is created.
    
    Returns:
        Fractal: A concrete subclass of Fractal
        
    Raises:
        NotImplementedError: If the fractal type is not supported
        FileNotFoundError: If the file cannot be opened
        RuntimeError: If the file has syntax errors or missing required parameters
    """
    if fname is None or fname == 'default':
        print("fractal_factory: creating default fractal")
        # Create a default Mandelbrot fractal
        default_config = {
            'name': 'default',
            'type': 'mandelbrot',
            'centerX': -0.7,
            'centerY': 0.0,
            'axisLength': 2.55,
            'iterations': 256
        }
        return Mandelbrot(default_config)
    
    # Parse the fractal configuration file
    frac = parse(fname)
    
    # Convert string values to appropriate types
    if 'type' in frac:
        frac_type = frac['type'].lower()
    else:
        # Default to mandelbrot if type is not specified
        frac_type = 'mandelbrot'
    
    # Convert numeric values to appropriate types and map lowercase keys to camelCase
    for key, camel_key in [('centerx', 'centerX'), ('centery', 'centerY'), ('axislength', 'axisLength'), 
                          ('creal', 'creal'), ('cimag', 'cimag'), ('preal', 'preal'), ('pimag', 'pimag')]:
        if key in frac:
            try:
                frac[camel_key] = float(frac[key])
            except ValueError:
                raise ValueError(f"Bad float value in {fname}: '{frac[key]}'")
    
    if 'iterations' in frac:
        try:
            frac['iterations'] = int(frac['iterations'])
        except ValueError:
            raise ValueError(f"Bad integer value in {fname}: '{frac['iterations']}'")
    
    # Create the appropriate fractal object
    if frac_type == 'mandelbrot':
        return Mandelbrot(frac)
    elif frac_type == 'mandelbrot3':
        return MandelbrotPow3(frac)
    elif frac_type == 'mandelbrot4':
        return MandelbrotPow4(frac)
    elif frac_type == 'phoenix':
        return Phoenix(frac)
    elif frac_type == 'julia':
        return Julia(frac)
    else:
        raise NotImplementedError(f"Unsupported fractal type '{frac_type}'")
