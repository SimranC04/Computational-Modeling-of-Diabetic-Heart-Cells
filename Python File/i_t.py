# python file 
import os
import sys 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import  R, T, F,g_t,E_K,K_o,K_i


def dr_dt_healthy(t, r, V):
    r_infinity = 1 / (1 + np.exp((V + 10.6) / -11.42))
    tau_r = 1 / (45.16 * np.exp(0.03577 * (V + 50)) + 98.9 * np.exp(-0.1 * (V + 38)))
    return (r_infinity - r) / tau_r

def ds_dt_healthy(t, s, V):
    s_infinity = 1 / (1 + np.exp((V + 45.3) / 6.8841))
    tau_s_endo = 0.55 * np.exp(-((V + 70) / 25)**2) + 0.049
    return (s_infinity - s) / tau_s_endo

def ds_slow_dt_healthy(t, s_slow, V):
    s_slow_infinity = 1 / (1 + np.exp((V + 45.3) / 6.8841))
    tau_s_slow_endo = 3.3 * np.exp(-((V + 70) / 30)**2) + 0.049
    return (s_slow_infinity - s_slow) / tau_s_slow_endo


def ds_dt_diabetes(t, s, V):
    s_infinity = 1 / (1 + np.exp((V + 45.3) / 6.8841))
    tau_s_endo = 0.35 * np.exp(-((V + 70) / 15)**2) + 0.035
    return (s_infinity - s) / tau_s_endo

def ds_slow_dt_diabetes(t, s_slow, V):
    s_slow_infinity = 1 / (1 + np.exp((V + 45.3) / 6.8841))
    tau_s_slow_endo = 3.7 * np.exp(-((V + 70) / 30)**2) + 0.035
    return (s_slow_infinity - s_slow) / tau_s_slow_endo


def i_t_current(V,g_t,E_K,diabetes):
    
    # Initial values
    r0 = 0.002191519
    s0 = 0.9842542
    s_slow0 = 0.6421196

    # time values
    end_time = 20
    t_span = (0, end_time)  
    t_eval = np.linspace(0, end_time, 1000) 

    # Solving
    if diabetes is True:
        g_t = 0.68 * g_t
        b = 0.31
        r_solution = solve_ivp(dr_dt_healthy, t_span, [r0], args=(V,), t_eval=t_eval, method='RK45')
        s_solution = solve_ivp(ds_dt_healthy, t_span, [s0], args=(V,), t_eval=t_eval, method='RK45')
        s_slow_solution = solve_ivp(ds_slow_dt_healthy, t_span, [s_slow0], args=(V,), t_eval=t_eval, method='RK45')
    else:
        b = 0.114
        r_solution = solve_ivp(dr_dt_healthy, t_span, [r0], args=(V,), t_eval=t_eval, method='RK45')
        s_solution = solve_ivp(ds_dt_diabetes, t_span, [s0], args=(V,), t_eval=t_eval, method='RK45')
        s_slow_solution = solve_ivp(ds_slow_dt_diabetes, t_span, [s_slow0], args=(V,), t_eval=t_eval, method='RK45')

    a = 1 - b
    # Extract the values at each time step
    r_values = r_solution.y[0]
    s_values = s_solution.y[0]
    s_slow_values = s_slow_solution.y[0]

    # Compute I_t at each time step and find the maximum value
    i_t_values = g_t * r_values * (a * s_values + b * s_slow_values) * (V - E_K)
    i_t_peak = np.max(i_t_values)
    return i_t_peak


V_range = np.linspace(-60, 60, 20)

"""
Diabetes 
"""

diabetes = False

# Initialising arrays 
i_t_peak_values = []

for V in V_range:
    i_t_peak =  i_t_current(V,g_t,E_K,diabetes)
    i_t_peak_values.append(i_t_peak)

"""
Diabetes 
"""
diabetes = True

# Initialising arrays 
i_t_peak_diabetic_values = []

# Solving 
for V in V_range:
    i_t_peak =  i_t_current(V,g_t,E_K,diabetes)
    i_t_peak_diabetic_values.append(i_t_peak)

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

# Normalising values to get current density
C = 100e-6 #microfarads
normalised_healthy_i_t = np.array(i_t_peak_values) * 1e-3 / C
normalised_diabetic_i_t = np.array(i_t_peak_diabetic_values) * 1e-3 / C

#  healthy I_t values
axs[0].plot(V_range, normalised_healthy_i_t, label='Healthy', color='blue')
axs[0].set_xlim(-80, 40)
axs[0].set_xlabel('Membrane Potential (mV)')
axs[0].set_ylabel('Peak I_t (pA/pF)')
axs[0].set_title('Healthy Cardiac Myocyte')
axs[0].legend()
axs[0].grid(True)

#  diabetic I_t values
axs[1].plot(V_range, normalised_diabetic_i_t, label='Diabetic', color='red')
axs[1].set_xlim(-80, 40)
axs[1].set_xlabel('Membrane Potential (mV)')
axs[1].set_ylabel('Peak I_t (pA/pF)')
axs[1].set_title('Diabetic Cardiac Myocyte')
axs[1].legend()
axs[1].grid(True)

# Combined plot 
plt.figure(figsize=(10, 6))
plt.plot(V_range, normalised_healthy_i_t, label='Healthy', color='blue', linestyle='--')
plt.plot(V_range, normalised_diabetic_i_t, label='Diabetic', color='red')
plt.xlim(-80, 40)
plt.xlabel('Membrane Potential (mV)')
plt.ylabel('Peak I_t (pA/pF)')
plt.title('Healthy and Diabetic Cardiac Myocyte Peak I_t')
plt.legend()
plt.grid(True)
plt.show()