import numpy as np
import matplotlib.pyplot as plt  

def gaussian(time,t_o,w):
	g = np.exp(-0.5*((time-t_o)/w)**2)
	return g

def mod_gaussian(time,t_o,f_o,w):
	g = np.sin(2*pi*f_o*time)*np.exp(-0.5*((time-t_o)/w)**2)
	return g


N_x = 200 		# number of x-cells
N_time = 100 	# number of time steps
t_o = 40  		# center of incident pulse 
w = 12 			# width of the incident pulse
time = 0.0 		# initial time = 0 seconds
init_pulse = 120 # start pulse train at 120 units
stability = 0.5 # stability condition

E_y = np.zeros(N_x) # initial condition for E_y
H_z = np.zeros(N_x) # initial condition for H_z

cell_arr = np.arange(0,N_x)

for n in range(0,N_time): # start time loop
	time = time + 1
	pulse = gaussian(time,t_o,w)
	for i in range(1,N_x): # calculate electric field 
		E_y[init_pulse-1] = pulse
		E_y[i] = E_y[i] - stability*(H_z[i] - H_z[i-1])

	for i in range(0,N_x-1): # calculate magnetic field
		H_z[i] = H_z[i] - stability*(E_y[i+1] - E_y[i])

plt.subplot(211)
plt.plot(cell_arr,E_y)
plt.subplot(212)
plt.plot(cell_arr,H_z)
plt.show()



