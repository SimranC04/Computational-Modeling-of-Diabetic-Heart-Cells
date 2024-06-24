# Size of variable arrays:
sizeAlgebraic = 55
sizeStates = 26
sizeConstants = 70
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_constants[0] = "R in component membrane (millijoule_per_mole_kelvin)"
    legend_constants[1] = "T in component membrane (kelvin)"
    legend_constants[2] = "F in component membrane (coulomb_per_mole)"
    legend_constants[3] = "Cm in component membrane (microF)"
    legend_algebraic[27] = "i_Na in component sodium_current (nanoA)"
    legend_algebraic[28] = "i_Ca_L in component L_type_Ca_channel (nanoA)"
    legend_algebraic[30] = "i_t in component Ca_independent_transient_outward_K_current (nanoA)"
    legend_algebraic[31] = "i_ss in component steady_state_outward_K_current (nanoA)"
    legend_algebraic[35] = "i_f in component hyperpolarisation_activated_current (nanoA)"
    legend_algebraic[32] = "i_K1 in component inward_rectifier (nanoA)"
    legend_algebraic[39] = "i_B in component background_currents (nanoA)"
    legend_algebraic[40] = "i_NaK in component sodium_potassium_pump (nanoA)"
    legend_algebraic[42] = "i_NaCa in component Na_Ca_ion_exchanger_current (nanoA)"
    legend_algebraic[41] = "i_Ca_P in component sarcolemmal_calcium_pump_current (nanoA)"
    legend_algebraic[25] = "i_Stim in component membrane (nanoA)"
    legend_algebraic[13] = "stim_period in component membrane (second)"
    legend_constants[4] = "stim_duration in component membrane (second)"
    legend_constants[5] = "stim_amplitude in component membrane (nanoA)"
    legend_algebraic[26] = "E_Na in component sodium_current (millivolt)"
    legend_constants[6] = "g_Na in component sodium_current (microS)"
    legend_constants[65] = "g_Na_endo in component sodium_current (microS)"
    legend_states[1] = "Na_i in component intracellular_ion_concentrations (millimolar)"
    legend_constants[7] = "Na_o in component standard_ionic_concentrations (millimolar)"
    legend_states[2] = "m in component sodium_current_m_gate (dimensionless)"
    legend_states[3] = "h in component sodium_current_h_gate (dimensionless)"
    legend_states[4] = "j in component sodium_current_j_gate (dimensionless)"
    legend_algebraic[0] = "m_infinity in component sodium_current_m_gate (dimensionless)"
    legend_algebraic[14] = "tau_m in component sodium_current_m_gate (second)"
    legend_algebraic[1] = "h_infinity in component sodium_current_h_gate (dimensionless)"
    legend_algebraic[15] = "tau_h in component sodium_current_h_gate (second)"
    legend_algebraic[2] = "j_infinity in component sodium_current_j_gate (dimensionless)"
    legend_algebraic[16] = "tau_j in component sodium_current_j_gate (second)"
    legend_constants[8] = "g_Ca_L in component L_type_Ca_channel (microS)"
    legend_constants[9] = "E_Ca_L in component L_type_Ca_channel (millivolt)"
    legend_states[5] = "Ca_ss in component intracellular_ion_concentrations (millimolar)"
    legend_states[6] = "d in component L_type_Ca_channel_d_gate (dimensionless)"
    legend_states[7] = "f_11 in component L_type_Ca_channel_f_11_gate (dimensionless)"
    legend_states[8] = "f_12 in component L_type_Ca_channel_f_12_gate (dimensionless)"
    legend_states[9] = "Ca_inact in component L_type_Ca_channel_Ca_inact_gate (dimensionless)"
    legend_algebraic[3] = "d_infinity in component L_type_Ca_channel_d_gate (dimensionless)"
    legend_algebraic[17] = "tau_d in component L_type_Ca_channel_d_gate (second)"
    legend_algebraic[4] = "f_11_infinity in component L_type_Ca_channel_f_11_gate (dimensionless)"
    legend_algebraic[18] = "tau_f_11 in component L_type_Ca_channel_f_11_gate (second)"
    legend_algebraic[5] = "f_12_infinity in component L_type_Ca_channel_f_12_gate (dimensionless)"
    legend_algebraic[19] = "tau_f_12 in component L_type_Ca_channel_f_12_gate (second)"
    legend_constants[10] = "tau_Ca_inact in component L_type_Ca_channel_Ca_inact_gate (second)"
    legend_algebraic[6] = "Ca_inact_infinity in component L_type_Ca_channel_Ca_inact_gate (dimensionless)"
    legend_algebraic[29] = "E_K in component Ca_independent_transient_outward_K_current (millivolt)"
    legend_constants[11] = "g_t in component Ca_independent_transient_outward_K_current (microS)"
    legend_constants[66] = "g_t_endo in component Ca_independent_transient_outward_K_current (microS)"
    legend_constants[12] = "a_endo in component Ca_independent_transient_outward_K_current (dimensionless)"
    legend_constants[13] = "b_endo in component Ca_independent_transient_outward_K_current (dimensionless)"
    legend_constants[14] = "K_o in component standard_ionic_concentrations (millimolar)"
    legend_states[10] = "K_i in component intracellular_ion_concentrations (millimolar)"
    legend_states[11] = "r in component Ca_independent_transient_outward_K_current_r_gate (dimensionless)"
    legend_states[12] = "s in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_states[13] = "s_slow in component Ca_independent_transient_outward_K_current_s_slow_gate (dimensionless)"
    legend_algebraic[20] = "tau_r in component Ca_independent_transient_outward_K_current_r_gate (second)"
    legend_algebraic[7] = "r_infinity in component Ca_independent_transient_outward_K_current_r_gate (dimensionless)"
    legend_algebraic[21] = "tau_s_endo in component Ca_independent_transient_outward_K_current_s_gate (second)"
    legend_algebraic[8] = "s_infinity in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_algebraic[22] = "tau_s_slow_endo in component Ca_independent_transient_outward_K_current_s_slow_gate (second)"
    legend_algebraic[9] = "s_slow_infinity in component Ca_independent_transient_outward_K_current_s_slow_gate (dimensionless)"
    legend_constants[15] = "g_ss in component steady_state_outward_K_current (microS)"
    legend_states[14] = "r_ss in component steady_state_outward_K_current_r_ss_gate (dimensionless)"
    legend_states[15] = "s_ss in component steady_state_outward_K_current_s_ss_gate (dimensionless)"
    legend_algebraic[23] = "tau_r_ss in component steady_state_outward_K_current_r_ss_gate (second)"
    legend_algebraic[10] = "r_ss_infinity in component steady_state_outward_K_current_r_ss_gate (dimensionless)"
    legend_constants[67] = "tau_s_ss in component steady_state_outward_K_current_s_ss_gate (second)"
    legend_algebraic[11] = "s_ss_infinity in component steady_state_outward_K_current_s_ss_gate (dimensionless)"
    legend_constants[16] = "g_K1 in component inward_rectifier (microS)"
    legend_algebraic[33] = "i_f_Na in component hyperpolarisation_activated_current (nanoA)"
    legend_algebraic[34] = "i_f_K in component hyperpolarisation_activated_current (nanoA)"
    legend_constants[17] = "g_f in component hyperpolarisation_activated_current (microS)"
    legend_constants[18] = "f_Na in component hyperpolarisation_activated_current (dimensionless)"
    legend_constants[68] = "f_K in component hyperpolarisation_activated_current (dimensionless)"
    legend_states[16] = "y in component hyperpolarisation_activated_current_y_gate (dimensionless)"
    legend_algebraic[24] = "tau_y in component hyperpolarisation_activated_current_y_gate (second)"
    legend_algebraic[12] = "y_infinity in component hyperpolarisation_activated_current_y_gate (dimensionless)"
    legend_algebraic[36] = "i_B_Na in component background_currents (nanoA)"
    legend_algebraic[37] = "i_B_Ca in component background_currents (nanoA)"
    legend_algebraic[38] = "i_B_K in component background_currents (nanoA)"
    legend_constants[19] = "g_B_Na in component background_currents (microS)"
    legend_constants[20] = "g_B_Ca in component background_currents (microS)"
    legend_constants[21] = "g_B_K in component background_currents (microS)"
    legend_constants[22] = "E_Ca in component background_currents (millivolt)"
    legend_constants[23] = "Ca_o in component standard_ionic_concentrations (millimolar)"
    legend_states[17] = "Ca_i in component intracellular_ion_concentrations (millimolar)"
    legend_constants[24] = "i_NaK_max in component sodium_potassium_pump (nanoA)"
    legend_constants[25] = "K_m_K in component sodium_potassium_pump (millimolar)"
    legend_constants[26] = "K_m_Na in component sodium_potassium_pump (millimolar)"
    legend_constants[69] = "sigma in component sodium_potassium_pump (dimensionless)"
    legend_constants[27] = "i_Ca_P_max in component sarcolemmal_calcium_pump_current (nanoA)"
    legend_constants[28] = "K_NaCa in component Na_Ca_ion_exchanger_current (nanoA_per_millimolar_4)"
    legend_constants[29] = "d_NaCa in component Na_Ca_ion_exchanger_current (millimolar_4)"
    legend_constants[30] = "gamma_NaCa in component Na_Ca_ion_exchanger_current (dimensionless)"
    legend_algebraic[43] = "J_rel in component SR_Ca_release_channel (millimolar_per_second)"
    legend_constants[31] = "v1 in component SR_Ca_release_channel (per_second)"
    legend_constants[32] = "k_a_plus in component SR_Ca_release_channel (millimolar4_per_second)"
    legend_constants[33] = "k_a_minus in component SR_Ca_release_channel (per_second)"
    legend_constants[34] = "k_b_plus in component SR_Ca_release_channel (millimolar3_per_second)"
    legend_constants[35] = "k_b_minus in component SR_Ca_release_channel (per_second)"
    legend_constants[36] = "k_c_plus in component SR_Ca_release_channel (per_second)"
    legend_constants[37] = "k_c_minus in component SR_Ca_release_channel (per_second)"
    legend_states[18] = "P_O1 in component SR_Ca_release_channel (dimensionless)"
    legend_states[19] = "P_O2 in component SR_Ca_release_channel (dimensionless)"
    legend_states[20] = "P_C1 in component SR_Ca_release_channel (dimensionless)"
    legend_states[21] = "P_C2 in component SR_Ca_release_channel (dimensionless)"
    legend_constants[38] = "n in component SR_Ca_release_channel (dimensionless)"
    legend_constants[39] = "m in component SR_Ca_release_channel (dimensionless)"
    legend_states[22] = "Ca_JSR in component intracellular_ion_concentrations (millimolar)"
    legend_algebraic[46] = "J_up in component SERCA2a_pump (millimolar_per_second)"
    legend_constants[40] = "K_fb in component SERCA2a_pump (millimolar)"
    legend_constants[41] = "K_rb in component SERCA2a_pump (millimolar)"
    legend_algebraic[44] = "fb in component SERCA2a_pump (dimensionless)"
    legend_algebraic[45] = "rb in component SERCA2a_pump (dimensionless)"
    legend_constants[42] = "Vmaxf in component SERCA2a_pump (millimolar_per_second)"
    legend_constants[43] = "Vmaxr in component SERCA2a_pump (millimolar_per_second)"
    legend_constants[44] = "K_SR in component SERCA2a_pump (dimensionless)"
    legend_constants[45] = "N_fb in component SERCA2a_pump (dimensionless)"
    legend_constants[46] = "N_rb in component SERCA2a_pump (dimensionless)"
    legend_states[23] = "Ca_NSR in component intracellular_ion_concentrations (millimolar)"
    legend_algebraic[48] = "J_tr in component intracellular_and_SR_Ca_fluxes (millimolar_per_second)"
    legend_algebraic[47] = "J_xfer in component intracellular_and_SR_Ca_fluxes (millimolar_per_second)"
    legend_algebraic[53] = "J_trpn in component intracellular_and_SR_Ca_fluxes (millimolar_per_second)"
    legend_constants[47] = "tau_tr in component intracellular_and_SR_Ca_fluxes (second)"
    legend_constants[48] = "tau_xfer in component intracellular_and_SR_Ca_fluxes (second)"
    legend_states[24] = "HTRPNCa in component intracellular_and_SR_Ca_fluxes (millimolar)"
    legend_states[25] = "LTRPNCa in component intracellular_and_SR_Ca_fluxes (millimolar)"
    legend_algebraic[49] = "J_HTRPNCa in component intracellular_and_SR_Ca_fluxes (millimolar_per_second)"
    legend_algebraic[52] = "J_LTRPNCa in component intracellular_and_SR_Ca_fluxes (millimolar_per_second)"
    legend_constants[49] = "HTRPN_tot in component intracellular_and_SR_Ca_fluxes (millimolar)"
    legend_constants[50] = "LTRPN_tot in component intracellular_and_SR_Ca_fluxes (millimolar)"
    legend_constants[51] = "k_htrpn_plus in component intracellular_and_SR_Ca_fluxes (per_millimolar_per_second)"
    legend_constants[52] = "k_htrpn_minus in component intracellular_and_SR_Ca_fluxes (per_second)"
    legend_constants[53] = "k_ltrpn_plus in component intracellular_and_SR_Ca_fluxes (per_millimolar_per_second)"
    legend_constants[54] = "k_ltrpn_minus in component intracellular_and_SR_Ca_fluxes (per_second)"
    legend_constants[55] = "V_myo in component intracellular_ion_concentrations (micro_litre)"
    legend_constants[56] = "V_JSR in component intracellular_ion_concentrations (micro_litre)"
    legend_constants[57] = "V_NSR in component intracellular_ion_concentrations (micro_litre)"
    legend_constants[58] = "V_SS in component intracellular_ion_concentrations (micro_litre)"
    legend_constants[59] = "K_mCMDN in component intracellular_ion_concentrations (millimolar)"
    legend_constants[60] = "K_mCSQN in component intracellular_ion_concentrations (millimolar)"
    legend_constants[61] = "K_mEGTA in component intracellular_ion_concentrations (millimolar)"
    legend_constants[62] = "CMDN_tot in component intracellular_ion_concentrations (millimolar)"
    legend_constants[63] = "CSQN_tot in component intracellular_ion_concentrations (millimolar)"
    legend_constants[64] = "EGTA_tot in component intracellular_ion_concentrations (millimolar)"
    legend_algebraic[54] = "beta_i in component intracellular_ion_concentrations (dimensionless)"
    legend_algebraic[50] = "beta_SS in component intracellular_ion_concentrations (dimensionless)"
    legend_algebraic[51] = "beta_JSR in component intracellular_ion_concentrations (dimensionless)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[2] = "d/dt m in component sodium_current_m_gate (dimensionless)"
    legend_rates[3] = "d/dt h in component sodium_current_h_gate (dimensionless)"
    legend_rates[4] = "d/dt j in component sodium_current_j_gate (dimensionless)"
    legend_rates[6] = "d/dt d in component L_type_Ca_channel_d_gate (dimensionless)"
    legend_rates[7] = "d/dt f_11 in component L_type_Ca_channel_f_11_gate (dimensionless)"
    legend_rates[8] = "d/dt f_12 in component L_type_Ca_channel_f_12_gate (dimensionless)"
    legend_rates[9] = "d/dt Ca_inact in component L_type_Ca_channel_Ca_inact_gate (dimensionless)"
    legend_rates[11] = "d/dt r in component Ca_independent_transient_outward_K_current_r_gate (dimensionless)"
    legend_rates[12] = "d/dt s in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_rates[13] = "d/dt s_slow in component Ca_independent_transient_outward_K_current_s_slow_gate (dimensionless)"
    legend_rates[14] = "d/dt r_ss in component steady_state_outward_K_current_r_ss_gate (dimensionless)"
    legend_rates[15] = "d/dt s_ss in component steady_state_outward_K_current_s_ss_gate (dimensionless)"
    legend_rates[16] = "d/dt y in component hyperpolarisation_activated_current_y_gate (dimensionless)"
    legend_rates[20] = "d/dt P_C1 in component SR_Ca_release_channel (dimensionless)"
    legend_rates[18] = "d/dt P_O1 in component SR_Ca_release_channel (dimensionless)"
    legend_rates[19] = "d/dt P_O2 in component SR_Ca_release_channel (dimensionless)"
    legend_rates[21] = "d/dt P_C2 in component SR_Ca_release_channel (dimensionless)"
    legend_rates[24] = "d/dt HTRPNCa in component intracellular_and_SR_Ca_fluxes (millimolar)"
    legend_rates[25] = "d/dt LTRPNCa in component intracellular_and_SR_Ca_fluxes (millimolar)"
    legend_rates[17] = "d/dt Ca_i in component intracellular_ion_concentrations (millimolar)"
    legend_rates[1] = "d/dt Na_i in component intracellular_ion_concentrations (millimolar)"
    legend_rates[10] = "d/dt K_i in component intracellular_ion_concentrations (millimolar)"
    legend_rates[5] = "d/dt Ca_ss in component intracellular_ion_concentrations (millimolar)"
    legend_rates[22] = "d/dt Ca_JSR in component intracellular_ion_concentrations (millimolar)"
    legend_rates[23] = "d/dt Ca_NSR in component intracellular_ion_concentrations (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -80.50146
    constants[0] = 8314.5
    constants[1] = 295
    constants[2] = 96487
    constants[3] = 0.0001
    constants[4] = 5e-3
    constants[5] = -0.6
    constants[6] = 0.8
    states[1] = 10.73519
    constants[7] = 140
    states[2] = 0.004164108
    states[3] = 0.6735613
    states[4] = 0.6729362
    constants[8] = 0.031
    constants[9] = 65
    states[5] = 0.00008737212
    states[6] = 0.000002171081
    states[7] = 0.9999529
    states[8] = 0.9999529
    states[9] = 0.9913102
    constants[10] = 0.009
    constants[11] = 0.035
    constants[12] = 0.583
    constants[13] = 0.417
    constants[14] = 5.4
    states[10] = 139.2751
    states[11] = 0.002191519
    states[12] = 0.9842542
    states[13] = 0.6421196
    constants[15] = 0.007
    states[14] = 0.002907171
    states[15] = 0.3142767
    constants[16] = 0.024
    constants[17] = 0.00145
    constants[18] = 0.2
    states[16] = 0.003578708
    constants[19] = 0.00008015
    constants[20] = 0.0000324
    constants[21] = 0.000138
    constants[22] = 65
    constants[23] = 1.2
    states[17] = 0.00007901351
    constants[24] = 0.08
    constants[25] = 1.5
    constants[26] = 10
    constants[27] = 0.004
    constants[28] = 0.000009984
    constants[29] = 0.0001
    constants[30] = 0.5
    constants[31] = 1.8e3
    constants[32] = 12.15e12
    constants[33] = 576
    constants[34] = 4.05e9
    constants[35] = 1930
    constants[36] = 100
    constants[37] = 0.8
    states[18] = 0.0004327548
    states[19] = 0.000000000606254
    states[20] = 0.6348229
    states[21] = 0.3647471
    constants[38] = 4
    constants[39] = 3
    states[22] = 0.06607948
    constants[40] = 0.000168
    constants[41] = 3.29
    constants[42] = 0.04
    constants[43] = 0.9
    constants[44] = 1
    constants[45] = 1.2
    constants[46] = 1
    states[23] = 0.06600742
    constants[47] = 0.0005747
    constants[48] = 0.0267
    states[24] = 1.394301e-1
    states[25] = 5.1619e-3
    constants[49] = 0.14
    constants[50] = 0.07
    constants[51] = 200000
    constants[52] = 0.066
    constants[53] = 40000
    constants[54] = 40
    constants[55] = 9.36e-6
    constants[56] = 0.056e-6
    constants[57] = 0.504e-6
    constants[58] = 1.2e-9
    constants[59] = 0.00238
    constants[60] = 0.8
    constants[61] = 0.00015
    constants[62] = 0.05
    constants[63] = 15
    constants[64] = 10
    constants[65] = 1.33000*constants[6]
    constants[66] = 0.464700*constants[11]
    constants[67] = 2.10000
    constants[68] = 1.00000-constants[18]
    constants[69] = (exp(constants[7]/67.3000)-1.00000)/7.00000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[20] = -constants[32]*(power(states[5], constants[38]))*states[20]+constants[33]*states[18]
    rates[18] = (constants[32]*(power(states[5], constants[38]))*states[20]-(constants[33]*states[18]+constants[34]*(power(states[5], constants[39]))*states[18]+constants[36]*states[18]))+constants[35]*states[19]+constants[37]*states[21]
    rates[19] = constants[34]*(power(states[5], constants[39]))*states[18]-constants[35]*states[19]
    rates[21] = constants[36]*states[18]-constants[37]*states[21]
    algebraic[6] = 1.00000/(1.00000+states[5]/0.0100000)
    rates[9] = (algebraic[6]-states[9])/constants[10]
    algebraic[11] = 1.00000/(1.00000+exp((states[0]+87.5000)/10.3000))
    rates[15] = (algebraic[11]-states[15])/constants[67]
    algebraic[0] = 1.00000/(1.00000+exp((states[0]+45.0000)/-6.50000))
    algebraic[14] = 0.00136000/((0.320000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))+0.0800000*exp(-states[0]/11.0000))
    rates[2] = (algebraic[0]-states[2])/algebraic[14]
    algebraic[1] = 1.00000/(1.00000+exp((states[0]+76.1000)/6.07000))
    algebraic[15] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.000453700*(1.00000+exp(-(states[0]+10.6600)/11.1000)) , True, 0.00349000/(0.135000*exp(-(states[0]+80.0000)/6.80000)+3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]))])
    rates[3] = (algebraic[1]-states[3])/algebraic[15]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+76.1000)/6.07000))
    algebraic[16] = custom_piecewise([greater_equal(states[0] , -40.0000), (0.0116300*(1.00000+exp(-0.100000*(states[0]+32.0000))))/exp(-2.53500e-07*states[0]) , True, 0.00349000/(((states[0]+37.7800)/(1.00000+exp(0.311000*(states[0]+79.2300))))*(-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))+(0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))))])
    rates[4] = (algebraic[2]-states[4])/algebraic[16]
    algebraic[3] = 1.00000/(1.00000+exp((states[0]+15.3000)/-5.00000))
    algebraic[17] = 0.00305000*exp(-0.00450000*(power(states[0]+7.00000, 2.00000)))+0.00105000*exp(-0.00200000*(power(states[0]-18.0000, 2.00000)))+0.000250000
    rates[6] = (algebraic[3]-states[6])/algebraic[17]
    algebraic[4] = 1.00000/(1.00000+exp((states[0]+26.7000)/5.40000))
    algebraic[18] = 0.105000*exp(-(power((states[0]+45.0000)/12.0000, 2.00000)))+0.0400000/(1.00000+exp((-states[0]+25.0000)/25.0000))+0.0150000/(1.00000+exp((states[0]+75.0000)/25.0000))+0.00170000
    rates[7] = (algebraic[4]-states[7])/algebraic[18]
    algebraic[5] = 1.00000/(1.00000+exp((states[0]+26.7000)/5.40000))
    algebraic[19] = 0.0410000*exp(-(power((states[0]+47.0000)/12.0000, 2.00000)))+0.0800000/(1.00000+exp((states[0]+55.0000)/-5.00000))+0.0150000/(1.00000+exp((states[0]+75.0000)/25.0000))+0.00170000
    rates[8] = (algebraic[5]-states[8])/algebraic[19]
    algebraic[20] = 1.00000/(45.1600*exp(0.0357700*(states[0]+50.0000))+98.9000*exp(-0.100000*(states[0]+38.0000)))
    algebraic[7] = 1.00000/(1.00000+exp((states[0]+10.6000)/-11.4200))
    rates[11] = (algebraic[7]-states[11])/algebraic[20]
    algebraic[21] = 0.550000*exp(-(power((states[0]+70.0000)/25.0000, 2.00000)))+0.0490000
    algebraic[8] = 1.00000/(1.00000+exp((states[0]+45.3000)/6.88410))
    rates[12] = (algebraic[8]-states[12])/algebraic[21]
    algebraic[22] = 3.30000*exp(((-(states[0]+70.0000)/30.0000)*(states[0]+70.0000))/30.0000)+0.0490000
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+45.3000)/6.88410))
    rates[13] = (algebraic[9]-states[13])/algebraic[22]
    algebraic[23] = 10.0000/(45.1600*exp(0.0357700*(states[0]+50.0000))+98.9000*exp(-0.100000*(states[0]+38.0000)))
    algebraic[10] = 1.00000/(1.00000+exp((states[0]+11.5000)/-11.8200))
    rates[14] = (algebraic[10]-states[14])/algebraic[23]
    algebraic[24] = 1.00000/(0.118850*exp((states[0]+80.0000)/28.3700)+0.562300*exp((states[0]+80.0000)/-14.1900))
    algebraic[12] = 1.00000/(1.00000+exp((states[0]+138.600)/10.4800))
    rates[16] = (algebraic[12]-states[16])/algebraic[24]
    algebraic[29] = ((constants[0]*constants[1])/constants[2])*log(constants[14]/states[10])
    algebraic[30] = constants[66]*states[11]*(constants[12]*states[12]+constants[13]*states[13])*(states[0]-algebraic[29])
    algebraic[31] = constants[15]*states[14]*states[15]*(states[0]-algebraic[29])
    algebraic[32] = ((48.0000/(exp((states[0]+37.0000)/25.0000)+exp((states[0]+37.0000)/-25.0000))+10.0000)*0.00100000)/(1.00000+exp((states[0]-(algebraic[29]+76.7700))/-17.0000))+(constants[16]*(states[0]-(algebraic[29]+1.73000)))/((1.00000+exp((1.61300*constants[2]*(states[0]-(algebraic[29]+1.73000)))/(constants[0]*constants[1])))*(1.00000+exp((constants[14]-0.998800)/-0.124000)))
    algebraic[40] = (((((constants[24]*1.00000)/(1.00000+0.124500*exp((-0.100000*states[0]*constants[2])/(constants[0]*constants[1]))+0.0365000*constants[69]*exp((-states[0]*constants[2])/(constants[0]*constants[1]))))*constants[14])/(constants[14]+constants[25]))*1.00000)/(1.00000+power(constants[26]/states[1], 1.50000))
    algebraic[13] = custom_piecewise([greater_equal(voi , 5.00000) & less_equal(voi , 10.0000), 1.00000 , True, 1.00000])
    algebraic[25] = custom_piecewise([greater_equal(voi-floor(voi/algebraic[13])*algebraic[13] , 0.0200000) & less_equal(voi-floor(voi/algebraic[13])*algebraic[13] , constants[4]+0.0200000), constants[5] , True, 0.00000])
    algebraic[34] = constants[17]*states[16]*constants[68]*(states[0]-algebraic[29])
    algebraic[38] = constants[21]*(states[0]-algebraic[29])
    rates[10] = (-(algebraic[25]+algebraic[31]+algebraic[38]+algebraic[30]+algebraic[32]+algebraic[34]+algebraic[40]*-2.00000)*1.00000)/(constants[55]*constants[2])
    algebraic[26] = ((constants[0]*constants[1])/constants[2])*log(constants[7]/states[1])
    algebraic[27] = constants[65]*(power(states[2], 3.00000))*states[3]*states[4]*(states[0]-algebraic[26])
    algebraic[28] = constants[8]*states[6]*((0.900000+states[9]/10.0000)*states[7]+(0.100000-states[9]/10.0000)*states[8])*(states[0]-constants[9])
    algebraic[33] = constants[17]*states[16]*constants[18]*(states[0]-algebraic[26])
    algebraic[35] = algebraic[33]+algebraic[34]
    algebraic[36] = constants[19]*(states[0]-algebraic[26])
    algebraic[37] = constants[20]*(states[0]-constants[22])
    algebraic[39] = algebraic[36]+algebraic[37]+algebraic[38]
    algebraic[42] = (constants[28]*((power(states[1], 3.00000))*constants[23]*exp(0.0374300*states[0]*constants[30])-(power(constants[7], 3.00000))*states[17]*exp(0.0374300*states[0]*(constants[30]-1.00000))))/(1.00000+constants[29]*(states[17]*(power(constants[7], 3.00000))+constants[23]*(power(states[1], 3.00000))))
    algebraic[41] = (constants[27]*states[17])/(states[17]+0.000400000)
    rates[0] = -(algebraic[27]+algebraic[28]+algebraic[30]+algebraic[31]+algebraic[35]+algebraic[32]+algebraic[39]+algebraic[40]+algebraic[42]+algebraic[41]+algebraic[25])/constants[3]
    rates[1] = (-(algebraic[27]+algebraic[36]+algebraic[42]*3.00000+algebraic[40]*3.00000+algebraic[33])*1.00000)/(constants[55]*constants[2])
    algebraic[44] = power(states[17]/constants[40], constants[45])
    algebraic[45] = power(states[23]/constants[41], constants[46])
    algebraic[46] = (constants[44]*(constants[42]*algebraic[44]-constants[43]*algebraic[45]))/(1.00000+algebraic[44]+algebraic[45])
    algebraic[48] = (states[23]-states[22])/constants[47]
    rates[23] = (algebraic[46]*constants[55])/constants[57]-(algebraic[48]*constants[56])/constants[57]
    algebraic[49] = constants[51]*states[17]*(constants[49]-states[24])-constants[52]*states[24]
    rates[24] = algebraic[49]
    algebraic[43] = constants[31]*(states[18]+states[19])*(states[22]-states[5])
    algebraic[47] = (states[5]-states[17])/constants[48]
    algebraic[50] = 1.00000/(1.00000+(constants[62]*constants[59])/(power(constants[59]+states[5], 2.00000)))
    rates[5] = algebraic[50]*(((algebraic[43]*constants[56])/constants[58]-(algebraic[47]*constants[55])/constants[58])-(algebraic[28]*1.00000)/(2.00000*constants[58]*constants[2]))
    algebraic[51] = 1.00000/(1.00000+(constants[63]*constants[60])/(power(constants[60]+states[22], 2.00000)))
    rates[22] = algebraic[51]*(algebraic[48]-algebraic[43])
    algebraic[52] = constants[53]*states[17]*(constants[50]-states[25])-constants[54]*states[25]
    rates[25] = algebraic[52]
    algebraic[53] = algebraic[49]+algebraic[52]
    algebraic[54] = 1.00000/(1.00000+(constants[62]*constants[59])/(power(constants[59]+states[17], 2.00000))+(constants[64]*constants[61])/(power(constants[61]+states[17], 2.00000)))
    rates[17] = algebraic[54]*(algebraic[47]-(algebraic[46]+algebraic[53]+(((algebraic[37]-2.00000*algebraic[42])+algebraic[41])*1.00000)/(2.00000*constants[55]*constants[2])))
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[6] = 1.00000/(1.00000+states[5]/0.0100000)
    algebraic[11] = 1.00000/(1.00000+exp((states[0]+87.5000)/10.3000))
    algebraic[0] = 1.00000/(1.00000+exp((states[0]+45.0000)/-6.50000))
    algebraic[14] = 0.00136000/((0.320000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))+0.0800000*exp(-states[0]/11.0000))
    algebraic[1] = 1.00000/(1.00000+exp((states[0]+76.1000)/6.07000))
    algebraic[15] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.000453700*(1.00000+exp(-(states[0]+10.6600)/11.1000)) , True, 0.00349000/(0.135000*exp(-(states[0]+80.0000)/6.80000)+3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]))])
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+76.1000)/6.07000))
    algebraic[16] = custom_piecewise([greater_equal(states[0] , -40.0000), (0.0116300*(1.00000+exp(-0.100000*(states[0]+32.0000))))/exp(-2.53500e-07*states[0]) , True, 0.00349000/(((states[0]+37.7800)/(1.00000+exp(0.311000*(states[0]+79.2300))))*(-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))+(0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))))])
    algebraic[3] = 1.00000/(1.00000+exp((states[0]+15.3000)/-5.00000))
    algebraic[17] = 0.00305000*exp(-0.00450000*(power(states[0]+7.00000, 2.00000)))+0.00105000*exp(-0.00200000*(power(states[0]-18.0000, 2.00000)))+0.000250000
    algebraic[4] = 1.00000/(1.00000+exp((states[0]+26.7000)/5.40000))
    algebraic[18] = 0.105000*exp(-(power((states[0]+45.0000)/12.0000, 2.00000)))+0.0400000/(1.00000+exp((-states[0]+25.0000)/25.0000))+0.0150000/(1.00000+exp((states[0]+75.0000)/25.0000))+0.00170000
    algebraic[5] = 1.00000/(1.00000+exp((states[0]+26.7000)/5.40000))
    algebraic[19] = 0.0410000*exp(-(power((states[0]+47.0000)/12.0000, 2.00000)))+0.0800000/(1.00000+exp((states[0]+55.0000)/-5.00000))+0.0150000/(1.00000+exp((states[0]+75.0000)/25.0000))+0.00170000
    algebraic[20] = 1.00000/(45.1600*exp(0.0357700*(states[0]+50.0000))+98.9000*exp(-0.100000*(states[0]+38.0000)))
    algebraic[7] = 1.00000/(1.00000+exp((states[0]+10.6000)/-11.4200))
    algebraic[21] = 0.550000*exp(-(power((states[0]+70.0000)/25.0000, 2.00000)))+0.0490000
    algebraic[8] = 1.00000/(1.00000+exp((states[0]+45.3000)/6.88410))
    algebraic[22] = 3.30000*exp(((-(states[0]+70.0000)/30.0000)*(states[0]+70.0000))/30.0000)+0.0490000
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+45.3000)/6.88410))
    algebraic[23] = 10.0000/(45.1600*exp(0.0357700*(states[0]+50.0000))+98.9000*exp(-0.100000*(states[0]+38.0000)))
    algebraic[10] = 1.00000/(1.00000+exp((states[0]+11.5000)/-11.8200))
    algebraic[24] = 1.00000/(0.118850*exp((states[0]+80.0000)/28.3700)+0.562300*exp((states[0]+80.0000)/-14.1900))
    algebraic[12] = 1.00000/(1.00000+exp((states[0]+138.600)/10.4800))
    algebraic[29] = ((constants[0]*constants[1])/constants[2])*log(constants[14]/states[10])
    algebraic[30] = constants[66]*states[11]*(constants[12]*states[12]+constants[13]*states[13])*(states[0]-algebraic[29])
    algebraic[31] = constants[15]*states[14]*states[15]*(states[0]-algebraic[29])
    algebraic[32] = ((48.0000/(exp((states[0]+37.0000)/25.0000)+exp((states[0]+37.0000)/-25.0000))+10.0000)*0.00100000)/(1.00000+exp((states[0]-(algebraic[29]+76.7700))/-17.0000))+(constants[16]*(states[0]-(algebraic[29]+1.73000)))/((1.00000+exp((1.61300*constants[2]*(states[0]-(algebraic[29]+1.73000)))/(constants[0]*constants[1])))*(1.00000+exp((constants[14]-0.998800)/-0.124000)))
    algebraic[40] = (((((constants[24]*1.00000)/(1.00000+0.124500*exp((-0.100000*states[0]*constants[2])/(constants[0]*constants[1]))+0.0365000*constants[69]*exp((-states[0]*constants[2])/(constants[0]*constants[1]))))*constants[14])/(constants[14]+constants[25]))*1.00000)/(1.00000+power(constants[26]/states[1], 1.50000))
    algebraic[13] = custom_piecewise([greater_equal(voi , 5.00000) & less_equal(voi , 10.0000), 1.00000 , True, 1.00000])
    algebraic[25] = custom_piecewise([greater_equal(voi-floor(voi/algebraic[13])*algebraic[13] , 0.0200000) & less_equal(voi-floor(voi/algebraic[13])*algebraic[13] , constants[4]+0.0200000), constants[5] , True, 0.00000])
    algebraic[34] = constants[17]*states[16]*constants[68]*(states[0]-algebraic[29])
    algebraic[38] = constants[21]*(states[0]-algebraic[29])
    algebraic[26] = ((constants[0]*constants[1])/constants[2])*log(constants[7]/states[1])
    algebraic[27] = constants[65]*(power(states[2], 3.00000))*states[3]*states[4]*(states[0]-algebraic[26])
    algebraic[28] = constants[8]*states[6]*((0.900000+states[9]/10.0000)*states[7]+(0.100000-states[9]/10.0000)*states[8])*(states[0]-constants[9])
    algebraic[33] = constants[17]*states[16]*constants[18]*(states[0]-algebraic[26])
    algebraic[35] = algebraic[33]+algebraic[34]
    algebraic[36] = constants[19]*(states[0]-algebraic[26])
    algebraic[37] = constants[20]*(states[0]-constants[22])
    algebraic[39] = algebraic[36]+algebraic[37]+algebraic[38]
    algebraic[42] = (constants[28]*((power(states[1], 3.00000))*constants[23]*exp(0.0374300*states[0]*constants[30])-(power(constants[7], 3.00000))*states[17]*exp(0.0374300*states[0]*(constants[30]-1.00000))))/(1.00000+constants[29]*(states[17]*(power(constants[7], 3.00000))+constants[23]*(power(states[1], 3.00000))))
    algebraic[41] = (constants[27]*states[17])/(states[17]+0.000400000)
    algebraic[44] = power(states[17]/constants[40], constants[45])
    algebraic[45] = power(states[23]/constants[41], constants[46])
    algebraic[46] = (constants[44]*(constants[42]*algebraic[44]-constants[43]*algebraic[45]))/(1.00000+algebraic[44]+algebraic[45])
    algebraic[48] = (states[23]-states[22])/constants[47]
    algebraic[49] = constants[51]*states[17]*(constants[49]-states[24])-constants[52]*states[24]
    algebraic[43] = constants[31]*(states[18]+states[19])*(states[22]-states[5])
    algebraic[47] = (states[5]-states[17])/constants[48]
    algebraic[50] = 1.00000/(1.00000+(constants[62]*constants[59])/(power(constants[59]+states[5], 2.00000)))
    algebraic[51] = 1.00000/(1.00000+(constants[63]*constants[60])/(power(constants[60]+states[22], 2.00000)))
    algebraic[52] = constants[53]*states[17]*(constants[50]-states[25])-constants[54]*states[25]
    algebraic[53] = algebraic[49]+algebraic[52]
    algebraic[54] = 1.00000/(1.00000+(constants[62]*constants[59])/(power(constants[59]+states[17], 2.00000))+(constants[64]*constants[61])/(power(constants[61]+states[17], 2.00000)))
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

