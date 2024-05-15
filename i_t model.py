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



""" S o l v i n g   f r o m   t h e   p a p e r """

# Initial values got these from the model
r0 = 0.002191519
s0 = 0.9842542
s_slow0 = 0.6421196

# Time span for 2 Hz (0 to 500 ms)
t_span = (0, 500)
t_eval = np.linspace(0, 500, 1001)

# Solving the differential equations
r_solution = solve_ivp(dr_dt, t_span, [r0], args=(V,), t_eval=t_eval)
s_solution = solve_ivp(ds_dt, t_span, [s0], args=(V,), t_eval=t_eval)
s_slow_solution = solve_ivp(ds_slow_dt, t_span, [s_slow0], args=(V,), t_eval=t_eval)

# Extract the final steady-state values
r_steady = r_solution.y[0][-1]
s_steady = s_solution.y[0][-1]
s_slow_steady = s_slow_solution.y[0][-1]

# Calculating E_K using the Nernst equation
E_K = R*T/F*np.log(K_o/K_i)

# Calculating the current 
i_t = g_t_endo*r_solution*(a_endo*s_solution+b_endo*s_slow_solution)*(V-E_K)






