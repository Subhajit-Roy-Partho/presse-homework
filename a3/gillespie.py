import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from time import time;
# Initial states.

np.random.seed(int(time()));
# c is the initial populations.
populations = np.array((1000,1000,0,0,0),dtype=int); # Ip = [A1,A2,A1*,E,S]
# rate is the initial rates
rates = np.array((1,1,100,1,100,1),dtype=float); # rates = [k1,k2,k3,k4,k5,kd]

# populations = np.zeros(5,dtype=int) # keeps track of nth population.
propensities = np.zeros(7,dtype=float) #keeps track of nth propensities

steps = 1000;

time = np.zeros(steps, dtype=float); # Store the time steps
storeP = np.zeros((steps,5),dtype=int); # Store all the populations at all time steps in 2D array.
storeP[0] = populations; #Store the initial population at step 0 
# Defining propensities
def prop(populations,propensities):
    propensities[0] = populations[0]*rates[0]; # A1 -> E + A1 (k1)
    propensities[1] = populations[1]*rates[1]; # A2 -> S + A2 (k2)
    propensities[2] = populations[3]*populations[0]*rates[2]; # E + A1 -> E + A1* (k3)
    propensities[3] = populations[2]*rates[3]; # A1* -> E + A1* (k4)
    propensities[4] = populations[4]*populations[0]*rates[4]; # S + A1 -> S + (-A1) (k5)
    propensities[5] = populations[4]*rates[5]; # S -> (-S) (kd)
    propensities[6] = populations[3]*rates[5]; # E -> (-E) (kd)
    return propensities

def reactions(populations,choice):
    if choice == 0: #For A1 -> E + A1 (k1)
        populations[3] +=1; # Only E increases
    if choice == 1 : # For A2 -> S + A2 (k2)
        populations[4] +=1; # Only S increases
    if choice == 2: # For E + A1 -> E + A1* (k3)
        populations[0] -=1; #A1 decreases
        populations[2] +=1; # A1* increases
        # E stayes the same.
    if choice == 3: #For A1* -> E + A1* (k4)
        populations[3] += 1; #Only E increases
    if choice == 4: # For S + A1 -> S + (-A1) (k5)
        populations[0] -=1; #Only A1 decreases as A1 is inactivated
    if choice == 5: # For S -> (-S) (kd)
        populations[4] -=1; # Only S decreases
    if choice == 6: #For E -> (-E) (kd)
        populations[3] -=1; #Only E decreases
    return populations


for i in tqdm(range(1,steps)): # Loop i will range from 1 to steps-1
    propensities = prop(populations,propensities); #Calculate propensities for all the reactions
    sumProp = np.sum(propensities); # sum of all the 
    maxTime = 1.0/sumProp; # Maximum time.
    tau = np.random.exponential(maxTime); # Holding time sampled from an exponential distribution.
    choice = np.random.choice(7,1,p=propensities/sumProp); # Making choice for the reaction to be evaluated
    populations = reactions(populations,choice); # Update the population based on the choice made above.
    time[i] = time[i-1]+tau; #Store the time.
    storeP[i]=populations#Store all the populations at step i

storeP = storeP.transpose();
plt.plot(time,storeP[2]);
plt.title("Gillespie Simulation")
plt.xlabel("Time");
plt.ylabel("Population");
plt.legend("A1*");
plt.savefig("A1*Population-"+str(steps)+"i1000.png",dpi=100)
plt.clf();
plt.hist(storeP[2],bins=50);
plt.xlabel("Population");
plt.ylabel("Number");
plt.title("A1* Histogram")
plt.savefig("A1*Histogram-"+str(steps)+"i1000.png",dpi=100)
plt.clf();

for i in range(5):
    plt.plot(time,storeP[i]);
plt.title("Gillespie Simulation");
plt.xlabel("Time");
plt.ylabel("Population");
plt.legend(["A1","A2","A1*","E","S"])
plt.savefig("All Population-"+str(steps)+"i1000.png",dpi=100)
plt.clf()