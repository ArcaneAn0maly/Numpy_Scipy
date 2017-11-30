import numpy as np
X = []

for line in open('data_2d.csv'):
  row = line.split(',')
  sample = map(float,row) #map applies a function, in this case "float"
			  #to all the items in a list, "row"
  X.append(sample)

X = np.array(X)

print(X)
print(X.shape)
