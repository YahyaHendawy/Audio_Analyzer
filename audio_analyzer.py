import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

fs = 44100  # sample rate
duration = 2  # seconds

print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

audio = audio.flatten()

# FFT (convert to frequency domain)
fft = np.fft.fft(audio)
freq = np.fft.fftfreq(len(fft), 1/fs)

# Only positive frequencies
mask = freq >= 0
freq = freq[mask]
fft = np.abs(fft[mask])

plt.plot(freq, fft)
plt.title("Audio Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.savefig("../graphs/spectrum.png")
plt.show()
