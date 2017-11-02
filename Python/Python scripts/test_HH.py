#! /usr/local/bin/python3.4
# test_HH.py


import numpy as np                  # used only for constants, exponents, and such
import matplotlib.pyplot as plt     # For plotting

# import the first name of the user
firstname = input('Please enter your first name: \n>> ')
# import the last name of the user
lastname = input('Please enter your last name: \n>> ')
rk = __import__(firstname.lower()+lastname.title()+'_nth_order_ODE')
hh = __import__(firstname.lower()+lastname.title()+'_HH')

# Time window
start = 0                               # Start time in ms
stop = 20                               # Stop time in ms
step_size = 0.01                        # Step size = 0.0005 ms
# Instantiate the independent variable
interval = [i for i in rk.irange(start, stop, step_size)]
# Initial conditions
Vm0 = 0                                 # Resting membrane potential
Je = np.zeros(len(interval))            # Resting current
# n0 = alpha_n0/(alpha_n0 + beta_n0)
alpha_n0 = (0.01 * (Vm0 + 10)) / (np.exp((Vm0 + 10) / 10) - 1)
beta_n0 = 0.125 * np.exp(Vm0 / 80)
n0 = alpha_n0 / (alpha_n0 + beta_n0)    # Initial value for n
# m0 = alpha_m0/(alpha_m0 + beta_m0)
alpha_m0 = (0.1 * (Vm0 + 25)) / (np.exp((Vm0 + 25) / 10) - 1)
beta_m0 = 4 * np.exp(Vm0 / 18)
m0 = alpha_m0 / (alpha_m0 + beta_m0)    # Initial value for m
# h0 = alpha_h0/(alpha_h0 + beta_h0)
alpha_h0 = 0.07 * np.exp(Vm0 / 20)
beta_h0 = 1 / (np.exp((Vm0 + 30) / 10) + 1)
h0 = alpha_h0 / (alpha_h0 + beta_h0)    # Initial value for h

# Stimulate the neuron:
# Recall that HH defines Vm as our -Vm, so a starting Vm=-15 corresponds to
# a 15 mV depolarizating post-synaptic potential. Similarly, current is
# defined by HH as flowing in to the cell, so Je=-200 corresponds to a
# depolarizing current of 200 uA/cm^2
print('You can stimulate the neuron with either a current pulse or a PSP')
stim = input('For a current pulse enter "I", for a PSP enter "V". \n>> ')
if stim == 'V' or stim == 'v':
    Vm0 = -1 * float(input('Please enter post-synaptic potential amplitude in mV: \n>> '))
elif stim == 'I' or stim == 'i':
    tstart = float(input('Please enter current pulse start time in ms: \n>> '))
    # For example tstart = 1 ms
    tstop = float(input('Please enter current pulse stop time in ms: \n>> '))
    # For example tstart = 1.05 ms
    Je_amp = -1 * float(input('Please enter depolarizing current amplitude in uA/cm^2: \n>> '))
    # For example Je_amp = -200 mA / cm^2
    Je = [Je_amp if i >= tstart and i < tstop else 0 for i in interval]
else:
    print('Running with no stimulus.')

# Find membrane voltage Vm, and the ionic currents Jk and Jna
initial_values = [Vm0, n0, m0, h0]                              # Initial values
odes = [hh.vmp_eq_26, hh.np_eq_7, hh.mp_eq_15, hh.hp_eq_16]     # ODEs
# Solve as system of four 1st order ODEs
solution = rk.rk(odes, interval, step_size, initial_values)
# Remember note:  HH defines Vm = Vo-Vi, whereas we define Vm = Vi-Vo so using
# the constants above and Eq. 26, 7, 15, and 16 requires flipping Vm here
Vm = [-row[0] for row in solution]                          # Membrane voltage
n = [row[1] for row in solution]
Jk = [hh.gk_bar * val**4 for val in n]                         # Potassium current
m = [row[2] for row in solution]
h = [row[3] for row in solution]
Jna = [hh.gna_bar * val**3 * h[m.index(val)] for val in m]     # Sodium current

# Plot
figure1 = plt.figure(figsize=(10, 10))
figure1.suptitle("Numerical Approximations of Hodgkin-Huxley",
                 fontsize=14, fontweight='bold')
subplot = figure1.add_subplot(311)      # 1 x 1 subplots in plot; this is subplot1
subplot.set_title('Stimulus Current Je')
subplot.set_ylabel('Je (uA/cm^2)')
subplot.plot(interval, Je, 'k')
subplot = figure1.add_subplot(312)      # 1 x 1 subplots in plot; this is subplot1
subplot.set_title('Membrane Voltage Vm')
subplot.set_ylabel('Voltage (mV)')
subplot.plot(interval, Vm, 'r.')
subplot = figure1.add_subplot(313)      # 1 x 1 subplots in plot; this is subplot1
subplot.set_title('Transient inward Na current (blue) and delayed outward K current (green)')
subplot.set_xlabel('time (ms)')
subplot.set_ylabel('Jion (uA/cm^2)')
subplot.plot(interval, Jna, 'b', interval, Jk, 'g')
plt.show()
