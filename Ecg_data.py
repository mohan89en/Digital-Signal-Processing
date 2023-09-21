# import electrocardiogram
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
import scipy.signal as signal

# import numpy
import numpy as np

# define electrocardiogram as ecg model
ecg = electrocardiogram()

# frequency is 0
frequency = 360

# calculating time data with ecg size along with frequency
t = np.arange(ecg.size) / frequency
y=ecg
hi = signal.hilbert(y)
alpha = np.linspace(0,1,20)*2*np.pi
for i in range(1,20):
   x1 = np.cos(alpha[i])*y+np.sin(alpha[i])*np.imag(hi)
   plt.plot(t,x1)
# plotting time and ecg model
#plt.plot(time_data, ecg)
plt.xlabel("time in seconds")
plt.ylabel("ECG in milli Volts")
plt.xlim(9.1, 9.6)
#plt.ylim(-1, 1.5)

# display
plt.show()
