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









