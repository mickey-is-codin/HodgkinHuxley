import math
import sys
import matplotlib

def GetUserInput():
	#Hard-Coded Variables


	#User Input Variables
	'''Cm = input("Membrane Conductance (mF/cm^2: ") #Paper Value: 1.0

	Vna = input("Sodium voltage (mV): ") #Paper Value: -115
	Vk = input("Potassium voltage (mV): ") #Paper Value: +12
	Vl = input("Leakage voltage (mV): ") #Paper Value: -10.613

	gBarNa = input("G bar for sodium (m.mho/cm^2): ") #Paper Value: 120
	gBarK = input("G bar for potassium (m.mho/cm^2): ") #Paper Value: 36
	gBarL = input("G bar for leakage (m.mho/cm^2): ")  #Paper Value: 0.3

	a = input("Neuron radius (m): ")
	ro = input("Outer resistance (ohms): ")
	ri = input("Inner resistance (ohms): ")

	Ke = input("Applied current (amps): ")'''

def Gna(gBarNa, m, h):
	Gna = gBarNa * m^3 * h
	return Gna

def Gk(gBarK, n):
	Gk = gBarK * n^4
	return Gk

def CurrentDensity(Cm, Vk, Vna, Vl):
	Jc = Cm * dVmdt
	Jk = Gk() * (Vm - Vk)
	Jna = Gna() * (Vm - Vna)
	Jl = Gl * (Vm - Vl)

	Jm = Jc + Jk + Jna + Jl

	return Jm

def ExponentialSolution(zero, infinity, tau, t)
	output = infinity - (infinity - zero) * exp(-t/tau)
	return output

def tau(alpha, beta):
	tau = 1 / (alpha + beta)
	return tau

def HuxleyRelations(a, ro, ri, Jm):
	Km = 2 * pi * a * Jm
	coeff = 1 / (2 * pi * a * (ro + ri))

	d2Vmdt2 = Jm * 2 * pi * a * (ro + ri)

def main():
	Cm = 1.0
	Vna = -115.0
	Vk = 12.0
	Vl = -10.613
	gBarNa = 120.0
	gBarK = 36.0
	gBarL = 0.3

	

if __name__ == "__main__":
	main()