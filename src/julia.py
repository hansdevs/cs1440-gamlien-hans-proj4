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

from fractal import Fractal

class Julia(Fractal):
    def __init__(self, frac):
        required_params = ['centerX', 'centerY', 'axisLength', 'iterations']
        for param in required_params:
            if param not in frac:
                raise RuntimeError(f"Missing required parameter '{param}' for Julia fractal")
            
        self.centerX = frac['centerX']
        self.centerY = frac['centerY']
        self.axisLength = frac['axisLength']
        self.iterations = frac['iterations']
        self.creal = float(frac.get('creal', 0.0))
        self.cimag = float(frac.get('cimag', 0.0))
        self.name = frac.get('name', 'julia')
        
    def count(self, z):
        """
        Julia set iteration count function.
        z_{n+1} = z_n^2 + c
        
        The difference from Mandelbrot is that c is a fixed parameter,
        and z is the point on the complex plane.
        """
        # Julia Constant
        c = complex(self.creal, self.cimag)
        
        for i in range(self.iterations):
            z = z * z + c
            if abs(z) > 2.0:
                return i
        return self.iterations - 1
