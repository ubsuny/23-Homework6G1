# I am going to explain all the steps especially for task 3.
## Task 3:

### (1) Compare the numpy integration functions to the ones found in compphys
### (2) Add missing docstrings in calculus.py
### (3) Reuse github actions for linting and unit tests for calculus.py
### (4) write unit tests for functions in calculus.py
So, I made a comparison of the intergration functions used in calculus.py with the numpy built in functions. The following is the comarison. 
- Numpy Integration Functions:

trapz(y, x) or quad(f, a, b) for Trapezoidal integration $\n$
quad(f, a, b) for Simpson integration

* Calculus.ph
simpson(f, a, b, n) for Simpson's rule $\n$
trapezoid(f, a, b, n) for trapezoidal rule
