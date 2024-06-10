
import numpy as np

# Concentraions 
Na_i = 1.073519e+01
K_i = 1.392751e+02
Ca_i = 7.901351e-05

Na_o = 140.0
K_o = 5.4
Ca_o = 1.2

# Constants 
g_BNa = 8.015e-05
g_BCa = 3.24e-05
g_BK = 13.8e-05

R = 8.314
T = 310.15
F = 96485

# Nernst 
E_Na = (R * T / F) * np.log(Na_o / Na_i) * 1000
E_K = (R * T / F) * np.log(K_o / K_i) * 1000
E_CaL = (R * T / (2 * F)) * np.log(Ca_o / Ca_i) * 1000


def background_currents(V, g_BNa, E_Na, g_BK, E_K, g_BCa, E_CaL):
    I_BNa = g_BNa * (V - E_Na)
    I_BK = g_BK * (V - E_K)
    I_BCa = g_BCa * (V - E_CaL)
    I_B = I_BNa + I_BCa + I_BK
    return I_BNa, I_BK, I_BCa, I_B
