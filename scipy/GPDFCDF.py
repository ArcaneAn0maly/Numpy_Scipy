import numpy as np
from scipy.stats import norm
print(norm.pdf(0)) #Calculate probability of zero from a
            #standard normal distribution

#Gaussian with mean other than zero and variance other than 1
#Ex: mean = 5, standard deviation = 10 (shown below)
print(norm.pdf(0, loc=5, scale=10))

r = np.random.randn(10) #10 numbers in Gaussian dist. w/ mean=0, var=1
print(norm.pdf(r)) #Calculate the probability of the whole array

#Calculate the NATURAL log of the probability of the whole array
print(norm.logpdf(r))


#Cumulative distribution function or CDF: Integral of pdf from
#-infinite to x. Not actually solvable. Numerically evaluated.
print(norm.cdf(r))
print(norm.logcdf(r))