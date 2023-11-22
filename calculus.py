import unittest
import calculus

class CalculusTests(unittest.TestCase):

  def test_simpson(self):
    """
    Tests the simpson function with a simple function f(x) = x^2.
    """
    # Test with a simple function
    f = lambda x: x**2

    a = 0
    b = 1
    n = 2

    result = calculus.simpson(f, a, b, n)
    self.assertEqual(result, 1.0 / 3)

  def test_trapezoid(self):
    """
    Tests the trapezoid function with a simple function f(x) = x^2.
    """
    # Test with a simple function
    f = lambda x: x**2

    a = 0
    b = 1
    n = 2

    result = calculus.trapezoid(f, a, b, n)
    self.assertEqual(result, 2.0 / 3)

  def test_adaptive_trapezoid(self):
    """
    Tests the adaptive_trapezoid function with a simple function f(x) = x^2.
    """
    # Test with a simple function
    f = lambda x: x**2

    a = 0
    b = 1
    acc = 1.0e-6

    result = calculus.adaptive_trapezoid(f, a, b, acc)
    self.assertEqual(result, 1.0 / 3)

  def test_root_simple(self):
    """
    Tests the root_simple function with a simple function f(x) = x^2 - 4.
    """
    # Test with a simple function
    f = lambda x: x**2 - 4

    x = 2
    dx = 1
    accuracy = 1.0e-6

    root, iterations = calculus.root_simple(f, x, dx, accuracy)
    self.assertEqual(root, 2.0)
    self.assertEqual(len(iterations), 1)

  def test_root_bisection(self):
    """
    Tests the root_bisection function with a simple function f(x) = x^2 - 4.
    """
    # Test with a simple function
    f = lambda x: x**2 - 4

    x1 = 1
    x2 = 3
    accuracy = 1.0e-6

    root, iterations = calculus.root_bisection(f, x1, x2, accuracy)
    self.assertEqual(root, 2.0)
    self.assertEqual(len(iterations), 3)

  def test_root_secant(self):
    """
    Tests the root_secant function with a simple function f(x) = x^2 - 4.
    """
    # Test with a simple function
    f = lambda x: x**2 - 4

    x0 = 1
    x1 = 3
    accuracy = 1.0e-6

    root, iterations = calculus.root_secant(f, x0, x1, accuracy)
    self.assertEqual(root, 2.0)
    self.assertEqual(len(iterations), 2)

  def test_root_tangent(self):
    """
    Tests the root_tangent function with a simple function f(x) = x^2 - 4.
    """
    # Test with a simple function
    f = lambda x: x**2 - 4
    fp = lambda x: 2*x

    x0 = 1
    accuracy = 1.0e-6

    root, iterations = calculus.root_tangent(f, fp, x0, accuracy)
    self.assertEqual(root, 2.0)
    self.assertEqual(len(iterations), 2)
