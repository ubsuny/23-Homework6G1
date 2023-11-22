# I am going to explain all the steps especially for task 3.
## Task 3:

### (1) Compare the numpy integration functions to the ones found in compphys
### (2) Add missing docstrings in calculus.py
### (3) Reuse github actions for linting and unit tests for calculus.py
### (4) write unit tests for functions in calculus.py
So, I made a comparison of the intergration functions used in calculus.py with the numpy built in functions. The following is the comarison. 
- Numpy Integration Functions: <br>

trapz(y, x) or quad(f, a, b) for Trapezoidal integration <br>
quad(f, a, b) for Simpson integration

* Calculus.ph <br>
simpson(f, a, b, n) for Simpson's rule <br>
trapezoid(f, a, b, n) for trapezoidal rule <br>
**main differneces** <br>
- Implementation: Numpy integration functions are implemented in C for speed, while provided code functions are implemented in Python for readability and modifiability.<br>
- Input Format: Numpy's trapz function works with arrays, while trapezoid and simpson functions take individual scalar function values.<br>
- Subinterval Division: Numpy can integrate functions defined over unevenly spaced data points, while the provided code functions assume evenly spaced data points.<br>
<img width="534" alt="Screenshot 2023-11-21 at 5 07 58 PM" src="https://github.com/uarif/23-Homework6G1/assets/13534352/f22b439c-4c6b-4674-b68e-38b200557e68">
<br> **Root-finding Algorithms** <br>
Numpy does not provide built-in root-finding algorithms. while the calculus.py, <br>
<br>
```
root_bisection(f, x1, x2, accuracy, max_steps, root_debug) for bisection method 
root_secant(f, x0, x1, accuracy, max_steps, root_debug) for secant method
root_tangent(f, fp, x0, accuracy, max_steps, root_debug) for tangent method
```
<br>
**Key Differences:**<br>
Availability: Numpy does not provide root-finding algorithms, while the provided code has multiple root-finding methods implemented. <br>
Algorithm Types: The provided code offers bisection, secant, and tangent methods, while Numpy does not provide root-finding capabilities.<br>
<img width="594" alt="Screenshot 2023-11-21 at 5 15 34 PM" src="https://github.com/uarif/23-Homework6G1/assets/13534352/2df97c25-e651-4278-b455-6bfd963e4106">
<br>
In a nut shell, Numpy integration functions are optimized for speed and can handle unevenly spaced data points, while the calculus.py functions are easier to understand and modify but require evenly spaced data. For root-finding, the calculus.py offers multiple methods, while Numpy does not provide root-finding capabilities <br>

### (2) Add missing docstrings in calculus.p.
 
Docstrings added for the calculus.py<br>

### (3) Reuse github actions for linting and unit tests for calculus.py
I am working on this part, I added but its not properly working, I corrected many things linting suggested but still there are some errors I need to fix. I am working on them and hope to correct them before the deadline. 

### (4) Unit test for calculus.py 
Unit test is done for calculus.py <br>




