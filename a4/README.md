# Assignment 4

I have used the following simplification:

- y_2n = 1-y_1n
- pi_1 = sum(y_1n)/sum(y_1n+y_2n) 
= sum(y_1n)/sum(y_1n+1-y_1n)
=sum(y_1n)/n
- Took my initial guess of mu as mean of the data generated for faster convergence.
- Similarly took the initial variance as the variance of the data.

Sample output:


True Parameters: pi_1 = 0.7, mu_1 = 1.0, mu_2 = 4.0, v = 0.5

Estimated Parameters: pi_1 = 0.7036487636639586, mu_1 = 1.0110600112242416, mu_2 = 4.02350646764783, v = 0.5017586475461915

%Error in estimation : pi_1 =0.5212519519940871 %, mu_1 = 1.1060011224241606 %, mu_2 = 0.5876616911957511 %, v =0.3517295092382966 %
