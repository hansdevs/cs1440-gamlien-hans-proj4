# CS 1440 Project 4.1: Object-Oriented Design - Code Smells Report

This report identifies potential code smells and areas for improvement in the current object-oriented implementation.

1. **Potential Duplication in Fractal Classes** at `mandelbrot.py` [in the Mandelbrot, MandelbrotPow3, and MandelbrotPow4 classes]  
   * **Description of smell**: The three Mandelbrot classes share similar initialization code and parameter validation, which could lead to maintenance issues if one class is updated but others are not.
   * **Offending Code**:
   ```python
   class Mandelbrot(Fractal):
       def __init__(self, frac):
           # Check for required parameters
           required_params = ['centerX', 'centerY', 'axisLength', 'iterations']
           for param in required_params:
               if param not in frac:
                   raise RuntimeError(f"Missing required parameter '{param}' for Mandelbrot fractal")
           # ...
   
   class MandelbrotPow3(Fractal):
       def __init__(self, frac):
           # Check for required parameters
           required_params = ['centerX', 'centerY', 'axisLength', 'iterations']
           for param in required_params:
               if param not in frac:
                   raise RuntimeError(f"Missing required parameter '{param}' for Mandelbrot^3 fractal")
           # ...
   \`\`\`
   * **How to resolve**: Create a base Mandelbrot class that handles common initialization and parameter validation, then have the specialized classes inherit from it. This would reduce duplication and make maintenance easier.

---

2. **Potential Feature Envy** at `fractalfactory.py` [in the fractal_factory function]  
   * **Description of smell**: The factory function has detailed knowledge of how to convert and validate parameters for each fractal type, which could be considered the responsibility of the fractal classes themselves.
   * **Offending Code**:
   ```python
   def fractal_factory(fname=None):
       # ...
       # Convert numeric values to appropriate types and map lowercase keys to camelCase
       for key, camel_key in [('centerx', 'centerX'), ('centery', 'centerY'), ('axislength', 'axisLength'), 
                             ('creal', 'creal'), ('cimag', 'cimag'), ('preal', 'preal'), ('pimag', 'pimag')]:
           if key in frac:
               try:
                   frac[camel_key] = float(frac[key])
               except ValueError:
                   raise ValueError(f"Bad float value in {fname}: '{frac[key]}'")
       # ...
   \`\`\`
   * **How to resolve**: Consider moving the parameter conversion and validation logic into the fractal classes themselves, allowing each class to handle its own specific requirements. The factory would then simply create the appropriate object without needing to know the details of parameter processing.

---

3. **Primitive Obsession** at `parser.py` [in the parse function]  
   * **Description of smell**: The function returns a dictionary of primitive values rather than a more structured object, which could lead to inconsistent access patterns and type issues.
   * **Offending Code**:
   ```python
   def parse(fname):
       frac = {
           'fname': fname,
           'name': Path(fname).stem,
       }
       # ...
       return frac
   \`\`\`
   * **How to resolve**: Consider creating a FractalConfiguration class that encapsulates the parsed data and provides methods for accessing and validating the configuration. This would provide a more structured approach and could include type conversion methods.

---

4. **Potential Long Method** at `image.py` [in the paint method of ImagePainter]  
   * **Description of smell**: The paint method handles multiple responsibilities: setting up the GUI, calculating coordinates, rendering pixels, updating the display, and saving the image.
   * **Offending Code**:
   ```python
   def paint(self, fractal, palette):
       # ... (many lines of code handling different responsibilities)
   \`\`\`
   * **How to resolve**: Break down the paint method into smaller, more focused methods, each handling a specific responsibility. For example, separate methods for GUI setup, coordinate calculation, pixel rendering, and image saving.

---

5. **Potential Lack of Encapsulation** at `fractal.py` and `palette.py` [in the abstract base classes]  
   * **Description of smell**: The attributes of the Fractal and Palette classes are directly accessed by client code rather than through accessor methods, which could make future changes to the internal representation more difficult.
   * **Offending Code**:
   ```python
   # Client code directly accessing attributes
   minx = fractal.centerX - (fractal.axisLength / 2.0)
   maxx = fractal.centerX + (fractal.axisLength / 2.0)
   \`\`\`
   * **How to resolve**: Consider adding accessor methods or properties to provide controlled access to the internal state of the objects. This would allow for validation, lazy loading, or other behaviors to be added without changing the client code.

---

These code smells represent opportunities for further refinement in the object-oriented design, but they don't necessarily indicate serious problems with the current implementation. The current design successfully applies the Strategy and Factory Method patterns and provides a clean separation of concerns.