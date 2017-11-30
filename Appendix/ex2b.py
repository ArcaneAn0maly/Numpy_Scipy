#Demonstrate the central limit theorem
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

N=1000

S = np.zeros(1000*N)
S = S.reshape(N,1000)

X = np.zeros(1000*N)
X = X.reshape(N,1000)

for i in range(0,N):
	X[i,:] = np.random.random(1000)
	for j in range(i,N):
	  S[j,:] = S[j,:] + X[i]

for j in range(0,1000):
  S[j] = S[j]/(j+1)

plt.hist(X[1],bins=20)
plt.hist(X[2],bins=20)
plt.hist(X[3],bins=20)
plt.hist(X[4],bins=20)
plt.hist(X[5],bins=20)
plt.hist(S[5],bins=20)
plt.hist(S[15],bins=20)
plt.hist(S[50],bins=20)
plt.hist(S[99],bins=20)
plt.hist(S[500],bins=20)
plt.hist(S[999],bins=20)
plt.show()
