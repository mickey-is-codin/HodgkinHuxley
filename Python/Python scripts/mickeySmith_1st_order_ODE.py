import sys
import matplotlib as plt

def irange(start, stop, step): 
	while start < stop:
		yield round(start,4)
		start += step

def euler(ode, x_hw, h, y0):

	y = [] 
	y.append(y0)

	[y.append(y[n] + (h*ode(x_hw[n]))) for n in range(0,len(x_hw)-1)] 

	return y

def rk(ode, x_hw, h, y0):

	y=[]
	y.append(y0)

	k1 = [(ode(x_hw[n]))for n in range (0,len(x_hw)-1)]
	k2 = [(ode(x_hw[n] + 0.5*h))for n in range (0,len(x_hw)-1)]
	k3 = [(ode(x_hw[n] + 0.5*h))for n in range (0,len(x_hw)-1)]
	k4 = [(ode(x_hw[n] + h))for n in range (0,len(x_hw)-1)]
	k_bar = [((k1[n] + 2*k2[n] + 2*k3[n] + k4[n]) / 6) for n in range(0,len(x_hw)-1)]
	[y.append(y[n] + k_bar[n]*h) for n in range(0,len(x_hw)-1)]

	return y

if __name__ == "__main__":
    main()
