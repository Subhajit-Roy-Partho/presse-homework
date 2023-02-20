# Assignment - 3

*Python is used for this assignment.*

### Q1. Stochastic binary decisions

Gillespie’s algorithm is used to solve these problem.

![A1* Population Steps 30](A1*Population-30.png)

<center><b>Fig 1: Population of A1* for 30 step simulation </b></center>

![A1* Histogram Steps 30](A1*Histogram-30.png)

<center><b>Fig 2: Histogram of A1* Population for 30 step simulation </b></center>

![A1* Population Steps 900](A1*Population-900.png)

<center><b>Fig 3: A1* Population for 900 step simulation </b></center>

![A1* Histogram Steps 9000](A1*Histogram-900.png)

<center><b>Fig 4: Histogram of A1* Population for 900 step simulation </b></center>

![All Population Steps 900](All-Population-900.png)

<center><b>Fig 5:Population of all species for 900 step simulation </b></center>

</br>

#### **Differnetial Rate Equations:**


dA1*/dt = k3.E.A1 .... [1]

dA1/dt = -k3.A1.E - A1.k5.S ..... [2]

dE/dt = k1.A1 +k4.A1* -kd.E ..... [3]

dS/dt = k2.A2 -kd.S .... [4]

Also k1=k2=k4=kd=1 and k3=100 and k5=100.

Looking at the above equation the rate of A1* is dependant upon the concentration of E and A1. Also the rate is always increasing and there is no destruction. Thus one expect a monotoneously increasing value of A1*. Also we expect a rapid growth of E at the begining as only -kd.E contribute to its destruction and should be low at the begining. Thus we expect a very large growth rate at the beginning but soon the rate is expected to drop as the concentration of A1 would deplete fast with the growth of S and E. We observe a similar situation in the grah.

Also we expect to observer a case where there is no growth of A1* if A1 decreases very rapidly. Then the concentration of E will reduce as well the A1 and we expect to observer almost no growth in the value of A1*. This is the numerical instability of the problem. Thuse we expect a constant value for the A1* or almost 0 very soon the simulation ater the begining of the simulation.

### **CASE-2**

*Very high value of A1 and A2*

![A1* Population for high A1 and A2](A1*Population-1000i1000.png)

<center><b>Fig 6: Population of A1* for very high value of A1 and A2 </b></center>

![A1* Histogram for large values of A1](A1*Histogram-1000i1000.png)

<center><b>Fig 1: Population of A1* for large population of A1 and A2 </b></center>

![All Population for large values of A1*](A1*Histogram-1000i1000.png)

<center><b>Fig 1: Population of A1* for 30 </b></center>
With a very high value of A1 in 