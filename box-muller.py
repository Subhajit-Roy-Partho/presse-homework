import numpy as np; # Importing numpy module used for all the mathematical operations
import matplotlib.pyplot as plt; #Importing the plotting library.
from tqdm import tqdm; #Tqdm gives the progress bar

def box_muller(mean, sigma):#Box-Muller implementation.
    u1 = np.random.uniform(0,1); #Uniform sequence generator from 0 to 1.
    u2 = np.random.uniform(0,1); #Uniform sequence generator for the second box-muller series.
    z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2) #Box-muller final formula for series 1
    z2 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2) #2nd Box muller formula.
    return mean + sigma * z1, mean + sigma * z2 # Return both the box muller results.

def multiple_box_muller(mean,sigma,number): #Multiple values generated from box muller algorithm.
    y1,y2 = np.zeros(number,dtype=float),np.zeros(number,dtype=float); #Initilizing the y1 and y2 array for holding the Normal values generated from box-muller algorithm.
    for i in tqdm(range(number)): #Looping to generating n numbers of values for normal distribution from box-muller algorithm.
        y1[i],y2[i] = box_muller(mean,sigma); #Storing the box muller values.
    return y1,y2 # Return both the box-muller Normal sequences.
mean = 0 #mean is assumed to be 1.
sigma = 1 #Sigma is assumed to be 1.
data = multiple_box_muller(mean,sigma,100000); # Generate 1e5 Normal distribution values

#Plotting the 1st distribution generated from Box-Muller algorithm.
plt.hist(data[0],density=True,bins=1000); #Plot a histogram from the 1st Box-Muller distribution.
plt.xlabel("y1 range"); # X-axis label
plt.ylabel("Frequency");# Y-axis label
plt.title("Histogram of y1 Box-Muller"); # Title of the plot.
plt.savefig("y1.png",dpi=100); #Saving the plot.
plt.show(); #Display the plot

#Plotting the 2nd distribution from the Box-Muller algorithm.
plt.hist(data[1],density=True,bins=1000); # Comments same as above.
plt.xlabel("y2 range");
plt.ylabel("Frequency");
plt.title("Histogram of y2 Box-Muller");
plt.savefig("y2.png",dpi=100);
plt.show();

#Plotting both the values together.
plt.hist(data,density=True,bins=1000);
plt.xlabel("y1 and y2 union range");
plt.ylabel("Frequency");
plt.title("Histogram of y1 and y2 combined Box-Muller");
plt.legend(["y1","y2"]);
plt.savefig("y-combined.png",dpi=100);
plt.show();