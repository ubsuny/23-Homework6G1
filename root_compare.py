import calculus.calculus as calc
import numpy as np

# We will compare the approaches of root_simple and root_secant

# Notice that in the given range, BOTH functions should have roots at
# exactly x = 0, making the test an easy comparison.

# Creates a function that compares the number of steps to find the roots
# given an unlimited max step size and same initial guess for both
# approaches

# Finds the root from a random (reasonable) initial guess
def compare_steps(f_input):

    # Gives a random number between -2, 2
    start = (np.random.rand() - 0.5) * 4

    # Note we need the root_debug = True to get values in our ierations array, which
    # we then take the length of to get the number of steps for root finding
    steps_simple = len(calc.root_simple(f_input, start, 0.5, root_debug=True)[1])

    steps_secant = len(
        calc.root_secant(f_input, start, np.random.rand() * start, root_debug=True)[1]
    )

    return steps_simple, steps_secant


def average_steps(f_input, trials):

    simple_array = []
    secant_array = []

    for i in range(trials):

        simple, secant = compare_steps(f_input)
        simple_array.append(simple)
        secant_array.append(secant)

    avg_simple = np.average(simple_array)
    avg_secant = np.average(secant_array)

    return avg_simple, avg_secant


simp_avg, sec_avg = average_steps(np.tan, 500)
print(
    "For the two algorithms with the same starting guess, the simple root finder takes an average of "
    + str(simp_avg)
    + " steps, while the secant takes "
    + str(sec_avg)
    + " steps."
)
