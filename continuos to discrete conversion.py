import matplotlib.pyplot as plt
from scipy.signal import cont2discrete, lti, dlti, dstep
import numpy as np
import wave

file_1 = wave.open('sample_1.wav', 'rb')

sample_freq_1 = file_1.getframerate()
frames_1 = file_1.getnframes()
signal_wave_1 = file_1.readframes(-1)

file_1.close()

file_2 = wave.open('sample_2.wav', 'rb')

sample_freq_2 = file_2.getframerate()
frames_2 = file_2.getnframes()
signal_wave_2 = file_2.readframes(-1)

file_2.close()

audio_array_1 = np.frombuffer(signal_wave_1, dtype=np.int16)
audio_array_2 = np.frombuffer(signal_wave_2, dtype=np.int16)

#A = np.array([[0, 1],[-10., -3]])
#B = np.array([[0],[10.]])
#C = np.array([[1., 0]])
#D = np.array([[0.]])
l_system = lti(audio_array_1)
t, x = l_system.step(T=np.linspace(0, 5, 100))
fig, ax = plt.subplots()
ax.plot(t, x, label='Continuous', linewidth=3)

dt = 0.1
for method in ['zoh', 'bilinear', 'euler', 'backward_diff', 'foh', 'impulse']:
   d_system = cont2discrete((audio_array_1), dt, method=method)
   s, x_d = dstep(d_system)
   ax.step(s, np.squeeze(x_d), label=method, where='post')
ax.axis([t[0], t[-1], x[0], 1.4])
ax.legend(loc='best')
fig.tight_layout()
plt.show()
