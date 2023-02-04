import random
import numpy as np
import matplotlib.pyplot as plt;

def simulate_birth_death_process(birth_rate, death_rate, initial_population, simulation_time):
    # Generate a sequence of exponentially distributed waiting times
    waiting_times = np.random.exponential(scale=1 / (birth_rate + death_rate), size=int(simulation_time / (birth_rate + death_rate)))
    waiting_times = np.cumsum(waiting_times)
    waiting_times = np.insert(waiting_times, 0, 0)
    
    # Generate a sequence of events (birth or death)
    events = np.random.choice([1, -1], size=len(waiting_times), p=[birth_rate / (birth_rate + death_rate), death_rate / (birth_rate + death_rate)])
    
    # Compute the population size over time
    population = np.cumsum(events) + initial_population
    population = np.insert(population, 0, initial_population)
    
    # Return the simulation results
    return waiting_times, population

x,y=simulate_birth_death_process(0.45,0.2,1,100);
print(x.shape)
print(y.shape)
plt.plot(x,y[:-1])
plt.savefig("plot.png",dpi=600)
plt.show();