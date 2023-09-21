import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as sound

samplerate, data = sound.read('recording1.wav')
duration = len(data) / samplerate
time = np.arange(0, duration, 1 / samplerate)

noise_avg_watts = (50000)**2

# Generate separate samples of white noise for each channel
mean_noise = 0
noise_volts_left = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(data))
noise_volts_right = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(data))

# Combine the noise for both channels
noise_data = np.column_stack((data[:, 0] + noise_volts_left, data[:, 1] + noise_volts_right))

plt.figure(figsize=(10, 6))

# Plot the original left channel in blue
#plt.plot(time, data[:, 0], label='Original Left Channel', color='blue')

# Plot the original right channel in green
#plt.plot(time, data[:, 1], label='Original Right Channel', color='green')

# Plot the left channel with noise in red
#plt.plot(time, noise_data[:, 0], label='Noisy Left Channel', color='red')

# Plot the right channel with noise in orange
#plt.plot(time, noise_data[:, 1], label='Noisy Right Channel', color='orange')
plt.subplot(2,1,1)
plt.plot(time,data)
plt.subplot(2,1,2)
plt.plot(time,noise_data[:,0])
#plt.title('Audio Signal Comparison (Original vs. Noisy)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
