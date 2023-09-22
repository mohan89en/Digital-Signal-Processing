import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import pandas as pd

frequency = 360
df = pd.read_csv("ecg.csv")
x=df.iloc[:, 0].values
t = np.arange(x.size) / frequency
noise_frequency = 50000  # 50 kHz
noise_amplitude = 1  # Adjust the amplitude as needed
noise_signal = noise_amplitude * np.sin(2 * np.pi * noise_frequency * t)

# Add the noise to the ECG signal
with_noise = x + noise_signal
plt.subplot(2,1,1)
plt.plot(t,x)
plt.xlim(9,9.3)
#plt.ylim(-1, 1.5)
plt.subplot(2,1,2)
plt.plot(t,with_noise)
plt.xlim(9,9.3)
plt.show()


