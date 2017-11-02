import numpy as np

#dy/dx = f(x) = cos(x)

#Analytically: y = sin(x) + C

#For any value of x you have a corresponding value of y

y = []
y0 = 0
y.append(y0)

f = 5000.0000 #sampling frequency
N = 41.0000 #number of samples
n = range(0,int(N-1)) #sample number from 0 through N - 1
T0 = 0 #start of interval
T = 4.0000 #total interval length sampled
h = T / (N - 1.0000) #separation between samples ====== h is the sampling rate!!!
#h = 1.0 / f#This one is based on the nyquist theorem
t = np.arange(T0,T,h)#independent variable

'''def Voltage(t):
	V = np.cos(t)
	return V'''

#result = Voltage(t)

print(h)

for i in range(0,int(N-1)):
	y.append(y[i] + h * (y[i] + np.power(t[i],3) - 2))	#Where yPrime is the actual function that we're useing as a diff eq

print(y[2])
print(t[2])

