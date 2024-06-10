
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


""" C o n s t a n t s """
# Constants from the paper itself 
g_ss = 0.007
K_o = 5.4  
K_i= 139.2751 
T = 295
R = 8314.5  
F = 96487 

""" E q u a t i o n s   f r o m   t h e   p a p e r """
def I_ss(g_ss, V, E_K):
    r_ss_value = None
    s_ss_value = None
    return g_ss * r_ss_value * s_ss_value * (V - E_K)

# Ca_independent_transient_outward_K_current_s_slow_gate
def dr_ss_dt(t,r_ss_current, V):
    tau_r_ss = 10.0 / 45.16 * np.exp(0.03577 * (V + 50.0)) + 98.9 * np.exp(-0.1 * (V + 38.0))
    r_ss = 1 / (1 + np.exp((V + 11.5) / -11.82))
    return (r_ss - r_ss_current) / tau_r_ss

# Ca_independent_transient_outward_K_current_s_slow_gate
def ds_ss_dt(t,s_ss_current, V):
    tau_s_ss = 2.1
    s_ss = 1 / (1 + np.exp((V + 87.5) / 10.3))
    return (s_ss - s_ss_current) / tau_s_ss


""" S o l v i n g   E q u a t i o n s """
def solve_differential(V,t_eval): 
    # Initial values got these from the model
    r_ss_0 = 0.002907171
    s_ss_0 = 0.3142767
    t_span = (0, 200)

    # Solving the differential equations
    r_ss_solution = solve_ivp(dr_ss_dt, t_span, [r_ss_0], args=(V,), t_eval=t_eval,  method='RK45')
    s_ss_solution = solve_ivp(ds_ss_dt, t_span, [s_ss_0], args=(V,), t_eval=t_eval,  method='RK45')

    # Extract the final steady-state values
    # ASSUMPTION : final solution is steadystate as its taking incredibly long to run the code 
    r_ss_steady = r_ss_solution.y[0]
    s_ss_steady = s_ss_solution.y[0]

    return r_ss_steady,s_ss_steady


# Using solver to calculated the steady state values
V_test = -40
t_eval = np.linspace(0, 200, 4)
r_ss_solution,s_ss_solution= solve_differential(V_test,t_eval)

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Plot R_ss Solution
axs[0].plot(t_eval, r_ss_solution, label='r_solution')
#axs[0].plot(t_manual, r_steady_manual, label='r_steady_manual', linestyle='--')
axs[0].set_title('R_ss Solution')
axs[0].legend()

# Plot S_ss Solution
axs[1].plot(t_eval, s_ss_solution, label='s_solution')
#axs[1].plot(t_manual, s_steady_manual, label='s_steady_manual', linestyle='--')
axs[1].set_title('S_ss Solution')
axs[1].legend()