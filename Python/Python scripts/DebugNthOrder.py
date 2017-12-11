import numpy as np
import sys
import matplotlib as plt

def main():
	start = 0                               # Start of range
	stop = 20                               # Stop of range
	N = 100                                 # Number of steps
	h = (stop - start)/(N-1)                # Step size
	# Instantiate the independent variable
	x_hw = [i for i in irange(start, stop, h)]

	y_initial = np.sin(start) 
	y_prime_initial = np.cos(start)

	rk([ode1_u1, ode1_u2], x_hw, h, [y_initial, y_prime_initial])

def ode1_u1(x,u):
	u1_prime = u[1]
	return u1_prime

def ode1_u2(x,u):
	u2_prime = -np.sin(x)
	return u2_prime

def irange(start, stop, step): 
	while start < stop:
		yield round(start,4)
		start += step

def rk(odes, x_hw, h, y0s):

	M = (len(odes))
	N = (len(x_hw))

	u = [[y0s[m] for m in range(0,M)]]

	k1 = []
	k2 = []
	k3 = []
	k4 = []
	k_bar = []

	for n in range(0,N-1):
		k1.append([odes[m](x_hw[n], u[n]) for m in range(0,M)])

		k2.append([(odes[m](x_hw[n] + 0.5*h, u[n] + 0.5*h*k1[n][m])) for m in range(0,M)])
		k3.append([(odes[m](x_hw[n] + 0.5*h, u[n] + 0.5*h*k2[n][m])) for m in range(0,M)])
		k4.append([(odes[m](x_hw[n] + h, u[n] + h*k3[n][m])) for m in range(0,M)])

		k_bar.append([((k1[n][m] + 2*k2[n][m] + 2*k3[n][m] + k4[n][m]) / 6) for m in range(0,M)])

		u.append([u[n][m] + h*k_bar[n][m] for m in range(0,M)])

	print(u)

	return u

if __name__ == "__main__":
	main()