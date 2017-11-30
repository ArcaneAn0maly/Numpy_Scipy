import numpy as np
import pandas as pd
X = pd.read_csv('data_2d.csv',header=None)
print(type(X))
print(X.info()) #Show info about the data frame
print(X.head()) #Show first few rows of data frame

M = X.as_matrix() #Converts to numpy array
print(type(M))
print(type(X[0])) #Prints data type of column zero of X
print(X.ix[0]) #Prints the 0th row of X
print(X.iloc[0]) #Prints the 0th row of X

print(X[[0,2]]) #Prints the 0th and 2nd rows of X

print(X[ X[0] < 5]) #Prints all rows where the data for the 0th column
	 	    #is less than 5.
