import numpy as np
import wave
import matplotlib.pyplot as plt

file_1 = wave.open('sample_1.wav', 'rb')

sample_freq_1 = file_1.getframerate()
frames_1 = file_1.getnframes()
signal_wave_1 = file_1.readframes(-1)
print(sample_freq_1)
print(frames_1)
#print(signal_wave_1)

file_1.close()

file_2 = wave.open('sample_2.wav', 'rb')

sample_freq_2 = file_2.getframerate()
frames_2 = file_2.getnframes()
signal_wave_2 = file_2.readframes(-1)
print(sample_freq_2)
print(frames_2)
#print(signal_wave_1)

file_2.close()

audio_array_1 = np.frombuffer(signal_wave_1, dtype=np.int16)
audio_array_2 = np.frombuffer(signal_wave_2, dtype=np.int16)

#audio_array_1 = [1,2,3]
#audio_array_2 = [1,2,3]

c = np.cov(audio_array_1,audio_array_1)
print(c)

#time = frames_1 / sample_freq_1


#if one channel use int16, if 2 use int32
#audio_array = np.frombuffer(c, dtype=np.int16)

#times = np.linspace(0, 16, num=frames_1)

#plt.figure(figsize=(45, 10))
#plt.plot(times, audio_array)
#plt.ylabel('Signal Wave')
#plt.xlabel('Time (s)')
#plt.xlim(0, time)
#plt.title('audio signal')
#plt.show()

