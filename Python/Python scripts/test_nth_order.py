#! /usr/local/bin/python3.4
# test_nth_order.py


import unittest
import inspect                      # For checking correct types of variables
import numpy as np                  # For constants and trig functions
import matplotlib.pyplot as plt     # For plotting

# Import the homeowrk solutions
import soln_nth_order_ODE as soln     # import instructor solutions
# Import the file specified at the user prompt
submission = input('Please enter the homework file name you wish to test.\n>>')
# Strip the '.py' if it exists
if submission[-3:] == '.py':
    submission = submission[0:(len(submission)-3)]
# Import the homework submission
hw = __import__(submission)


'------------------------------Begin TestIrange------------------------------------'


# Define all the tests for the hw.irange method
class TestIrange(unittest.TestCase):
    # Check return value type
    def testgenerator(self):
        test = list(hw.irange(0, 10, 1))                # Creat generator using hw.irange()
        self.assertFalse(inspect.isgenerator(test))     # Check that a generator object is returned

    # Check integer generator
    def testintgenerator(self):
        test = list(hw.irange(72, 90, 3))               # Creat generator using hw.irange()
        answer = list(soln.irange(72, 90, 3))           # Creat generator using soln.irange()
        self.assertEqual(test, answer)                  # Check that both generators are the same

    # Check float generator
    def testfloatgenerator(self):
        test = list(hw.irange(-.5, .5, .1))             # Creat generator using hw.irange()
        answer = list(soln.irange(-.5, .5, .1))         # Creat generator using soln.irange()
        self.assertAlmostEqual(test, answer)
'------------------------------End TestIrange--------------------------------------'


# We'll test the hw.rk() method using a number of test cases.
# For each of the following examples, calculate the output two different ways
# and comparing the results for both  hw and soln to the analytical solution.
# y is the unknown or dependent variable
# y' is dy/dx
start = 0                               # Start of range
stop = 20                               # Stop of range
N = 100                                 # Number of steps
h = (stop - start)/(N-1)                # Step size
# Instantiate the independent variable
x_hw = [i for i in hw.irange(start, stop, h)]
x_soln = [i for i in soln.irange(start, stop, h)]


# First test ODE
# 2nd order ODE to solve: y = sin(x)
def ode1_u1(x, u):
    """This function implements the ODE we're trying to solve
    In this case u1 = y(t)
    In this case u2 = dy/dt
    Therefore our 1st order ODE is:
    u1' = u2
    """
    u1_prime = u[1]                             # The equation given above
    return u1_prime


# 2nd order ODE to solve: y = sin(x)
def ode1_u2(x, u):
    """This function implements the ODE we're trying to solve
    In this case u1 = y(t)
    In this case u2 = dy/dt
    Our ODE: y'' = -sin(x) + 2
    becomes: u2' = -sin(x) + 2
    Therefore our 1st order ODE is:
    u2' = -sin(x)
    """
    u2_prime = -np.sin(x)                       # The equation given above
    return u2_prime


'------------------------------Begin TestRK----------------------------------------'


# Define all the tests for hw.euler method
class TestRK(unittest.TestCase):
    # Numerical approximation using rk method
    y_initial = np.sin(start)              # Initial value
    y_prime_initial = np.cos(start)        # Initial value
    # Exact solution to compare to our numerically obtained solution
    y_analitical = [np.sin(step) for step in x_soln]
    # Numerical approximation using Euler method
    y_and_primes_hw = hw.rk([ode1_u1, ode1_u2], x_hw, h, [y_initial, y_prime_initial])
    y_and_primes_soln = soln.rk([ode1_u1, ode1_u2], x_soln, h, [y_initial, y_prime_initial])
    # Extract y = f(x)
    test = [row[0] for row in y_and_primes_hw]
    answer = [row[0] for row in y_and_primes_soln]

    # Check values are correct
    def testrk(self):
        self.assertAlmostEqual(self.test, self.answer)

    # Plot and compare hw & soln
    figure2 = plt.figure()
    figure2.suptitle("Numerical Approximations of y for y'' = -sin(x)",
                     fontsize=14, fontweight='bold')
    subplot = figure2.add_subplot(111)      # 1 x 1 subplots in plot; this is subplot1
    subplot.set_xlabel('x')
    subplot.set_ylabel('y = f(x)')
    subplot.set_title('y = f(x) = sin(x)')
    subplot.plot(x_soln, test, 'r.', x_soln, answer, 'bx')
    plt.show()
    # Plot and compare hw & soln
'------------------------------End TestRK------------------------------------------'


# Now run all the tests:
if __name__ == '__main__':
    unittest.main()
