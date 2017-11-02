#! /usr/local/bin/python3.4
# test_1st_order.py


import numpy as np                  # For constants and trig functions
import matplotlib.pyplot as plt     # For plotting

# Import the homeowrk solutions
import mickeySmith_1st_order_ODE as soln     # import instructor solutions
# Import the file specified at the user prompt
submission = input('Please enter the homework file name you wish to test.\n>>')
# Strip the '.py' if it exists
if submission[-3:] == '.py':
    submission = submission[0:(len(submission)-3)]
# Import the homework submission
hw = __import__(submission)


# We'll test the hw.euler() and hw.rk() methods using a number of test cases.
# For each of the following examples, calculate the output two different ways
# and comparing the results for both  hw and soln to the analytical solution.
# y is the unknown or dependent variable
# y' or dy/dx is what we are given: the ODE we wish to solve
start = -np.pi                          # Start of range
stop = np.pi                            # Stop of range
N = 100                                 # Number of steps
h = (stop - start)/(N-1)                # Step size
# Instantiate the independent variable
x_hw = [i for i in hw.irange(start, stop, h)]
x_soln = [i for i in soln.irange(start, stop, h)]


# First test ODE
# dy/dx = 2*x
def f_x(x):
    """This function implements the ODE we're trying to solve
    In this case y' = dy/dx = 2x
    This corresponds to y = x^2
    """
    f_x = 2 * x                         # The equation given above
    return f_x
# Exact solution to compare to our numerically obtained solution
y_analitical1 = [(step**2) for step in x_soln]


# Second test ODE
# dy/dx = cos(x)
def f_x2(x):
    """This function implements the ODE we're trying to solve
    In this case y' = dy/dx = cos(x)
    This corresponds to y = sin(x)
    """
    f_x2 = np.cos(x)                    # The equation given above
    return f_x2
# Exact solution to compare to our numerically obtained solution
y_analitical2 = [np.sin(step) for step in x_soln]


# Third test ODE
# dy/dx = 3x^2
def f_x3(x):
    """This function implements the ODE we're trying to solve
    In this case y' = dy/dx = 3x^2
    This corresponds to y = x^3
    """
    f_x3 = 3 * x ** 2                   # The equation given above
    return f_x3
# Exact solution to compare to our numerically obtained solution
y_analitical3 = [(step**3) for step in x_soln]


'------------------------------Begin TestEuler-------------------------------------'
# Define all the tests for hw.euler method
# Numerical approximation using Euler method
y0 = start ** 2                         # Initial value or boundary condition
test1 = hw.euler(f_x, x_hw, h, y0)
answer1 = soln.euler(f_x, x_soln, h, y0)

# Numerical approximation using Euler method
y0 = np.sin(start)                      # Initial value or boundary condition
test2 = hw.euler(f_x2, x_soln, h, y0)
answer2 = soln.euler(f_x2, x_soln, h, y0)

# Numerical approximation using Euler method
y0 = (start ** 3)                       # Initial value or boundary condition
test3 = hw.euler(f_x3, x_soln, h, y0)
answer3 = soln.euler(f_x3, x_soln, h, y0)

# Plot and compare hw & soln
figure1 = plt.figure()
figure1.suptitle('Numerical Approximations of y Using the Euler Method',
                 fontsize=14, fontweight='bold')
subplot = figure1.add_subplot(311)      # 3 x 1 subplots in plot; this is subplot1
subplot.set_ylabel('y')
subplot.set_title('y = x^2')
subplot.plot(x_soln, test1, 'r.', x_soln, answer1, 'bx', x_soln, y_analitical1, 'k')
subplot = figure1.add_subplot(312)      # 3 x 1 subplots in plot; this is subplot1
subplot.set_ylabel('y')
subplot.set_title('y = sin(x)')
subplot.plot(x_soln, test2, 'r.', x_soln, answer2, 'bx', x_soln, y_analitical2, 'k')
subplot = figure1.add_subplot(313)      # 3 x 1 subplots in plot; this is subplot1
subplot.set_xlabel('x')
subplot.set_ylabel('y')
subplot.set_title('y = x^3')
subplot.plot(x_soln, test3, 'r.', x_soln, answer3, 'bx', x_soln, y_analitical3, 'k')
plt.show()
'------------------------------End TestEuler---------------------------------------'


'------------------------------Begin TestRK----------------------------------------'
# Define all the tests for hw.euler method
# Numerical approximation using RK method
y0 = start ** 2                         # Initial value or boundary condition
test1 = hw.rk(f_x, x_hw, h, y0)
answer1 = soln.rk(f_x, x_soln, h, y0)

# Numerical approximation using rk method
y0 = np.sin(start)                      # Initial value or boundary condition
test2 = hw.rk(f_x2, x_soln, h, y0)
answer2 = hw.rk(f_x2, x_soln, h, y0)

# Numerical approximation using rk method
y0 = (start ** 3)                       # Initial value or boundary condition
test3 = hw.rk(f_x3, x_soln, h, y0)
answer3 = hw.rk(f_x3, x_soln, h, y0)

# Plot and compare hw & soln
figure1 = plt.figure()
figure1.suptitle('Numerical Approximations of y Using the Runge-Kutta Method',
                 fontsize=14, fontweight='bold')
subplot = figure1.add_subplot(311)      # 3 x 1 subplots in plot; this is subplot1
subplot.set_ylabel('y')
subplot.set_title('y = x^2')
subplot.plot(x_soln, test1, 'r.', x_soln, answer1, 'bx', x_soln, y_analitical1, 'k')
subplot = figure1.add_subplot(312)      # 3 x 1 subplots in plot; this is subplot1
subplot.set_ylabel('y')
subplot.set_title('y = sin(x)')
subplot.plot(x_soln, test2, 'r.', x_soln, answer2, 'bx', x_soln, y_analitical2, 'k')
subplot = figure1.add_subplot(313)      # 3 x 1 subplots in plot; this is subplot1
subplot.set_xlabel('x')
subplot.set_ylabel('y')
subplot.set_title('y = x^3')
subplot.plot(x_soln, test3, 'r.', x_soln, answer3, 'bx', x_soln, y_analitical3, 'k')
plt.show()
'------------------------------End TestRK------------------------------------------'
