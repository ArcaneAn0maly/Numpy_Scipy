import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

A = pd.read_csv('data_1d.csv',header=None).as_matrix()
x = A[:,0] #x data is first column
y = A[:,1] #y data is second column

plt.scatter(x,y) #create scatter plot

x_line = np.linspace(0,100,100)
y_line = 2*x_line + 1

plt.plot(x_line,y_line)
plt.show()