def solve_model():
    """Solve model with ODE solver"""
    from scipy.integrate import ode
    # Initialise constants and state variables
    (init_states, constants) = initConsts()

    # Set timespan to solve over
    voi = linspace(0, 10, 500)

    # Construct ODE object to solve
    r = ode(computeRates)
    r.set_integrator('vode', method='bdf', atol=1e-06, rtol=1e-06, max_step=1)
    r.set_initial_value(init_states, voi[0])
    r.set_f_params(constants)

    # Solve model
    states = array([[0.0] * len(voi)] * sizeStates)
    states[:,0] = init_states
    for (i,t) in enumerate(voi[1:]):
        if r.successful():
            r.integrate(t)
            states[:,i+1] = r.y
        else:
            break

    # Compute algebraic variables
    algebraic = computeAlgebraic(constants, states, voi)
    return (voi, states, algebraic)

def plot_model(voi, states, algebraic):
    """Plot variables against variable of integration"""
    import pylab
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()
    pylab.figure(1)
    pylab.plot(voi,vstack((states,algebraic)).T)
    pylab.xlabel(legend_voi)
    pylab.legend(legend_states + legend_algebraic, loc='best')
    pylab.show()

if __name__ == "__main__":
    (voi, states, algebraic) = solve_model()
    plot_model(voi, states, algebraic)
