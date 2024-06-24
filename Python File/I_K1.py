import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import K_o, g_K1,E_K,E_Na,F,R,T,K
import numpy as np


K1_o = K_o 

def I_K1(V):
    term1 = 48 / (np.exp((V + 37) / 25) + np.exp((V + 37) / -25)) + 10
    term2 = 0.0001 / (1 + np.exp((V - E_K - 76.77) / 17))
    term3 = g_K1 * (V - E_K - 1.73) / (1 + np.exp(1.613 * F * (V - E_K - 1.73) / (R * T))) / (1 + np.exp(K1_o - 0.9988 / -0.124))
    return term1 * term2 + term3

