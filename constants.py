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

#Nernst Stuff
R = 8314
T = 295
F = 96487

# nernst 
E_Na = (R * T / F) * np.log(Na_o / Na_i) * 1000
E_K = (R * T / F) * np.log(K_o / K_i) * 1000
E_CaL = (R * T / (2 * F)) * np.log(Ca_o / Ca_i) * 1000


