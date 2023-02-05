import random #random number generator
import numpy as np #numpy library for mathematical operation 
import matplotlib.pyplot as plt; #Plotting library 
import time; #current system time
from tqdm import tqdm; #progress bar

# time = int(time.time())
# np.random.seed(time);

# def bernoulli_draw(p):
#     # Generate a random number between 0 and 1
#     x = random.random()
    
#     # Check if the random number is less than p
#     if x < p:
#         return 1
#     else:
#         return -1

def simulate_birth_death_process(birth_rate, death_rate, s0, size): # Function for birth-death process
	if (s0<0): # making sure initial population is greater than 1
		print("Initial population must be greater than 0"); #warning message
		quit(); #terminate the program
	if (birth_rate+death_rate !=1): #p+q should be 1
		print("Birth Rate + Death Rate should be 1");# warning message
		quit(); #terminate the program
	s0 = int(s0); #confirm initial population is integer
	time = np.zeros(size,dtype="float"); #initialing time array to store the cdf of waiting time from one state to another.
	s = np.zeros(size,dtype="float");
	s[0] = s0;

	for i in tqdm(range(1,size)):
		events = np.random.choice([1, -1], size=size, p=[birth_rate / (birth_rate + s[i-1]*death_rate), s[i-1]*death_rate / (birth_rate + s[i-1]*death_rate)])
		s[i] = s[i-1] + events[i];
		if s[i] <0:
			s[i]=0;
			print("Crazy");
		time[i] = np.random.exponential(scale=1/(birth_rate + s[i-1]*death_rate),size=1);
		time[i] += time[i-1];

	return time,s;


x,y = simulate_birth_death_process(0.995,0.005,1,10000);
plot = (0.995/0.005)+(1-(0.995/0.005))*np.exp(-0.005*x);
# print(x,y);
plt.plot(x,y);
plt.plot(x,plot);
plt.xlabel("Time elapsed");
plt.ylabel("Population of RNA");
plt.title("Birt-Death Process");
plt.legend(["Simulated Process","Mass Action Law"]);
plt.ylim(0,250);
plt.savefig("plot.png",dpi=600);