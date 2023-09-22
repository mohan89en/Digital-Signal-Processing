% Load the audio signal from the WAV file
[data, samplerate] = audioread('recording4.wav');

% Define the parameters for the 50 kHz noise
noise_frequency = 50;  % 50 kHz
noise_amplitude =max(max(data)); % Adjust the amplitude as needed

% Generate the noise signal
duration = length(data) / samplerate;
time = (0:1/samplerate:duration-1/samplerate)';
noise_signal = noise_amplitude * sin(2 * pi * noise_frequency * time);

% Add the noise to both channels of the audio signal
with_noise = data + noise_signal;


% Save the audio signal with noise to a new WAV file
plot(with_noise)
audiowrite('noisy_recording.wav', with_noise, samplerate);

% Play the noisy recording
sound(with_noise, samplerate);
