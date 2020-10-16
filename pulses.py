import numpy as np
# import matplotlib.pyplot as plt 

def gaussian(time,t_o,w):
	g = np.exp(-0.5*((time-t_o)/w)**2)
	return g

def mod_gaussian(time,t_o,f_o,w):
	g = np.sin(2*pi*f_o*time)*np.exp(-0.5*((time-t_o)/w)**2)
	return g


