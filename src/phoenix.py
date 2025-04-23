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

class Phoenix(Fractal):
    def __init__(self, frac):
        # Check for required parameters
        required_params = ['centerX', 'centerY', 'axisLength', 'iterations', 'creal', 'cimag', 'preal', 'pimag']
        for param in required_params:
            if param not in frac:
                raise RuntimeError(f"Missing required parameter '{param}' for Phoenix fractal")
            
        # Store parameters
        self.centerX = frac['centerX']
        self.centerY = frac['centerY']
        self.axisLength = frac['axisLength']
        self.iterations = frac['iterations']
        self.creal = frac['creal']
        self.cimag = frac['cimag']
        self.preal = frac['preal']
        self.pimag = frac['pimag']
        self.name = frac.get('name', 'phoenix')
        
    def count(self, z):
        """
        Phoenix fractal iteration count function.
        z_{n+1} = z_n^2 + c + p*z_{n-1}
        """
        # Julia Constant
        C = complex(float(self.creal), float(self.cimag))

        # Phoenix Constant
        PHOENIX = complex(float(self.preal), float(self.pimag))

        z_prev = 0+0j

        for i in range(self.iterations):
            z_save = z  # save the current Z value before we overwrite it

            # update Z
            z = z * z + C + (PHOENIX * z_prev)

            # Set the prevZ value for the next iteration
            z_prev = z_save

            # if the absolute value of Z is greater or equal than 2, then return the count
            if abs(z) > 2.0:
                return i

        return self.iterations - 1
