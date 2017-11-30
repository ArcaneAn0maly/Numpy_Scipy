import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Make a spherical Gaussian
r = np.random.randn(10000,2)

#Scale it for ellipticity and shift the center
r[:,1] = 5*r[:,1] + 2

plt.axis('equal')

#Visualize
plt.scatter(r[:,0], r[:,1])
plt.show()
