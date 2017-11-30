#Demonstrate the central limit theorem
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

N=100

S = np.zeros(1000)

X = np.zeros(1000*N)
X = X.reshape(N,1000)

for i in range(0,N):
	X[i,:] = np.random.random(1000)
	S = S + X[i]

S = S/N

plt.hist(X[1],bins=20)
plt.hist(X[2],bins=20)
plt.hist(X[3],bins=20)
plt.hist(X[4],bins=20)
plt.hist(X[5],bins=20)
plt.hist(S,bins=20)
plt.show()
