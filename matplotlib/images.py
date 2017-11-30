#Loads a set of 28x28 images (784 pixels total)
#First row contains labels (names) for each pixel. Subsequent
#rows contain values corresponding to pixel intensities.
#Since I import using Pandas, it ignores the first row as a
#header, which is good because it's just a row of labels
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("../../large_files/train.csv")
print(df.shape)

M = df.as_matrix()

im = M[0,1:] #First image in the dataset (row 0). Exclude first element
             #Because it's just number that the image is supposed to look like

print(im.shape)

#comvert the first image, which is a length 784 1d array into a 2d
#28 x 28 matrix using numpy's reshape function
im = im.reshape(28,28)
print(im.shape)

#plt.imshow(im)
#plt.imshow(im, cmap='gray')
plt.imshow(255 - im, cmap='gray')
plt.show()