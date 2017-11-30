import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
r = np.random.randn(10000) #10,000 numbers in a Gaussian dist. w/ mean 0, var 1

#Change the mean to 12 and the std. dev to 10 by scaling and shifting
B = 10.*r + 12.

#plt.hist(r,bins=100) #Histogram shows that it's indeed a Gaussian dist
plt.hist(B,bins=100) #Histogram shows that it's indeed a Gaussian dist
plt.show()
