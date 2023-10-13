import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Replace 'your_audio_file.wav' with the path to your audio file
sample_rate, audio_data = wavfile.read('recording4.wav')

# Normalize the audio data to a range of -1 to 1
audio_data = audio_data / np.max(np.abs(audio_data))

# Calculate the FFT
fft_result = np.fft.fft(audio_data)
n = len(fft_result)

# Calculate the frequency values
freq = np.fft.fftfreq(n, 1 / sample_rate)

# Plot the frequency spectrum (symmetric)
#plt.figure(figsize=(10, 6))
plt.plot(freq, (fft_result))

plt.show()
