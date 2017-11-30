#v = v.A.A.A.A.A.A
import numpy as np
import matplotlib.pyplot as plt
v = np.array([1./3.,1./3.,1./3.])
A = np.array([[0.3,0.6,0.1],[0.5,0.2,0.3],[0.4,0.1,0.5]])

quant = np.zeros(25)
x = np.linspace(0, 24, 25)

for i in range(0,25):
  vold = v
  v = np.dot(v,A)
  quant[i] = np.sqrt(np.dot((v-vold),(v-vold)))

plt.plot(quant)
plt.show()