# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import solve_ivp

# """
# Calcium-independent Transient Outward K+ Current (I_t) 
# 💡 Task 1 : Create a matlab/python code for the cell model
#     - create a new cell model for I_t
#     - set a volatge 10 millivolts
#     - run it to steady state
#     - the value will a singular data point on the graph
#     - model with 4 state variables  a_endo, s, b_endo, s
#     - very simple to pull out and code up
#     - look at paper to describe the channel and it will show an equation for it
# """
# """ C o n s t a n t s """
# # Constants from the paper itself 
# g_t_epi = 0.035
# g_t_endo = 0.4647*g_t_epi
# a_endo = 0.583
# b_endo =  0.417
# a_epi = 0.886
# b_epi = 0.114
# K_o = 5.4  
# K_i= 139.2751 
# T = 295
# R = 8314.5  
# F = 96487 
# V = -80.514

# # Membrane potential array from -60 mV to 60 mV
# V = np.linspace(-60, 60, 10)

# """ E q u a t i o n s   f r o m   t h e   p a p e r """
# # Ca_independent_transient_outward_K_current_r_gate
# def dr_dt(t, r, V):
#     r_infinity = 1 / (1 + np.exp((V + 10.6) / -11.42))
#     tau_r = 1 / (45.16 * np.exp(0.03577 * (V + 50)) + 98.9 * np.exp(-0.1 * (V + 38)))
#     return (r_infinity - r) / tau_r

# # Ca_independent_transient_outward_K_current_s_gate
# def ds_dt(t, s, V):
#     s_infinity =  1 / (1 + np.exp((V + 45.3) / 6.8841))
#     tau_s_endo = 0.55 * np.exp(-((V + 70) / 25)**2) + 0.049
#     return (s_infinity - s) / tau_s_endo

# # Ca_independent_transient_outward_K_current_s_slow_gate
# def ds_slow_dt(t, s_slow, V):
#     s_slow_infinity = 1 / (1 + np.exp((V + 45.3) / 6.8841))
#     tau_s_slow_endo = 3.3 * np.exp(-((V + 70) / 30)**2) + 0.049
#     return (s_slow_infinity - s_slow) / tau_s_slow_endo

# """ S o l v i n g   E q u a t i o n s """
# # Function to compute I_t for given cell type
# def compute_current(cell_type, V):
#     if cell_type == 'endo':
#         a = a_endo
#         b = b_endo
#         g_t = g_t_endo
#     elif cell_type == 'epi':
#         a = a_epi
#         b = b_epi
#         g_t = g_t_epi

#         # Initial values got these from the model
#         r0 = 0.002191519
#         s0 = 0.9842542
#         s_slow0 = 0.6421196

#         # Time span
#         t_span = (0, 100)
#         t_eval = np.linspace(0, 100, 4)

#         # Solving the differential equations
#         r_solution = solve_ivp(dr_dt, t_span, [r0], args=(V,), t_eval=t_eval,  method='RK45')
#         s_solution = solve_ivp(ds_dt, t_span, [s0], args=(V,), t_eval=t_eval,  method='RK45')
#         s_slow_solution = solve_ivp(ds_slow_dt, t_span, [s_slow0], args=(V,), t_eval=t_eval,  method='RK45')

#         # Extract the final steady-state values
#         # ASSUMPTION : final solution is steadystate as its taking incredibly long to run the code
#         # plt.figure()
#         # plt.plot(t_eval, r_solution.y[0], label='r_solution')  # ENDOCARDIAL ISN"T WORKING
#         # plt.title('R Solution')
#         # plt.show()       
#         # plt.figure()
#         # plt.plot(t_eval, s_solution.y[0], label='r_solution')  # ENDOCARDIAL ISN"T WORKING
#         # plt.title('S Solution')
#         # plt.show()     
#         # plt.figure()
#         # plt.plot(t_eval, s_slow_solution.y[0], label='r_solution')  # ENDOCARDIAL ISN"T WORKING
#         # plt.title('S Slow Solution')
#         # plt.show()

#         r_steady = r_solution.y[0][-1]
#         s_steady = s_solution.y[0][-1]
#         s_slow_steady = s_slow_solution.y[0][-1]

#         # Calculating E_K using the Nernst equation
#         E_K = R*T/F*np.log(K_o/K_i)*1e3

#         # Compute I_t for both endocardial and epicardial cells over the range of voltages
#         i_t = g_t * r_steady * (a * s_steady + b* s_slow_steady) * (V - E_K)
#         return i_t

# # Compute i_t for both endocardial and epicardial cells over the range of voltages
# i_t_endo = np.zeros(len(V))
# i_t_epi = np.zeros(len(V))

