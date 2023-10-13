import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as sound
import scipy.fft as fft

# Load the audio signal from the WAV file
samplerate, data = sound.read('recording4.wav')
data_length=len(data)
# Define the parameters for the 50 kHz noise
noise_frequency = 50  # 50 kHz
noise_amplitude = 2.5*1e7 # Adjust the amplitude as needed
print(samplerate)
# Generate the noise signal
duration = len(data)
time = np.arange(0, duration)*1/samplerate
noise_signal = noise_amplitude * np.sin(2 * np.pi * noise_frequency * time)
print(noise_signal)
# Add the noise to both channels of the audio signal
with_noise = data + noise_signal[:, np.newaxis]  # Add noise to both channels
print(np.max(with_noise))
plt.plot(time,(noise_signal))

# Create a subplot to compare the original and noisy signals
# plt.figure(figsize=(10, 6))

# plt.subplot(2, 1, 1)
# plt.plot(data[:, 0], label='Left Channel')
# plt.plot(data[:, 1], label='Right Channel')
# plt.title('Original Audio Signal')
# plt.xlabel('Sample')
# plt.ylabel('Amplitude')
# plt.legend()

# plt.subplot(2, 1, 2)
# plt.plot(with_noise[:, 0], label='Left Channel with Noise')
# plt.plot(with_noise[:, 1], label='Right Channel with Noise')
# plt.title('Audio Signal with 50 kHz Noise')
# plt.xlabel('Sample')
# plt.ylabel('Amplitude')
# plt.legend()

# plt.tight_layout(
frequency = (np.linspace(-1,1,data_length))*samplerate//2
fft_plot = fft.fft(with_noise[:,1])
#plt.plot(frequency,abs(fft_plot))
plt.show()

# Save the audio signal with noise to a new WAV file
sound.write('noisy_recording.wav', samplerate, np.int16(with_noise))
# print(max(data[:,0]))
