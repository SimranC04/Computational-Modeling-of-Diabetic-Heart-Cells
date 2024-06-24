import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import Na_i, K_i, Ca_i, Na_o, K_o, Ca_o, g_BNa, g_BCa, g_BK, R, T, F,E_K,E_CaL,E_Na
import numpy as np

def background_currents(V, g_BNa, E_Na, g_BK, E_K, g_BCa, E_CaL):
    I_BNa = g_BNa * (V - E_Na)
    I_BK = g_BK * (V - E_K)
    I_BCa = g_BCa * (V - E_CaL)
    I_B = I_BNa + I_BCa + I_BK
    return I_BNa, I_BK, I_BCa, I_B

