# python file 
import os
import sys 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import  Na_i, K_i, Ca_i, Na_o, K_o, Ca_o, g_BNa, g_BCa, g_BK, R, T, F ,E_CaL,E_Na,E_K


def background_currents(V, g_BNa, E_Na, g_BK, E_K, g_BCa, E_CaL, diabetes):
    # diabetic condition
    if diabetes is True:
        g_BCa = 0.5 * g_BCa
        g_BNa = 1.25 * g_BNa
    
    print(E_K)
    I_BNa = g_BNa * (V - E_Na)
    I_BK = g_BK * (V - E_K)
    I_BCa = g_BCa * (V - E_CaL)
    I_B = I_BNa + I_BCa + I_BK
    return I_BNa, I_BK, I_BCa, I_B

V_range = np.linspace(-60, 60, 100)

diabetes = False

# Initialising arrays 
I_BNa_values = []
I_BK_values = []
I_BCa_values = []
I_B_values = []


for V in V_range:
    I_BNa, I_BK, I_BCa, I_B =  background_currents(V, g_BNa, E_Na, g_BK, E_K, g_BCa, E_CaL,diabetes )
    I_BNa_values.append(I_BNa)
    I_BK_values.append(I_BK)
    I_BCa_values.append(I_BCa)
    I_B_values.append(I_B)

diabetes = True

# Initialising arrays 
I_BNa_diabetic_values = []
I_BK_diabetic_values = []
I_BCa_diabetic_values = []
I_B_diabetic_values = []

for V in V_range:
    I_BNa_diabetic, I_BK_diabetic, I_BCa_diabetic, I_B_diabetic =  background_currents(V, g_BNa, E_Na, g_BK, E_K, g_BCa, E_CaL,diabetes)
    I_BNa_diabetic_values.append(I_BNa_diabetic)
    I_BK_diabetic_values.append(I_BK_diabetic)
    I_BCa_diabetic_values.append(I_BCa_diabetic)
    I_B_diabetic_values.append(I_B_diabetic)

# Normalising values to get current density
C = 100e-6 #microfarads
normalised_healthy_i_t = np.array(I_B_values) * 1e-3 / C
normalised_diabetic_i_t = np.array(I_B_diabetic_values) * 1e-3 / C

fig, axs = plt.subplots(1, 2, figsize=(20, 6), sharey=True)

# healthy
axs[0].plot(V_range, I_BNa_values, label='I_BNa (Healthy)', color='blue')
axs[0].plot(V_range, I_BK_values, label='I_BK (Healthy)', color='green')
axs[0].plot(V_range, I_BCa_values, label='I_BCa (Healthy)', color='red')
axs[0].plot(V_range, I_B_values, label='I_B (Healthy)', color='black', linestyle='--')
axs[0].set_xlabel('Membrane Potential (mV)')
axs[0].set_ylabel('Current (nA)')
axs[0].set_title('Healthy Myocyte Background Currents')
axs[0].legend()
axs[0].grid(True)

# diabetic
axs[1].plot(V_range, I_BNa_diabetic_values, label='I_BNa (Diabetic)', color='blue')
axs[1].plot(V_range, I_BK_diabetic_values, label='I_BK (Diabetic)', color='green')
axs[1].plot(V_range, I_BCa_diabetic_values, label='I_BCa (Diabetic)', color='red')
axs[1].plot(V_range, I_B_diabetic_values, label='I_B (Diabetic)', color='black', linestyle='--')
axs[1].set_xlabel('Membrane Potential (mV)')
axs[1].set_title('Diabetic Myocyte Background Currents')
axs[1].legend()
axs[1].grid(True)

# both
plt.figure(figsize=(10, 6))
plt.plot(V_range, I_BNa_values, label='I_BNa (Healthy)', color='blue', linestyle='--')
plt.plot(V_range, I_BNa_diabetic_values, label='I_BNa (Diabetic)', color='blue')
plt.plot(V_range, I_BK_values, label='I_BK (Healthy)', color='green', linestyle='--')
plt.plot(V_range, I_BK_diabetic_values, label='I_BK (Diabetic)', color='green')
plt.plot(V_range, I_BCa_values, label='I_BCa (Healthy)', color='red', linestyle='--')
plt.plot(V_range, I_BCa_diabetic_values, label='I_BCa (Diabetic)', color='red')
plt.plot(V_range, I_B_values, label='I_B (Healthy)', color='black', linestyle='--')
plt.plot(V_range, I_B_diabetic_values, label='I_B (Diabetic)', color='black')
plt.xlabel('Membrane Potential (mV)')
plt.ylabel('Current (nA)')
plt.title('Healthy and Diabetic Myocyte Background Currents')
plt.legend()
plt.grid(True)
plt.show()