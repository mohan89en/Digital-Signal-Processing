import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import pandas as pd
F = 200
t = np.linspace(-5,5, 200)
mu=0
sigma = 1

y= (np.exp(-((t - mu) ** 2) / (2 * sigma ** 2)))  #Gauss
#y = np.sin(t)
#y=np.cos(t)
hi = signal.hilbert(y)
alpha = np.linspace(0,1,20)*2*np.pi
for i in range(1,20):
   x1 = np.cos(alpha[i])*y+np.sin(alpha[i])*np.imag(hi)
   plt.plot(t,x1)
#plt.plot(x)
plt.savefig('Gauss_phase_Transform.png')
plt.show()


