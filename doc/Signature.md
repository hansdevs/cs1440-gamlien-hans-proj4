## Sprint Signature 4.0

---
## Sprint Signature 4.0

| **Date**   | **Time Spent** | **Events**                                                                                                                                                                      |
|------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| April 4    | 3.5 hours      | Analyzed the messy original code, verifying it rendered fractal images (Mandelbrot & Phoenix) as expected. Began identifying code smells (global variables, magic numbers, odd imports). Created plan notes for how to reorganize and clarify. |
| April 5    | 2.75 hours     | Started cleaning up `mbrot_fractal.py` by removing unnecessary globals and clarifying functions (no new features, just reorganizing code). Took notes of leftover debugging imports and replaced magic constants with named variables. Tested after each small change to ensure no functionality broke. |
| April 6    | 2.75 hours     | Continued refactoring in `phoenix_fractal.py`, focusing on poor naming and dead code. Verified that all fractal images still matched their “before” versions. Wrote minimal documentation clarifying usage, but did not alter the program’s behavior.                                                                                                                                 |
| **TOTAL**  | **9 hours**    | Completed a thorough **refactoring** pass of the original fractal code without adding new functionality. Preserved existing behavior and user interface while improving readability, reducing code smells, and ensuring stable fractal outputs. |

---


## Sprint Signature 4.1

| Date        | Time Spent | Events
|-------------|------------|--------------------
| April 22    | 0.75 hours | Analyzed requirements and designed class hierarchy for Fractal and Palette abstract classes
| April 22    | 1 hour     | Implemented abstract classes and factory methods for both Fractal and Palette hierarchies
| April 22    | 1.25 hours | Created concrete Fractal classes (Mandelbrot, Julia, Phoenix) and their algorithms
| April 22    | 0.75 hours | Implemented color palette classes and unified parser for all fractal types
| April 22    | 0.75 hours | Wrote unit tests and fixed bugs in implementation
| April 22    | 0.5 hours  | Updated documentation and created code smells report
| TOTAL       | 5 hours    | Completed object-oriented refactoring using Strategy and Factory patterns with extensible design