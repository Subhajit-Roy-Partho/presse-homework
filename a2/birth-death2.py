import random #random number generator
import numpy as np #numpy library for mathematical operation 
import matplotlib.pyplot as plt; #Plotting library 
import time; #current system time
from tqdm import tqdm; #progress bar

time = int(time.time()); #calling the system time.
np.random.seed(time); # using the system time as random seed.

def bernoulli_draw(p):
    # Generate a random number between 0 and 1
    x = random.random()
    
    # Check if the random number is less than p
    if x < p:
        return 1
    else:
        return -1

def simulate_birth_death_process(birth_rate, death_rate, s0, size): # Function for birth-death process
	if (s0<0): # making sure initial population is greater than 1
		print("Initial population must be greater than 0"); #warning message
		quit(); #terminate the program
	if (birth_rate+death_rate !=1): #p+q should be 1
		print("Birth Rate + Death Rate should be 1");# warning message
		quit(); #terminate the program
	s0 = int(s0); #confirm initial population is integer
	time = np.zeros(size,dtype="float"); #initializing  time array to store the cdf of waiting time from one state to another.
	s = np.zeros(size,dtype="float"); # initializing the s array that will contain the population of RNA at different time points.
	s[0] = s0; # The 0th position is the initial value.

	for i in tqdm(range(1,size)): # Looping from 1st position to 1-size steps. TQDM is used to generate the progress bar.
		# events = np.random.choice([1, -1], size=1, p=[birth_rate / (birth_rate + s[i-1]*death_rate), s[i-1]*death_rate / (birth_rate + s[i-1]*death_rate)]); # In-built bernoulli draw.
		events = bernoulli_draw(birth_rate / (birth_rate + s[i-1]*death_rate)); # My bernoulli draw function.
		s[i] = s[i-1] + events; # Increasing or decreasing the population accourding to bernoulli draw.
		if s[i] <0: # Test case, population can't be less than 0.
			s[i]=0; # even if it goes to 0 due to some error set it to 0
			print("Crazy"); #Warning something wrong.
		time[i] = np.random.exponential(scale=1/(birth_rate + s[i-1]*death_rate),size=1); #smapling the time from an exponential distribution.
		time[i] += time[i-1]; # CDF of the time.

	return time,s; # Return the time and population array.


x,y = simulate_birth_death_process(0.995,0.005,1,10000); #Call the function.
plot = (0.995/0.005)+(1-(0.995/0.005))*np.exp(-0.005*x); # Plot the mass action law, please look into the mathematica notebook for the final formula.
# print(x,y); # Prinint x and y for debugging.
plt.plot(x,y); # Plot the time and the population array.
plt.plot(x,plot); # Plot time and the mass action law to verify our results.
plt.xlabel("Time elapsed"); # X-axis label of the plot
plt.ylabel("Population of RNA");# Y-axis label of the plot.
plt.title("Birt-Death Process"); # Plot title.
plt.legend(["Simulated Process","Mass Action Law"]); # Plot legend.
plt.savefig("plot.png",dpi=100); # Saving the plot into a file plot.png with 100 dot per inch resolution.
# plt.show(); # Would show the plot in qt window but it is not necessary.
