# Write a NumPy program to compute the mean, standard deviation,
# and variance of a given array along an axis given as a parameter.

import numpy as np

data = np.array([[10, 20, 23],
                [12, 22, 20],
                [18, 20, 26]])

print(data)

# Medelvärden längs axis 0 och 1

print("Medelvärde per kolumn (axis=0):", np.mean(data, axis=0))
print("Medelvärde per rad (axis=1):", np.mean(data, axis=1))
print()

# Variance längs axis 0 och 1

print("Varians per kolumn (axis=0):", np.var(data, axis=0))
print("Varians per rad (axis=1):", np.var(data, axis=1))
print()

# Standardavvikelse längs axis 0 och 1

print("Standardavvikelse per kolumn (axis=0):", np.std(data, axis=0))
print("Standardavvikelse per rad (axis=1):", np.std(data, axis=1))
print()