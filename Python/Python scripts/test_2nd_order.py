#! /usr/local/bin/python3.4
# test_2nd_order.py


import unittest
import inspect                      # For checking correct types of variables
import numpy as np                  # For constants and trig functions
import matplotlib.pyplot as plt     # For plotting

# Import the homeowrk solutions
import pedroIrazoqui_2nd_order_ODE as soln     # import instructor solutions
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


# We'll test the hw.euler() and hw.rk() methods using a number of test cases.
# For each of the following examples, calculate the output two different ways
# and comparing the results for both  hw and soln to the analytical solution.
# y is the unknown or dependent variable
# y' is dy/dx
# y'' or d^2y/dx^2 is what we are given: the 2nd order ODE we wish to solve
start = 0                               # Start of range
stop = 20                               # Stop of range
N = 100                                 # Number of steps
h = (stop - start)/(N-1)                # Step size
# Instantiate the independent variable
x_hw = [i for i in hw.irange(start, stop, h)]
x_soln = [i for i in soln.irange(start, stop, h)]


# First test ODE
# 2nd order ODE to solve: y'' - 2y' + 2y = e^(2t) * sin(t)
def ode1_u1(t, u1, u2):
    """This function implements the ODE we're trying to solve
    In this case u1 = y(t)
    In this case u2 = dy/dt
    Therefore our 1st order ODE is:
    u1' = u2
    """
    u1_prime = u2                           # The equation given above
    return u1_prime


def ode1_u2(t, u1, u2):
    """This function implements the ODE we're trying to solve
    In this case u1 = y(t)
    In this case u2 = dy/dt
    Our ODE: y'' - 2*y' + 2*y = e^(2*t) * sin(t)
    becomes: u2' - 2*u2 + 2*u1 = e^(2*t) * sin(t)
    Therefore our 1st order ODE is:
    u2' = 2*u2 - 2*u1 + e^(2*t) * sin(t)
    """
    u2_prime = (2*u2) - (2*u1) + ((np.e**(2*t)) * np.sin(t))    # The equation given above
    return u2_prime


# Second test ODE
# 2nd order ODE to solve: y'' = -sin(x)+2
def ode2_u1(x, u1, u2):
    """This function implements the ODE we're trying to solve
    In this case u1 = y(t)
    In this case u2 = dy/dt
    Therefore our 1st order ODE is:
        u1' = u2
        """
    u1_prime = u2                           # The equation given above
    return u1_prime


def ode2_u2(x, u1, u2):
    """This function implements the ODE we're trying to solve
    In this case u1 = y(t)
    In this case u2 = dy/dt
    Our ODE: y'' = -sin(x) + 2
    becomes: u2' = -sin(x) + 2
    Therefore our 1st order ODE is:
    u2' = -sin(x) + 2
    """
    u2_prime = -np.sin(x)                   # The equation given above
    return u2_prime


'------------------------------Begin TestEuler-------------------------------------'


# Define all the tests for hw.euler method
class TestEuler(unittest.TestCase):
    # Numerical approximation using Euler method
    y_initial = -0.4                        # Initial value (given)
    y_prime_initial = -0.6                  # Initial value (given)
    test1, test1p = hw.euler(ode1_u1, ode1_u2, x_hw, h, y_initial, y_prime_initial)
    answer1, answer1p = soln.euler(ode1_u1, ode1_u2, x_soln, h, y_initial, y_prime_initial)

    # Check values are correct
    def testeuler1(self):
        self.assertAlmostEqual(self.test1, self.answer1)

    def testeuler2(self):
        self.assertAlmostEqual(self.test1p, self.answer1p)

    # Numerical approximation using Euler method
    y_initial = np.sin(start)              # Initial value
    y_prime_initial = np.cos(start)        # Initial value
    # Exact solution to compare to our numerically obtained solution
    y_analitical2 = [np.sin(step) for step in x_soln]
    y_analitical2p = [np.cos(step) for step in x_soln]
    # Numerical approximation using Euler method
    test2, test2p = hw.euler(ode2_u1, ode2_u2, x_hw, h, y_initial, y_prime_initial)
    answer2, answer2p = soln.euler(ode2_u1, ode2_u2, x_soln, h, y_initial, y_prime_initial)

    # Check values are correct
    def testeuler3(self):
        self.assertAlmostEqual(self.test2, self.answer2)

    def testeuler4(self):
        self.assertAlmostEqual(self.test2p, self.answer2p)

    # Plot and compare hw & soln
    figure1 = plt.figure()
    figure1.suptitle('Numerical Approximations of y Using the Euler Method',
                     fontsize=14, fontweight='bold')
    subplot = figure1.add_subplot(221)      # 2 x 2 subplots in plot; this is subplot1
    subplot.set_xlabel('x')
    subplot.set_ylabel('y')
    subplot.set_title("y'' - 2y' + 2y = e^(2t) * sin(t)")
    subplot.plot(x_soln, test1, 'r.', x_soln, answer1, 'bx')
    subplot = figure1.add_subplot(222)      # 2 x 2 subplots in plot; this is subplot2
    subplot.set_xlabel('x')
    subplot.set_ylabel("y' = dy/dx")
    subplot.set_title('y prime')
    subplot.plot(x_soln, test1p, 'r.', x_soln, answer1p, 'bx')
    subplot = figure1.add_subplot(223)      # 2 x 2 subplots in plot; this is subplot3
    subplot.set_xlabel('x')
    subplot.set_ylabel('y')
    subplot.set_title("y'' = -sin(x) + 2")
    subplot.plot(x_soln, test2, 'r.', x_soln, answer2, 'bx', x_soln, y_analitical2, 'k')
    subplot = figure1.add_subplot(224)      # 2 x 2 subplots in plot; this is subplot4
    subplot.set_xlabel('x')
    subplot.set_ylabel("y' = dy/dx")
    subplot.set_title('y prime')
    subplot.plot(x_soln, test2p, 'r.', x_soln, answer2p, 'bx', x_soln, y_analitical2p, 'k')
    plt.show()
