import numpy as np; # Importing numpy for mathematical operations
from tqdm import tqdm; # Important tqdm for progress bar.
import matplotlib.pyplot as plt; #Plotting library

def fairDice(rolls): #Fair dice roll implementation
    rolls = int(rolls); # Number of rolls should be integer.
    p = np.zeros(6,dtype=float); #Initializing array to store probability 
    cdf = np.zeros(6,dtype=float); # Storing the cdf of probability 
    u = np.random.uniform(0,1,rolls); #Generating uniform random numbers from 0 to 1
    for i in tqdm(range(rolls)):#Looping over total number of rolls
        for j in range(6): #Looping over all the dice rolls
            if (u[i]<(j+1)/6 and u[i]>= j/6):#Boning the random uniform distribution into bins.
                p[j]+=1;#If within [j/6,(j+1)/6) then add 1 to bin
    
    p /=float(rolls); #Dividing all the bins with total roll gives the probability.
    cdf[0] = p[0]; #Initializing the first value of cdf with the first probability.
    for i in range(1,6):
        cdf[i] = cdf[i-1]+p[i];# creating the cdf

    return p,cdf #Returning the probability and the cdf array.

diceRoll = fairDice(100000) #Implement the fairDice function.
print("Probability of getting 1,2, .... 6 =",diceRoll[0]);#Printing the probability 
print("CDF of dice roll getting 1,2 ... 6 =",diceRoll[1]);#Printing the cdf

x=np.linspace(1,6,6); #Generating x axis for the graph a linear array from 1 to 6
#Plotting the graph
plt.plot(x,diceRoll[0],'o');# Plotting probability.
plt.ylim(0,0.18);# Setting y axis ranging from 0 to 0.18
plt.savefig("diceProb.png",dpi=100); #Save the probability graph.
plt.clf(); #Clear plot canvas of the plot.
plt.plot(x,diceRoll[1],'o'); #Plotting cdf
plt.ylim(0,) #Starting y axis from 0
plt.savefig("diceCDF.png",dpi=100); #Save cdf plot.
