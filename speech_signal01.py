import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as sound
import scipy.fft as fft

# Load the audio signal from the WAV file
samplerate, data = sound.read('recording4.wav')

# Define the parameters for the 50 kHz noise
noise_frequency = 50  # 50 kHz
noise_amplitude = max(data[:, 0])  # Adjust the amplitude as needed

# Generate the noise signal
duration = len(data) / samplerate
time = np.arange(0, duration, 1 / samplerate)
noise_signal = noise_amplitude * np.sin(2 * np.pi * noise_frequency * time)

# Add the noise to both channels of the audio signal
with_noise = data + noise_signal[:, np.newaxis]

# Perform FFT on the noisy signal
fft_result = fft.fft(with_noise[:, 0])  # Use one channel for processing

# Identify the frequency bin corresponding to the noise frequency
# Frequency bin = (noise_frequency / samplerate) * N, where N is the number of samples
noise_bin = int((noise_frequency / samplerate) * len(fft_result))

# Set the amplitude of the noise frequency bin to zero
fft_result[noise_bin] = 0
# Also, set the conjugate symmetric component to zero
fft_result[-noise_bin] = 0

# Perform the inverse FFT to get the cleaned audio signal
cleaned_signal = np.real(fft.ifft(fft_result))

# Save the cleaned audio signal to a new WAV file
sound.write('cleaned_recording.wav', samplerate, np.int16(cleaned_signal))

# Plot the cleaned signal
plt.plot(time, cleaned_signal)
plt.title('Cleaned Audio Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
