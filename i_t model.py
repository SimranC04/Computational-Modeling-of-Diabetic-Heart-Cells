import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

"""
Calcium-independent Transient Outward K+ Current (I_t) 
💡 Task 1 : Create a matlab/python code for the cell model
    - create a new cell model for I_t
    - set a volatge 10 millivolts
    - run it to steady state
    - the value will a singular data point on the graph
    - model with 4 state variables  a_endo, s, b_endo, s
    - very simple to pull out and code up
    - look at paper to describe the channel and it will show an equation for it
"""
""" C o n s t a n t s """
# Constants from the paper itself 
g_t = 0.035
g_t_endo = 0.4647*g_t
a_endo = 0.583
b_endo =  0.417
a_epi = 0.886
b_epi = 0.114
K_o = 5.4  
K_i= 139.2751 
T = 295
R = 8314.5  
F = 96487 
V = -80.514


# Membrane potential array from -60 mV to 60 mV
V = np.linspace(-60, 60, 100)

""" E q u a t i o n s   f r o m   t h e   p a p e r """

# Ca_independent_transient_outward_K_current_r_gate
def r_gate(V, t):
    r_infinity = 1 / (1 + np.exp((V + 10.6) / -11.42))
    tau_r = 1 / (45.16 * np.exp(0.03577 * (V + 50)) + 98.9 * np.exp(-0.1 * (V + 38)))
    return r_infinity, tau_r

def dr_dt(t, r, V):
    r_infinity, tau_r = r_gate(V, t)
    return (r_infinity - r) / tau_r

# Ca_independent_transient_outward_K_current_s_gate
def s_gate(V, t):
    s_infinity = 1 / (1 + np.exp((V + 45.3) / 6.8841))
    tau_s_endo = 0.55 * np.exp(-((V + 70) / 25)**2) + 0.049
    return s_infinity, tau_s_endo

def ds_dt(t, s, V):
    s_infinity, tau_s_endo = s_gate(V, t)
    return (s_infinity - s) / tau_s_endo

# Ca_independent_transient_outward_K_current_s_slow_gate
def s_slow_gate(V, t):
    s_slow_infinity = 1 / (1 + np.exp((V + 45.3) / 6.8841))
    tau_s_slow_endo = 3.3 * np.exp(-((V + 70) / 30)**2) + 0.049
    return s_slow_infinity, tau_s_slow_endo

def ds_slow_dt(t, s_slow, V):
    s_slow_infinity, tau_s_slow_endo = s_slow_gate(V, t)
    return (s_slow_infinity - s_slow) / tau_s_slow_endo








