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

class Mandelbrot(Fractal):
    def __init__(self, frac):
        # Check for required parameters
        required_params = ['centerX', 'centerY', 'axisLength', 'iterations']
        for param in required_params:
            if param not in frac:
                raise RuntimeError(f"Missing required parameter '{param}' for Mandelbrot fractal")
            
        # Store parameters
        self.centerX = frac['centerX']
        self.centerY = frac['centerY']
        self.axisLength = frac['axisLength']
        self.iterations = frac['iterations']
        self.name = frac.get('name', 'mandelbrot')
        
    def count(self, z):
        """
        Mandelbrot set iteration count function.
        z_{n+1} = z_n^2 + c
        """
        c = z  # In Mandelbrot, c is the point on the complex plane
        z = complex(0, 0)  # z0
        
        for i in range(self.iterations):
            z = z * z + c
            if abs(z) > 2.0:
                return i
        return self.iterations - 1

class MandelbrotPow3(Fractal):
    def __init__(self, frac):
        # Check for required parameters
        required_params = ['centerX', 'centerY', 'axisLength', 'iterations']
        for param in required_params:
            if param not in frac:
                raise RuntimeError(f"Missing required parameter '{param}' for Mandelbrot^3 fractal")
            
        # Store parameters
        self.centerX = frac['centerX']
        self.centerY = frac['centerY']
        self.axisLength = frac['axisLength']
        self.iterations = frac['iterations']
        self.name = frac.get('name', 'mandelbrot3')
        
    def count(self, z):
        """
        Mandelbrot^3 set iteration count function.
        z_{n+1} = z_n^3 + c
        """
        c = z  # In Mandelbrot, c is the point on the complex plane
        z = complex(0, 0)  # z0
        
        for i in range(self.iterations):
            z = z**3 + c  # Cube instead of square
            if abs(z) > 2.0:
                return i
        return self.iterations - 1

class MandelbrotPow4(Fractal):
    def __init__(self, frac):
        # Check for required parameters
        required_params = ['centerX', 'centerY', 'axisLength', 'iterations']
        for param in required_params:
            if param not in frac:
                raise RuntimeError(f"Missing required parameter '{param}' for Mandelbrot^4 fractal")
            
        # Store parameters
        self.centerX = frac['centerX']
        self.centerY = frac['centerY']
        self.axisLength = frac['axisLength']
        self.iterations = frac['iterations']
        self.name = frac.get('name', 'mandelbrot4')
        
    def count(self, z):
        """
        Mandelbrot^4 set iteration count function.
        z_{n+1} = z_n^4 + c
        """
        c = z  # In Mandelbrot, c is the point on the complex plane
        z = complex(0, 0)  # z0
        
        for i in range(self.iterations):
            z = z**4 + c  # Fourth power instead of square
            if abs(z) > 2.0:
                return i
        return self.iterations - 1
