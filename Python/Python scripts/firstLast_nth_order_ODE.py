--#! /usr/local/bin/python3.4


# pedroIrazoqui_nth_order_ODE.py
# Create functions that will solve any order ODE using 4th order Runge-Kutta
# Use only standard Python, no NumPy

# Method to allow arbitrary ranges with floating point increments and 4 significant figures
def irange(start, stop, step):
    """ Create a generator to iterate over the interval we wish to solve the ODE on
    """
    while start < stop:
        yield round(start, 4)
        start += step


# 4th order Runge-Kutta methoc
def rk(odes, x_hw, h, y0s):
    
    M = len(odes)-1
    N = len(x_hw)-1

    u = [[y0s[m]] for m in range(0,M)]

    print(u)

    """k1 = [[(odes[m](x_hw[n], u[m])) for m in range(0,M)] for n in range(0,N)]
    k2 = [[(odes[m](x_hw[n] + 0.5*h, u[m] + 0.5*h*k1[n][m])) for m in range(0,M)] for n in range(0,N)]
    k3 = [[(odes[m](x_hw[n] + 0.5*h, u[m] + 0.5*h*k2[n][m])) for m in range(0,M-1)] for n in range(0,N-1)]
    k4 = [[(odes[m](x_hw[n] + h, u[m] + h*k3[n][m])) for m in range(0,M-1)] for n in range(0,N-1)]
    k_bar = [[((k1[n][m] + 2*k2[n][m] + 2*k3[n][m] + k4[n][m]) / 6) for m in range(0,M-1)] for n in range(0,N-1)]
    [[(u.append(u[m][n] + h*k_bar[n][m])) for m in range(0,M-1)] for n in range(0,N-1)]"""
        

    """ Solve for u(x, u1, u2, ..., uM) over interval, given M ODEs and boundary conditions 

    Slope 1:
    k11 = f1(x[n], u1[n], u2[n], ..., uM[n])
    k12 = f2(x[n], u1[n], u2[n], ..., uM[n])
    ...
    k1M = fM(x[n], u1[n], u2[n], ..., uM[n])
    ----------------------------------------------------------------------
    Slope 2:
    k21 = f1(x[n]+h/2, u1[n]+k11*h/2], u1[n]+k11*h/2], ..., uM[n]+k11*h/2])
    k22 = f2(x[n]+h/2, u1[n]+k12*h/2], u1[n]+k12*h/2], ..., uM[n]+k12*h/2])
    ...
    k2M = fM(x[n]+h/2, u1[n]+k1M*h/2], u1[n]+k1M*h/2], ..., uM[n]+k1M*h/2])
    ----------------------------------------------------------------------
    Slope 3:
    k31 = f1(x[n]+h/2, u1[n]+k21*h/2], u1[n]+k21*h/2], ..., uM[n]+k21*h/2])
    k32 = f2(x[n]+h/2, u1[n]+k22*h/2], u1[n]+k22*h/2], ..., uM[n]+k22*h/2])
    ...
    k3M = fM(x[n]+h/2, u1[n]+k2M*h/2], u1[n]+k2M*h/2], ..., uM[n]+k2M*h/2])
    ----------------------------------------------------------------------
    Slope 4:
    k41 = f1(x[n]+h/2, u1[n]+k31*h/2], u1[n]+k31*h/2], ..., uM[n]+k31*h/2])
    k42 = f2(x[n]+h/2, u1[n]+k32*h/2], u1[n]+k32*h/2], ..., uM[n]+k32*h/2])
    ...
    k4M = fM(x[n]+h/2, u1[n]+k3M*h/2], u1[n]+k3M*h/2], ..., uM[n]+k3M*h/2])
    ----------------------------------------------------------------------
    Weighted average slope:
    k_bar1 = (k11 + 2*k21 + 2*k31 + k41) / 6
    k_bar2 = (k12 + 2*k22 + 2*k32 + k42) / 6
    ...
    k_barM = (k1M + 2*k2M + 2*k3M + k4M) / 6
    ----------------------------------------------------------------------
    Next value:
    u1[n+1] = u1[n] + (k_bar1 * h)
    u2[n+1] = u2[n] + (k_bar2 * h)
    ...
    uM[n+1] = uM[n] + (k_barM * h)
    """
    return u                    # Return solution matrix, with u[:][0] = y
