import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
from scipy.io import wavfile
import wave

file_1 = wave.open('sample_4.wav', 'rb')

sample_freq_1 = file_1.getframerate()
frames_1 = file_1.getnframes()

file_1.close()

file_2 = wave.open('sample_4.wav', 'rb')

sample_freq_2 = file_2.getframerate()
frames_2 = file_2.getnframes()
signal_wave_2 = file_2.readframes(-1)

file_2.close()

duration = 1.0
fs = 400.0
samples = int(fs*duration)
t = np.arange(samples) / fs
signal = chirp(t, 20.0, t[-1], 100.0)
signal *= (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t) )

analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = (np.diff(instantaneous_phase) /
                           (2.0*np.pi) * fs)
fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.plot(t, signal, label='signal')
ax0.plot(t, amplitude_envelope, label='envelope')
ax0.set_xlabel("time in seconds")
ax0.legend()
ax1.plot(t[1:], instantaneous_frequency)
ax1.set_xlabel("time in seconds")
ax1.set_ylim(0.0, 120.0)
fig.tight_layout()
fig.show()
