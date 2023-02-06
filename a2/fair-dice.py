import numpy as np;
from tqdm import tqdm;
import matplotlib.pyplot as plt;

def fairDice(rolls):
    rolls = int(rolls);
    p = np.zeros(6,dtype=float);
    cdf = np.zeros(6,dtype=float);
    u = np.random.uniform(0,1,rolls);
    for i in tqdm(range(rolls)):
        for j in range(6):
            if (u[i]<(j+1)/6 and u[i]>= j/6):
                p[j]+=1;
    
    p /=float(rolls);
    cdf[0] = p[0];
    for i in range(1,6):
        cdf[i] = cdf[i-1]+p[i];

    return p,cdf

diceRoll = fairDice(100000)
print("Probability of getting 1,2, .... 6 =",diceRoll[0]);
print("CDF of dice roll getting 1,2 ... 6 =",diceRoll[1]);

x=np.linspace(1,6,6);

plt.plot(x,diceRoll[0],'o');
plt.ylim(0,0.18);
plt.savefig("diceProb.png",dpi=100);
plt.clf();
plt.plot(x,diceRoll[1],'o');
plt.ylim(0,)
plt.savefig("diceCDF.png",dpi=100);