# # manually calculation of steady state values 
# r_steady_manual = np.zeros(len(V))
# s_steady_manual = np.zeros(len(V))
# s_slow_steady_manual = np.zeros(len(V))
# for i,v in enumerate(V):
#     r_steady_manual[i] = 1 / (1 + np.exp((v + 10.6) / -11.42))
#     s_steady_manual[i] =  1 / (1 + np.exp((v + 45.3) / 6.8841))
#     s_slow_steady_manual[i] = 1 / (1 + np.exp((v + 45.3) / 6.8841))

# for i, v in enumerate(V):
#     i_t_endo[i] = compute_current('endo', v)
#     i_t_epi[i] = compute_current('epi', v)

# """ P l o t t i n g   R e s u l t s """
# # Plotting the results
# plt.figure()
# plt.plot(V, i_t_endo, label='Endocardial')  # ENDOCARDIAL ISN"T WORKING
# plt.plot(V, i_t_epi, label='Epicardial')
# plt.xlabel('Membrane Potential (mV)')
# plt.ylabel('I_t')
# plt.title('Transient Outward Potassium Current (I_t) vs Membrane Potential')
# plt.legend()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g_t_epi = 0.035
g_t_endo = 0.4647 * g_t_epi
a_endo = 0.583
b_endo = 0.417
a_epi = 0.886
b_epi = 0.114
K_o = 5.4
K_i = 139.2751
T = 295
R = 8314.5
F = 96487

# Membrane potential array from -60 mV to 60 mV
V = np.linspace(-60, 60, 50)  # Reduced number of points for faster computation

# Equations for the gates
def dr_dt(t, r, V):
    r_infinity = 1 / (1 + np.exp((V + 10.6) / -11.42))
    tau_r = 1 / (45.16 * np.exp(0.03577 * (V + 50)) + 98.9 * np.exp(-0.1 * (V + 38)))
    return (r_infinity - r) / tau_r

def ds_dt(t, s, V):
    s_infinity = 1 / (1 + np.exp((V + 45.3) / 6.8841))
    tau_s_endo = 0.55 * np.exp(-((V + 70) / 25)**2) + 0.049
    return (s_infinity - s) / tau_s_endo

def ds_slow_dt(t, s_slow, V):
    s_slow_infinity = 1 / (1 + np.exp((V + 45.3) / 6.8841))
    tau_s_slow_endo = 3.3 * np.exp(-((V + 70) / 30)**2) + 0.049
    return (s_slow_infinity - s_slow) / tau_s_slow_endo

# Function to compute I_t for given cell type
def compute_current(cell_type, V):
    if cell_type == 'endo':
        a = a_endo
        b = b_endo
        g_t = g_t_endo
    elif cell_type == 'epi':
        a = a_epi
        b = b_epi
        g_t = g_t_epi
    
    # Initial values
    r0 = 0.002191519
    s0 = 0.9842542
    s_slow0 = 0.6421196

    # Time span
    t_span = (0, 100)  # Reduced time span for faster computation
    t_eval = np.linspace(0, 100, 10)  # Reduced number of points

    # Solving the differential equations
    r_solution = solve_ivp(dr_dt, t_span, [r0], args=(V,), t_eval=t_eval, method='RK45')
    s_solution = solve_ivp(ds_dt, t_span, [s0], args=(V,), t_eval=t_eval, method='RK45')
    s_slow_solution = solve_ivp(ds_slow_dt, t_span, [s_slow0], args=(V,), t_eval=t_eval, method='RK45')

    # Extract the final steady-state values
    r_steady = r_solution.y[0][-1]
    s_steady = s_solution.y[0][-1]
    s_slow_steady = s_slow_solution.y[0][-1]

    # Calculating E_K using the Nernst equation
    E_K = (R * T / F) * np.log(K_o / K_i) * 1e3

    # Compute I_t
    i_t = g_t * r_steady * (a * s_steady + b * s_slow_steady) * (V - E_K)
    return i_t

# Compute I_t for both endocardial and epicardial cells over the range of voltages
i_t_endo = np.array([compute_current('endo', v) for v in V])
i_t_epi = np.array([compute_current('epi', v) for v in V])

# Ensure that the data types are correct and plot the results
plt.figure()
plt.plot(V, i_t_endo, label='Endocardial')
plt.plot(V, i_t_epi, label='Epicardial')
plt.xlabel('Membrane Potential (mV)')
plt.ylabel('I_t (pA/pF)')
plt.title('Transient Outward Potassium Current (I_t) vs Membrane Potential')
plt.legend()
plt.show()



