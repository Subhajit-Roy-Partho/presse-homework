import random
import numpy as np
import matplotlib.pyplot as plt;
import time;
from tqdm import tqdm;

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

def simulate_birth_death_process(birth_rate, death_rate, s0, size):
	if (s0<0):
		print("Initial population must be greater than 0");
		quit();
	if (birth_rate+death_rate !=1):
		print("Birth Rate + Death Rate should be 1");
		quit();
	s0 = int(s0);
	draw = 0;
	time = np.zeros(size,dtype="float");
	s = np.zeros(size,dtype="float");
	s[0] = s0;

	# events = np.random.choice([1, -1], size=size, p=[birth_rate / (birth_rate + death_rate), death_rate / (birth_rate + death_rate)])

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
plt.ylim(0,250);
plt.savefig("plot.png",dpi=600);
plt.show();
