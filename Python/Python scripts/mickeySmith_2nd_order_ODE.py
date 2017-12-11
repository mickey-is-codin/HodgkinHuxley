import numpy as np
import sys
import matplotlib as plt

def irange(start, stop, step): 
	while start < stop:
		yield round(start,4)
		start += step

def euler(ode_u1, ode_u2, x_hw, h, u1_0, u2_0):

	u1 = [0 for i in range(0,len(x_hw))] #Initialize u1 with an array of zeros so that I don't have to use a bunch of append functions.
	u2 = [0 for i in range(0,len(x_hw))] #Initialize u2 with an array of zeros so that I don't have to use a bunch of append functions.

	u1[0] = (u1_0) #Add the initial values so we can build on them.
	u2[0] = (u2_0) #Add the inidial values so we can build on them.

	#[u2.append(u2[n] + h*ode_u2(x_hw[n], u1[n], u2[n])) for n in range(0,len(x_hw)-1)]
	#[u1.append(u1[n] + h*ode_u1(x_hw[n], u1[n], u2[n])) for n in range(0,len(x_hw)-1)]
	#This didn't work because u2 uses previous u1 and u2 values so they have to both be built in sequence before going to the next n value.

	for n in range(1, len(x_hw)):
		u2[n] = (u2[n-1] + h * ode_u2(x_hw[n-1], u1[n-1], u2[n-1])) #Building u2 using the previous values of u2 and the ode function given in the test script.
		u1[n] = (u1[n-1] + h * ode_u1(x_hw[n-1], u1[n-1], u2[n-1])) #Building u1 using the previous values of u1 and the ode function given in the test script.

	#For loop used to add values incrementally to u2 and then u1 since u2 is the second derivative.
	#The euler method formula is used to build the arrays.	
	#Difficulty with a list comprehension here is the necessity for u1 in u2 so a list comp would have to be nested or otherwise more complicated than I'm understanding.

	return u1, u2

def rk(ode_u1, ode_u2, x_hw, h, u1_0, u2_0):

	u1 = [0 for i in range(0,len(x_hw))] #Initialize u1 with an array of zeros so that I don't have to use a bunch of append functions.
	u2 = [0 for i in range(0,len(x_hw))] #Initialize u2 with an array of zeros so that I don't have to use a bunch of append functions.

	u1[0] = (u1_0) #Add the initial values so we can build on them.
	u2[0] = (u2_0) #Add the inidial values so we can build on them.

	for n in range(1,len(x_hw)):

		k1_u1 = ode_u1(x_hw[n-1], u1[n-1], u2[n-1]) #Building k1 at each point for first solution
		k1_u2 = ode_u2(x_hw[n-1], u1[n-1], u2[n-1]) #Building k1 at each point for second solution
		
		k2_u1 = ode_u1(x_hw[n-1] + 0.5*h, u1[n-1] + 0.5*h*k1_u1, u2[n-1] + 0.5*h*k1_u2) #Building k2 at each point for first solution
		k2_u2 = ode_u2(x_hw[n-1] + 0.5*h, u1[n-1] + 0.5*h*k1_u1, u2[n-1] + 0.5*h*k1_u2) #Building k2 at each point for second solution

		k3_u1 = ode_u1(x_hw[n-1] + 0.5*h, u1[n-1] + 0.5*h*k2_u1, u2[n-1] + 0.5*h*k2_u2) #Building k3 at each point for first solution 
		k3_u2 = ode_u2(x_hw[n-1] + 0.5*h, u1[n-1] + 0.5*h*k2_u1, u2[n-1] + 0.5*h*k2_u2) #Building k3 at each point for second solution

		k4_u1 = ode_u1(x_hw[n-1] + h, u1[n-1] + h*k3_u1, u2[n-1] + h*k3_u2)	#Building k4 at each point for first solution	
		k4_u2 = ode_u2(x_hw[n-1] + h, u1[n-1] + h*k3_u1, u2[n-1] + h*k3_u2) #Building k4 at each point for second solution

		print(k4_u1)

		kbar_u1 = (k1_u1 + 2*k2_u1 + 2*k3_u1 + k4_u1) / 6 #Calculating the weighted average slope for each point to find next u
		kbar_u2 = (k1_u2 + 2*k2_u2 + 2*k3_u2 + k4_u2) / 6 #Calculating the weighted average slope for each point to find next u

		u1[n] = (u1[n-1] + (kbar_u1*h)) #Find the next guess of where u1 will be using the previous value and a weighted slope
		u2[n] = (u2[n-1] + (kbar_u2*h)) #Find the next guess of where u2 will be using the previous value and a weighted slope 

	#For loop adds values incrementally, first building the k1 values for both solutions then increasing which k.
	#This method simply uses the runge-kutta method formula but makes use of the previous k values for each incremental k, this was not done in the first portion of the modeling assignment.

	return u1, u2

if __name__ == "__main__":
    main()
