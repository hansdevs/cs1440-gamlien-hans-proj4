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

from tkinter import Tk, Canvas, PhotoImage, mainloop
import time
import sys

class ImagePainter:
    def __init__(self, size=512, bg="#000000"):
        self.size = size
        self.bg = bg
        
    def paint(self, fractal, palette):
        """
        Paint a fractal image using the given fractal and palette.
        
        Args:
            fractal (Fractal): A concrete subclass of Fractal
            palette (Palette): A concrete subclass of Palette
        """
        print(f"Rendering {fractal.name} fractal", file=sys.stderr)

        # Note the time of when we started so we can measure performance improvements
        before = time.time()

        # Set up the GUI so that we can display the fractal image on the screen
        window = Tk()

        # Display the image on the screen
        canvas = Canvas(window, width=self.size, height=self.size, bg=self.bg)
        img = PhotoImage(width=self.size, height=self.size)
        canvas.create_image((self.size/2, self.size/2), image=img, state="normal")
        canvas.pack()

        # Figure out how the boundaries of the PhotoImage relate to coordinates on
        # the imaginary plane.
        minx = fractal.centerX - (fractal.axisLength / 2.0)
        maxx = fractal.centerX + (fractal.axisLength / 2.0)
        miny = fractal.centerY - (fractal.axisLength / 2.0)

        # At this scale, how much length and height on the imaginary plane does one
        # pixel take?
        pixelsize = abs(maxx - minx) / self.size

        for row in range(self.size, 0, -1):
            cc = []
            for col in range(self.size):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                
                # Use the Strategy pattern: call count() without knowing which fractal type it is
                count = fractal.count(complex(x, y))
                
                # Use the Strategy pattern: call get_color() without knowing which palette type it is
                color = palette.get_color(count)
                
                cc.append(color)

            img.put('{' + ' '.join(cc) + '}', to=(0, self.size - row))
            window.update()
            print(self._status_bar(row), end='\r', file=sys.stderr)

        print(f"\nDone in {time.time() - before:.3f} seconds!", file=sys.stderr)

        # Output the Fractal into a .png image
        img.write(f"{fractal.name}.png")
        print(f"Saved image to file {fractal.name}.png", file=sys.stderr)
        print("Close the image window to exit the program", file=sys.stderr)
        mainloop()

    def _status_bar(self, rows):
        """
        Create a status bar showing the progress of rendering.
        
        Args:
            rows (int): Current row being processed
            
        Returns:
            str: Status bar string
        """
        portion = (self.size - rows) / self.size
        status_percent = '{:>4.0%}'.format(portion)
        bar = '=' * int(34 * portion)
        bar = '{:<33}'.format(bar)
        return ''.join(list(['[', status_percent, ' ', bar, ']']))
