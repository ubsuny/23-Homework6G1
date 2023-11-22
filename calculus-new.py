import math

def simpson(f, a, b, n):
    """
    Simpson's rule numerical integration
    """
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)
    return result * h / 6

def trapezoid(f, a, b, n):
    """
    Trapezoidal rule numerical integration
    """
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + i * h)
    return result * h / 2

def adaptive_trapezoid(f, a, b, acc):
    """
    Adaptive trapezoidal rule approximation
    """
    if abs(b - a) < 1e-16:
        return f((a + b) / 2)
    else:
        mid = (a + b) / 2
        left = adaptive_trapezoid(f, a, mid, acc)
        right = adaptive_trapezoid(f, mid, b, acc)
        result = (left + right) / 2
        if is_within_acceptable_error(mid, left, right, acc):
            return result
        else:
            return result + adaptive_trapezoid(f, a, mid, acc / 2) + adaptive_trapezoid(f, mid, b, acc / 2)

def root_bisection(f, x1, x2, acc):
    """
    Root bisection algorithm
    """
    iterations = []
    while abs(x2 - x1) > acc:
        mid = (x1 + x2) / 2
        if f(x1) * f(mid) < 0:
            x2 = mid
        else:
            x1 = mid
        iterations.append((x1, x2))
    return (x1 + x2) / 2, iterations

def root_secant(f, x0, x1, acc):
    """
    Root-finding secant method
    """
    iterations = []
    while abs(f(x1)) > acc:
        iterations.append((x0, x1))
        fx0 = f(x0)
        fx1 = f(x1)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0 = x1
        x1 = x2
    return x1, iterations

def root_simple(f, x, dx, acc):
    """
    Root-finding method based on simple iteration
    """
    iterations = []
    while abs(f(x)) > acc:
        iterations.append(x)
        x = x - f(x) / dx
    return x, iterations

def root_tangent(f, fp, x0, acc):
    """
    Root-finding tangent method
    """
    iterations = []
    while abs(f(x0)) > acc:
        iterations.append(x0)
        x1 = x0 - f(x0) / fp(x0)
        x0 = x1
    return x1, iterations

def is_within_acceptable_error(x, left, right, acc):
    return abs(left - right) < acc or math.isnan(left) or math.isnan(right)
