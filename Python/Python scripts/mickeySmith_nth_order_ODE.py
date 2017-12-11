import numpy as np
import sys
import matplotlib as plt

def irange(start, stop, step): 
	while start < stop:
		yield round(start,4)
		start += step

def rk(odes, x_hw, h, y0s):

	M = (len(odes)) #Create a variable for the amount of elements in the ode array so I can index with this
	N = (len(x_hw)) #Create a variable for the amount of elements in the x array so I can index with this

	u = [[y0s[m] for m in range(0,M)]] #Make an array of one element arrays. Each of these sub-arrays contains only the initial value for a given ODE.

	k1 = [] #Initialize empty array for k1's
	k2 = [] #Initialize empty array for k2's
	k3 = [] #Initialize empty array for k3's ------->  The k's will be populated at each n. Each n value has 4 k's and a k_bar.
	k4 = [] #Initialize empty array for k4's
	k_bar = [] #Initialize empty array for k_bar's

	for n in range(0,N-1):
		k1.append([odes[m](x_hw[n], u[n]) for m in range(0,M)]) #For every m value add an index to the sub-array so that for every n value we have m k1 values. 
		k2.append([odes[m](x_hw[n] + 0.5*h, [u[n][z] + 0.5*h*k1[n][z] for z in range(0,M)]) for m in range(0,M)]) #For every m value add an index to the sub-array so that for every n value we have m k2 values.
		k3.append([odes[m](x_hw[n] + 0.5*h, [u[n][z] + 0.5*h*k2[n][z] for z in range(0,M)]) for m in range(0,M)]) #For every m value add an index to the sub-array so that for every n value we have m k3 values.
		k4.append([odes[m](x_hw[n] + h, [u[n][z] + h*k3[n][z] for z in range(0,M)]) for m in range(0,M)]) #For every m value add an index to the sub-array so that for every n value we have m k4 values.

		k_bar.append([((k1[n][m] + 2*k2[n][m] + 2*k3[n][m] + k4[n][m]) / 6) for m in range(0,M)]) #The k_bar array is indexed the same way but built as a weighted average of each k for all the ode's at an n point.

		#Every time n is incremented we add an m element array to the empty k array.
		#The k in the 2nd parameter for the odes() method is created with a sub-index list comprehension so that the same value is not given to each k.

		u.append([(u[n][m] + h*k_bar[n][m]) for m in range(0,M)]) #After each k has been added at a specific n value we add a u based on the weighted average of all of those k's.
			
	return u
