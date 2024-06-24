import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import Na_i, K_i, Ca_i, Na_o, K_o, Ca_o, g_BNa, g_BCa, g_BK, R, T, F,E_K,E_CaL,E_Na,I_NaK_max,k_m_K,k_m_Na
import numpy as np

# Calculate sigma
sigma = (np.exp(Na_i / 67.3) - 1.0) / 7.0

# Calculate I_NaK
def I_NaK(V, I_NaK_max, sigma, K_o, k_m_K, F, R, T):
    term1 = 1.0 / (1.0 + 0.1245 * np.exp(0.1 * V * F / (R * T)) + 0.0365 * sigma * np.exp(V * F / (R * T)))
    term2 = K_o / (K_o + k_m_K)
    return I_NaK_max * term1 * term2

