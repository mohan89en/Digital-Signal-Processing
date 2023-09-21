import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as sound

samplerate,data = sound.read('recording1.wav')
#print(samplerate)
duration = len(data)/samplerate
time = np.arange(0,duration,1/samplerate)
plt.plot(time,data)
plt.show()