import numpy as np
import matplotlib.pyplot as plt

# Define the rate constants and initial molecule counts
k1 = 0.1
k2 = 0.2
A0 = 100
B0 = 0
C0 = 0

# Define the propensity functions for the reactions
def prop_func_1(A, B, C):
    return k1 * A * B

def prop_func_2(A, B, C):
    return k2 * C

# Set the initial time and molecule counts
t = 0
A = A0
B = B0
C = C0

# Create empty lists to store the time and molecule counts
time_points = [t]
A_counts = [A]
B_counts = [B]
C_counts = [C]

# Run the Gillespie algorithm
while t < 50:
    a1 = prop_func_1(A, B, C)
    a2 = prop_func_2(A, B, C)
    a0 = a1 + a2
    tau = np.random.exponential(1/a0)
    reaction_choice = np.random.choice([1, 2], p=[a1/a0, a2/a0])
    if reaction_choice == 1:
        A -= 1
        B -= 1
        C += 1
    else:
        A += 1
        B += 1
        C -= 1
    t += tau
    time_points.append(t)
    A_counts.append(A)
    B_counts.append(B)
    C_counts.append(C)

# Plot the results
plt.plot(time_points, A_counts, label="A")
plt.plot(time_points, B_counts, label="B")
plt.plot(time_points, C_counts, label="C")
plt.xlabel("Time")
plt.ylabel("Molecule Count")
plt.legend()
plt.show()
