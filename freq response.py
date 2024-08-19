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
print(sample_freq_1)
#signal_1
fs = sample_freq_1
tstep = 1/fs
f0 = 0.1
n = int(fs/f0)
t = np.linspace(0,(n-1)*tstep,n)
fstep = fs/n
f =np.linspace(0,(n-1)*fstep,n)
y = audio_array_1

#perform fft
X = np.fft.fft(y)
X_mag = np.abs(X)/n
f_plot = f[0:int(n/2+1)]
X_mag_plot = 2*X_mag[0:int(n/2+1)]
X_mag_plot[0] = X_mag_plot[0]/2



#signal_2
fs_2 = sample_freq_2
tstep_2 = 1/fs_2
f0_2 = 0.1
n_2 = int(fs_2/f0_2)
t_2 = np.linspace(0,(n_2-1)*tstep_2,n_2)
fstep_2 = fs_2/n_2
f_2 =np.linspace(0,(n_2-1)*fstep_2,n_2)
y_2 = audio_array_2

#perform fft
X_2 = np.fft.fft(y_2)
X_mag_2 = np.abs(X_2)/n
f_plot_2 = f[0:int(n_2/2+1)]
X_mag_plot_2 = 2*X_mag_2[0:int(n_2/2+1)]
X_mag_plot_2[0] = X_mag_plot_2[0]/2


#fig,[ax1,ax2,ax3,ax4]= plt.subplots(nrows=2,ncols=1)

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

ax1.plot(t_2,y_2,'r')
ax2.plot(f_plot_2,X_mag_plot_2,'b')
ax3.plot(t,y,'r')
ax4.plot(f_plot,X_mag_plot,'b')
plt.show()
