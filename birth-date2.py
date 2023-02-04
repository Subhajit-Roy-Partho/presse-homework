import random
import numpy as np
import matplotlib.pyplot as plt;

def simulate_birth_death_process(birth_rate, death_rate, inp, size):
	if (inp>0):
		print("Initial population must be greater than 0");
		quit();
	for i in range(size):
		
	# waiting_times = np.random.exponential(scale=1 / (birth_rate + death_rate), size=int(simulation_time / (birth_rate + death_rate)))