# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 16:06:27 2020

@author: Spri
"""


import numpy as np
import matplotlib.pyplot as plt
time= np.loadtxt('Results/ATP deprived_voltages.dat', skiprows=1, usecols=(0))
potential= np.loadtxt('Results/ATP deprived_voltages.dat', skiprows=1, usecols=(1))

time1= np.loadtxt('Results/control_voltages.dat', skiprows=1, usecols=(0))
potential1= np.loadtxt('Results/control_voltages.dat', skiprows=1, usecols=(1))

time2= np.loadtxt('Results/ek -40_voltages.dat', skiprows=1, usecols=(0))
potential2= np.loadtxt('Results/ek -40_voltages.dat', skiprows=1, usecols=(1))

time3= np.loadtxt('Results/ena 30_voltages.dat', skiprows=1, usecols=(0))
potential3= np.loadtxt('Results/ena 30_voltages.dat', skiprows=1, usecols=(1))

time4= np.loadtxt('Results/gk by 5_voltages.dat', skiprows=1, usecols=(0))
potential4= np.loadtxt('Results/gk by 5_voltages.dat', skiprows=1, usecols=(1))

time5= np.loadtxt('Results/gna by .2_voltages.dat', skiprows=1, usecols=(0))
potential5= np.loadtxt('Results/gna by .2_voltages.dat', skiprows=1, usecols=(1))

time6= np.loadtxt('Results/gnat,kfast.2 gnap,kslow5_voltages.dat', skiprows=1, usecols=(0))
potential6= np.loadtxt('Results/gnat,kfast.2 gnap,kslow5_voltages.dat', skiprows=1, usecols=(1))

plot= plt.plot(time, potential, color='lightcoral')

plot1= plt.plot(time1, potential1, color='mediumaquamarine')

# plot2= plt.plot(time2, potential2, color='darkcyan')

# plot3= plt.plot(time3, potential3, color='magenta')

# plot4= plt.plot(time4, potential4, color='mediumpurple')

# plot5= plt.plot(time5, potential5, color='crimson')

plot6= plt.plot(time6, potential6, color='navy')

plt.legend(plot+ plot1 + plot6, ['ATP deprived', 'Control', 'Experimental'], loc='upper right')

saveopenimage(plt, 'soma potentials')

plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.show()