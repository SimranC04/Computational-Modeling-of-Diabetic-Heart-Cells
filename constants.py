import numpy as np
#membrane parameters 

# Concentraions 
Na_i = 1.073519e+01 #(mM)
K_i = 1.392751e+02 #(mM)
Ca_i = 7.901351e-05 #(mM)
Na_o = 140.0 #(mM)
K_o = 5.4 #(mM)
Ca_o = 1.2 #(mM)

# Conductance values  
g_Na = 0.8  # µS, Maximum conductance for I_Na
g_CaL = 0.031  # µS, Maximum conductance for I_CaL
g_t = 0.035  # µS, Maximum conductance for I_t
g_ss = 0.007  # µS, Maximum conductance for I_ss
g_K1 = 0.024  # µS, Maximum conductance for I_K1
g_BNa = 8.015e-05  # µS, Maximum conductance for I_B,Na
g_BCa = 3.24e-05  # µS, Maximum conductance for I_B,Ca
g_BK = 13.8e-05  # µS, Maximum conductance for I_B,K
g_f = 0.00145  # µS, Maximum conductance for I_f

# Nernst Stuff
F = 96487.0  # C/mol, Faraday constant
T = 295  # K, Absolute temperature
R = 8314.0  # mJ/mol K, Ideal gas constant
E_Na = (R * T / F) * np.log(Na_o / Na_i) * 1000
E_K = (R * T / F) * np.log(K_o / K_i) * 1000
E_CaL = (R * T / (2 * F)) * np.log(Ca_o / Ca_i) * 1000

# Other parameteres
I_NaK_max = 0.08  # nA, Maximum I_NaK current
K_m_Na = 10.0  # mM, Half-maximum Na+ binding constant for I_NaK
K_m_K = 1.5  # mM, Half-maximum K+ binding constant for I_NaK
I_CaP_max = 0.004  # nA, Maximum I_CaP current
k_NaCa = 0.9984e-05  # (mM)^-4, Scaling factor for I_NaCa
d_NaCa = 0.0001  # (mM)^-4, Denominator constant for I_NaCa
gamma_NaCa = 0.5  # Position of energy barrier controlling voltage dependence for I_NaCa





