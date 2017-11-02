import numpy as np
import sys
import matplotlib as plt


def main():

	irange(0,(N-1),h)
	euler()
	rk()

def irange(start, stop, step):
	"""Create a generator to iterate over the interval we wish to solve the ODE on."""
	while start < stop:
		yield round(start,4)
		start += step

def euler(ode, interval, step_size, initial_value):
	"""Solve for y(x) given ODE dy/dx = f(x) and boundary conditions, over the values in interval y_n+1 = y_n + (f(x) * h)"""
	#"Your Code Here"

	return y

def rk(ode, interval, step_size, initial_value):
	"""Solve for y(x), given ODE dy/dx = f(x) and boundary conditions, over the values in interval 
	k1 = f(x[n],y[n])
	k2 = f(x[n] + h/2,y[n] + k1*h/2)
	k3 = f(x[n] + h/2,y[n] + k2*h/2)
	k4 = f(x[n] + h,y[n] + k3*h)
	k_bar = (k1 + 2*k2 + 2*k3 + k4) / 6
	y[n+1] = y[n] + (k_bar * h)"""

	#"Your Code Here"
	

	return y

if __name__ == "__main__":
	main()