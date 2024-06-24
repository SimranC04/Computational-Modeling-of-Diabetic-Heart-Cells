import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import K_o, g_K1,E_K,E_Na,F,R,T,g_f
import numpy as np

# Constants
K1_o = K_o  # External potassium concentration

def I_f(V):
    y_inf =  1 / (1 + np.exp((V + 138.6) / 10.48))
    y = y_inf
    tau_y = 1 / (0.11885 * np.exp((V + 80.00) / 28.37) + 0.56236 * np.exp((V + 80.00) / -14.19))
    f_Na = 0.2
    f_K = 1 - f_Na
    return g_f * y * (f_Na * (V - E_Na) + f_K * (V - E_K))

# Voltage range
V_range = np.linspace(-120, 60, 100)

# Calculate currents
I_f_values = [I_f(V) for V in V_range]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(V_range, I_f_values, label='I_f', color='red')
plt.xlabel('Membrane Potential (mV)')
plt.ylabel('Current (pA)')
plt.title(' I_f vs Membrane Potential')
plt.legend()
plt.show()
