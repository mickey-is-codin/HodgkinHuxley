import sys
import numpy as np
import matplotlib as plt

def main():

	start = -np.pi                          # Start of range
	stop = np.pi                            # Stop of range
	N = 100                                 # Number of steps
	h = (stop - start)/(N-1) 
	y0 = start**2

	x_hw = [i for i in irange(start, stop, h)]

	y_euler = euler(f_x, x_hw, h, y0)
	y_rk = rk(f_x, x_hw, h, y0)

	for i in range(0,len(y_euler)):
		print("Euler: ", y_euler[i], "RK: ", y_rk[i])

	print("Length of x values: ", len(x_hw))
	print("Length of Euler Solutions: ", len(y_euler))
	print("Length of RK Solution: ", len(y_rk))

def f_x(x):
    """This function implements the ODE we're trying to solve
    In this case y' = dy/dx = 2x
    This corresponds to y = x^2
    """
    f_x = 2 * x                         # The equation given above
    return f_x

def irange(start, stop, step): 
	"""Create a generator to iterate over the interval we wish to solve the ODE on."""
	while start < stop:
		yield round(start,4)
		start += step

def euler(ode, x_hw, h, y0):
	"""Solve for y(x) given ODE dy/dx = f(x) and boundary conditions, over the values in interval y_n+1 = y_n + (f(x) * h)"""

	#ode is 2x, it's a derivative solution so we're trying to go from 2x as an input to all of the points in x^2 as an output.
	#x_hw is the interval, irazoqui makes that interval in his script. It's irange from start to stop with step h.
	#h is the interval that irazoqui defines and inputs.
	#y0 is the inital value of the actual solution. he defines it as start^2 which is -pi^2.

	#Need to output y as an entire array, not calling the function more than once.

	y = [] #Initialize empty array
	y.append(y0) #Add the initial value to this array. It's now a one element array with y0 as it's only value.

	#Using interval because that has the correct h division amount of points between 0 and N.
	for n in range(0,len(x_hw)-1): 
		y.append(y[n] + h * ode(x_hw[n])) #We're solving the ode at each n, not each t!

	return y

def rk(ode, x_hw, h, y0):
	"""Solve for y(x), given ODE dy/dx = f(x) and boundary conditions, over the values in interval 
	k1 = f(x[n],y[n])
	k2 = f(x[n] + h/2,y[n] + k1*h/2)
	k3 = f(x[n] + h/2,y[n] + k2*h/2)
	k4 = f(x[n] + h,y[n] + k3*h)
	k_bar = (k1 + 2*k2 + 2*k3 + k4) / 6
	y[n+1] = y[n] + (k_bar * h)"""

	y = []
	y.append(y0)

	for n in range(0,len(x_hw)-1):
		k1 = ode(x_hw[n])
		k2 = ode(x_hw[n] + 0.5*h)
		k3 = ode(x_hw[n] + 0.5*h)
		k4 = ode(x_hw[n] + h)
		k_bar = (k1 + 2*k2 + 2*k3 + k4) / 6
		y.append(y[n] + (k_bar*h))

	return y


if __name__ == "__main__":
    main()
