#Sampling from a general multivariate normal distribution, where the
#dimensions are not necessarily independent from one another, which
#means that we have a full covariance matrix
import numpy as np
from scipy.stats import norm
from scipy.stats import multivariate_normal as mvn
import matplotlib.pyplot as plt

#Var = 1 (1st dimension), Variance = 3 (2nd dimension)
#Covariance between 1st and 2nd dimension = 0.8
cov = np.array([[1, 0.8],[0.8, 3]])

#These are the means of the each distribution
mu = np.array([0,2])

#Create some random variables with the specified means and
#covariances as specified above
r = mvn.rvs(mean=mu, cov=cov, size=1000)

#We can do this using numpy as well as scipy:
#r = np.random.multivariabe_normal(mean=mu, cov=cov, size=1000)

plt.scatter(r[:,0], r[:,1])

plt.axis('equal')
plt.show()