# Draw Barnsley's fernLinks to an external site. (using NumPy and matplotlib) 

import numpy as np
import matplotlib.pyplot as plt


# Antal punkter vi vill generera
n = 5000000

# Skapa arrays för att lagra alla x och y koordinater
x = np.zeros(n)
y = np.zeros(n)

# Den stora loopen som skapar ormbunken
for i in range(n-1):
    # Slumpa ett tal mellan 0 och 1
    r = np.random.random()

    # Transformation 1: stjälken (1% sannolikhet)
    if r < 0.01:
        x[i+1] = 0
        y[i+1] = 0.16 * y[i]

    # Transformation 2: de successivt mindre bladen (85% sannolikhet)
    elif r < 0.86:
        x[i+1] = 0.85 * x[i] + 0.04 * y[i]
        y[i+1] = -0.04 * x[i] + 0.85 * y[i] + 1.6

    # Transformation 3: Vänster sidoskott (7% sannolikhet)
    elif r < 0.93:
        x[i+1] = 0.2 * x[i] - 0.26 * y[i]
        y[i+1] = 0.23 * x[i] + 0.22 * y[i] + 1.6
    
    # Transformation 4: Höger sidoskott (resterande 7%)
    else:
        x[i+1] = -0.15 * x[i] + 0.28 * y[i]
        y[i+1] = 0.26 * x[i] + 0.24 * y[i] + 0.44

plt.scatter(x, y, s=0.1, color='green')
plt.title("Barnsley's Fern")
plt.savefig('fern.png')