'------------------------------End TestEuler---------------------------------------'


'------------------------------Begin TestRK----------------------------------------'


# Define all the tests for hw.euler method
class TestRK(unittest.TestCase):
    # Numerical approximation using RK method
    y_initial = -0.4                        # Initial value (given)
    y_prime_initial = -0.6                  # Initial value (given)
    test1, test1p = hw.rk(ode1_u1, ode1_u2, x_hw, h, y_initial, y_prime_initial)
    answer1, answer1p = soln.rk(ode1_u1, ode1_u2, x_soln, h, y_initial, y_prime_initial)

    # Check values are correct
    def testrk1(self):
        self.assertAlmostEqual(self.test1, self.answer1)

    def testrk2(self):
        self.assertAlmostEqual(self.test1p, self.answer1p)

    # Numerical approximation using rk method
    y_initial = np.sin(start)              # Initial value
    y_prime_initial = np.cos(start)        # Initial value
    # Exact solution to compare to our numerically obtained solution
    y_analitical2 = [np.sin(step) for step in x_soln]
    y_analitical2p = [np.cos(step) for step in x_soln]
    # Numerical approximation using Euler method
    test2, test2p = hw.rk(ode2_u1, ode2_u2, x_hw, h, y_initial, y_prime_initial)
    answer2, answer2p = soln.rk(ode2_u1, ode2_u2, x_soln, h, y_initial, y_prime_initial)

    # Check values are correct
    def testrk3(self):
        self.assertAlmostEqual(self.test2, self.answer2)

    def testrk4(self):
        self.assertAlmostEqual(self.test2p, self.answer2p)

    # Plot and compare hw & soln
    figure2 = plt.figure()
    figure2.suptitle('Numerical Approximations of y Using the Runge-Kutta Method',
                     fontsize=14, fontweight='bold')
    subplot = figure2.add_subplot(221)      # 2 x 2 subplots in plot; this is subplot1
    subplot.set_xlabel('x')
    subplot.set_ylabel('y')
    subplot.set_title("y'' - 2y' + 2y = e^(2t) * sin(t)")
    subplot.plot(x_soln, test1, 'r.', x_soln, answer1, 'bx')
    subplot = figure2.add_subplot(222)      # 2 x 2 subplots in plot; this is subplot2
    subplot.set_xlabel('x')
    subplot.set_ylabel("y' = dy/dx")
    subplot.set_title('y prime')
    subplot.plot(x_soln, test1p, 'r.', x_soln, answer1p, 'bx')
    subplot = figure2.add_subplot(223)      # 2 x 2 subplots in plot; this is subplot3
    subplot.set_xlabel('x')
    subplot.set_ylabel('y')
    subplot.set_title("y'' = -sin(x) + 2")
    subplot.plot(x_soln, test2, 'r.', x_soln, answer2, 'bx', x_soln, y_analitical2, 'k')
    subplot = figure2.add_subplot(224)      # 2 x 2 subplots in plot; this is subplot4
    subplot.set_xlabel('x')
    subplot.set_ylabel("y' = dy/dx")
    subplot.set_title('y prime')
    subplot.plot(x_soln, test2p, 'r.', x_soln, answer2p, 'bx', x_soln, y_analitical2p, 'k')
    plt.show()
    # Plot and compare hw & soln
'------------------------------End TestRK------------------------------------------'


# Now run all the tests:
if __name__ == '__main__':
    unittest.main()
