import unittest
import calculus as calc


class CalculusTests(unittest.TestCase):

    """
    Test suite for the Calculus module
    """

    def test_simpson(self):
        """
        Tests the Simpson's rule approximation
        """
        # Test with a simple function
        f = lambda x: x**2

        a = 0
        b = 1
        n = 2

        result = calc.simpson(f, a, b, n)
        self.assertEqual(result, 1.0 / 3)

    def test_trapezoid(self):
        """
        Tests the trapezoidal rule approximation
        """
        # Test with a simple function
        f = lambda x: x**2

        a = 0
        b = 1
        n = 2

        result = calc.trapezoid(f, a, b, n)
        self.assertEqual(result, 2.0 / 3)

    def test_adaptive_trapezoid(self):
        """
        Tests the adaptive trapezoidal rule approximation
        """
        # Test with a simple function
        f = lambda x: x**2

        a = 0
        b = 1
        acc = 1.0e-6

        result = calc.adaptive_trapezoid(f, a, b, acc)
        self.assertEqual(result, 1.0 / 3)

    def test_root_simple(self):
        """
        Tests the root_simple method
        """
        # Test with a simple function
        f = lambda x: x**2 - 4

        x = 2
        dx = 1
        accuracy = 1.0e-6

        root, iterations = calc.root_simple(f, x, dx, accuracy)
        self.assertEqual(root, 2.0)
        self.assertEqual(len(iterations), 1)

    def test_root_bisection(self):
        """
        Tests the root_bisection method
        """
        # Test with a simple function
        f = lambda x: x**2 - 4

        x1 = 1
        x2 = 3
        accuracy = 1.0e-6

        root, iterations = calc.root_bisection(f, x1, x2, accuracy)
        self.assertEqual(root, 2.0)
        self.assertEqual(len(iterations), 3)

    def test_root_secant(self):
        """
        Tests the root_secant method
        """
        # Test with a simple function
        f = lambda x: x**2 - 4

        x0 = 1
        x1 = 3
        accuracy = 1.0e-6

        root, iterations = calc.root_secant(f, x0, x1, accuracy)
        self.assertEqual(root, 2.0)
        self.assertEqual(len(iterations), 2)

    def test_root_tangent(self):
        """
        Tests the root_tangent method
        """
        # Test with a simple function
        f = lambda x: x**2 - 4
        fp = lambda x: 2*x

        x0 = 1
        accuracy = 1.0e-6

        root, iterations = calc.root_tangent(f, fp, x0, accuracy)
        self.assertEqual(root, 2.0)
        self.assertEqual(len(iterations), 2)


def f_prime(x):
    """
    Calculates the derivative of f(x) = x**2
    """
    return 2*x
