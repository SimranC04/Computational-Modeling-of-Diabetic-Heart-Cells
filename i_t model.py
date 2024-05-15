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


