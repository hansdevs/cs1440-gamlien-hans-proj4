# Fractal Viewer User Manual

## Getting Started

### Launching the Program

The program can be launched from the command line with the following syntax:

\`\`\`
python3 src/main.py [FRACTAL_FILE|default [PALETTE_NAME]]
\`\`\`

Where:
- `FRACTAL_FILE` is an optional path to a fractal configuration file (usually with a .frac extension)
- `default` is a special keyword that generates the default fractal
- `PALETTE_NAME` is an optional name of a color palette to use

Examples:
\`\`\`
python3 src/main.py                           # Uses default fractal and default palette
python3 src/main.py data/mandelbrot.frac      # Uses specified fractal file with default palette
python3 src/main.py data/phoenix.frac Fire    # Uses specified fractal file with Fire palette
python3 src/main.py default Grayscale         # Uses default fractal with Grayscale palette
\`\`\`

### Exiting the Program

To exit the program, simply close the image window that appears after the fractal is rendered.

## Supported Fractal Types

The program supports the following fractal types:

1. **Mandelbrot** - The classic Mandelbrot set fractal
   - Formula: z_{n+1} = z_n^2 + c
   - Required parameters: centerX, centerY, axisLength, iterations

2. **Mandelbrot^3** - Mandelbrot set with z^3 + c iteration formula
   - Formula: z_{n+1} = z_n^3 + c
   - Required parameters: centerX, centerY, axisLength, iterations

3. **Mandelbrot^4** - Mandelbrot set with z^4 + c iteration formula
   - Formula: z_{n+1} = z_n^4 + c
   - Required parameters: centerX, centerY, axisLength, iterations

4. **Phoenix** - Phoenix fractal with complex parameters
   - Formula: z_{n+1} = z_n^2 + c + p*z_{n-1}
   - Required parameters: centerX, centerY, axisLength, iterations, creal, cimag, preal, pimag

5. **Julia** - Julia set fractal with complex parameters
   - Formula: z_{n+1} = z_n^2 + c (where c is fixed)
   - Required parameters: centerX, centerY, axisLength, iterations, creal, cimag

## Available Color Palettes

The following color palettes are available:

1. **Mandelbrot** - Default palette with blues, purples, and greens (used for Mandelbrot fractals)
2. **Phoenix** - Default palette with yellows, greens, and blues (used for Phoenix fractals)
3. **Grayscale** - Black to white gradient
4. **Fire** - Red, orange, and yellow colors resembling flames
5. **Ocean** - Blues and cyans reminiscent of ocean depths
6. **Citrus** - Bright orange, yellow, and green colors

## Fractal Configuration Files

Fractal configuration files (.frac) contain parameters that define the fractal to be rendered. These files use a simple key-value format:

\`\`\`
type: mandelbrot
centerx: -0.7
centery: 0.0
axislength: 2.55
iterations: 96
\`\`\`

Common parameters include:
- `type`: The type of fractal (mandelbrot, mandelbrot3, mandelbrot4, phoenix, julia)
- `centerx`, `centery`: The center point of the view on the complex plane
- `axislength`: The length of the view window on the complex plane
- `iterations`: The maximum number of iterations to perform
- `creal`, `cimag`: Complex constant parameters (required for Julia and Phoenix)
- `preal`, `pimag`: Phoenix parameters (required for Phoenix)

## Examples

### Basic Mandelbrot Set with Different Palettes

\`\`\`
# Mandelbrot with default palette
python3 src/main.py data/mandelbrot.frac

# Mandelbrot with Fire palette
python3 src/main.py data/mandelbrot.frac fire

# Mandelbrot with Ocean palette
python3 src/main.py data/mandelbrot.frac ocean

# Mandelbrot with Grayscale palette
python3 src/main.py data/mandelbrot.frac grayscale

# Mandelbrot with Citrus palette
python3 src/main.py data/mandelbrot.frac citrus
\`\`\`

### Zoomed Mandelbrot with Different Palettes

\`\`\`
# Zoomed Mandelbrot with default palette
python3 src/main.py data/mandelbrot-zoomed.frac

# Zoomed Mandelbrot with Fire palette
python3 src/main.py data/mandelbrot-zoomed.frac fire

# Zoomed Mandelbrot with Ocean palette
python3 src/main.py data/mandelbrot-zoomed.frac ocean
\`\`\`

### Mandelbrot Variations

\`\`\`
# Mandelbrot^3 with default palette
python3 src/main.py data/mandel-pow3.frac

# Mandelbrot^3 with Fire palette
python3 src/main.py data/mandel-pow3.frac fire

# Mandelbrot^4 with Ocean palette
python3 src/main.py data/mandel-pow4.frac ocean

# Mandelbrot^4 with Grayscale palette
python3 src/main.py data/mandel-pow4.frac grayscale
\`\`\`

### Interesting Mandelbrot Locations

\`\`\`
# Seahorse Valley with Fire palette
python3 src/main.py data/m-seahorse.frac fire

# Elephant Valley with Ocean palette
python3 src/main.py data/m-elephants.frac ocean

# Spiral with Citrus palette
python3 src/main.py data/m-spiral0.frac citrus

# Rabbit Hole with Grayscale palette
python3 src/main.py data/m-rabbit-hole.frac grayscale
\`\`\`

### Phoenix Fractal Examples

\`\`\`
# Basic Phoenix with default palette
python3 src/main.py data/phoenix.frac

# Phoenix with Fire palette
python3 src/main.py data/phoenix.frac fire

# Phoenix Feathers with Ocean palette
python3 src/main.py data/p-feathers.frac ocean

# Phoenix Tentacles with Grayscale palette
python3 src/main.py data/p-tentacles.frac grayscale
\`\`\`

### Julia Set Examples

\`\`\`
# Basic Julia with default palette
python3 src/main.py data/julia.frac

# Julia with Fire palette
python3 src/main.py data/julia.frac fire

# Connected Julia with Ocean palette
python3 src/main.py data/j-connected.frac ocean

# Unconnected Julia with Grayscale palette
python3 src/main.py data/j-unconnected.frac grayscale
\`\`\`

### Comparing Iterations

Try rendering the same fractal with different iteration counts to see how it affects detail:

\`\`\`
# Spiral with 256 iterations using Fire palette
python3 src/main.py data/m-spiral1@0256.frac fire

# Spiral with 512 iterations using Fire palette
python3 src/main.py data/m-spiral1@0512.frac fire

# Spiral with 1024 iterations using Fire palette
python3 src/main.py data/m-spiral1@1024.frac fire
\`\`\`

## Saving Images

The program automatically saves the rendered fractal as a PNG image in the current directory. The filename is derived from the fractal name (e.g., "mandelbrot.png", "phoenix.png").

## Creating Custom Fractal Files

You can create your own fractal configuration files to explore different regions of the fractal sets. Here's an example of a custom Mandelbrot fractal file:

\`\`\`
type: mandelbrot
centerx: -0.75
centery: 0.1
axislength: 0.1
iterations: 200
\`\`\`

Save this to a file with a `.frac` extension and run the program with this file as the first argument.

## Program Architecture

The Fractal Viewer is designed using object-oriented principles, specifically the Strategy and Factory Method patterns:

1. **Strategy Pattern**: Used for the fractal algorithms and color palettes
   - Abstract `Fractal` class with concrete implementations (Mandelbrot, Julia, Phoenix, etc.)
   - Abstract `Palette` class with concrete implementations (MandelbrotPalette, PhoenixPalette, etc.)

2. **Factory Method Pattern**: Used to create fractal and palette objects
   - `fractal_factory` creates the appropriate fractal object based on the configuration
   - `palette_factory` creates the appropriate palette object based on the name

3. **Image Rendering**: The `ImagePainter` class handles rendering the fractal to the screen and saving it to a file

## Troubleshooting

### File Not Found
If you see an error like:
\`\`\`
FileNotFoundError: [Errno 2] No such file or directory: 'data/nonexistent.frac'
\`\`\`
Check that the fractal file path is correct and the file exists.

### Unsupported Palette
If you see an error like:
\`\`\`
NotImplementedError: Unsupported palette 'InvalidPalette'
\`\`\`
Use one of the supported palette names listed in this manual.

### Unsupported Fractal Type
If you see an error like:
\`\`\`
NotImplementedError: Unsupported fractal type 'unknown'
\`\`\`
Use one of the supported fractal types listed in this manual.

### Missing Required Parameters
If you see an error like:
\`\`\`
RuntimeError: Missing required parameter 'creal' for Julia fractal
\`\`\`
Make sure your fractal configuration file includes all required parameters for the specified fractal type.

### Slow Rendering
If rendering is slow, try:
- Reducing the number of iterations
- Reducing the pixel size
- Using a smaller axislength to zoom in on a specific area

## Running Tests

To run the unit tests for the program, use:

\`\`\`
python3 run_tests.py
\`\`\`

This will run all the tests and report any failures.

## Extending the Program

The program can be extended with new fractal types and color palettes:

1. To add a new fractal type:
   - Create a new class that extends the `Fractal` class
   - Implement the `count` method with your fractal formula
   - Add the new fractal type to the `fractal_factory` function

2. To add a new color palette:
   - Create a new class that extends the `Palette` class
   - Implement the `get_color` method to return colors
   - Add the new palette to the `palette_factory` function

