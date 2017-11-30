import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,1000) #0 to ten, ten points total
y=np.sin(x)

plt.plot(x,y)
plt.xlabel("Time")
plt.ylabel('f(t)')
plt.show()
