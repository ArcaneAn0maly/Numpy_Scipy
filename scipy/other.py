#Other functions in scipy
import numpy as np
import matplotlib.pyplot as plt
 
#Read wave file using scipy
#scipy.io.wavefile.read
#Write wave file using scipy
#scipy.io.wavefile.Write

#Convolute signal (2d for images)
#scipy.signal.convolve2d

#3 frequencies in this wave
x = np.linspace(0,100,10000)
y = np.sin(x) + np.sin(3*x) + np.sin(5*x)

#Fourier transform of y
Y = np.fft.fft(y)

plt.plot(np.abs(Y))
plt.show()