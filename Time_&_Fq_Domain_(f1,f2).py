import numpy as np
import wave
import matplotlib.pyplot as plt
from scipy.signal import correlate as cr

file_1 = wave.open('sample_6.wav', 'rb')

sample_freq_1 = file_1.getframerate()
frames_1 = file_1.getnframes()
signal_wave_1 = file_1.readframes(-1)
print(sample_freq_1)
print(frames_1)
#print(signal_wave_1)

file_1.close()

file_2 = wave.open('sample_4.wav', 'rb')

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

#print("freq value of freq resp of 2",list(f_plot_2))
#print("freq value of freq resp of 1",list(f_plot))
#print("mag value of freq resp of 2",list(X_mag_plot_2))
#print("mag value of freq resp of 1",list(X_mag_plot))
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

ax1.plot(t_2,y_2,'r')
#ax2.plot(f_plot_2,X_mag_plot_2,'b')
ax3.plot(t,y,'r')
#ax4.plot(f_plot,X_mag_plot,'b')
plt.show()

c = cr(X_mag_plot_2,X_mag_plot)
print(c)
print(len(c))


start = 0
mid_point_1 = int((len(c)/2)-0.5)
mid_point_2 = int(mid_point_1 + 1)
end = len(c)
l_1 = list(c[start:mid_point_1])
l_2 = list(c[mid_point_2:end])
l_3 = []
#print(l_1)
#print(l_2)
#print(l_3)
#print(len(l_1))
#print(len(l_2))
for i in l_2:
    l_3.insert(0, i)
#print(l_3)
k = len(l_1)
count_1 = len(l_1)
l_4 = []

#for item in l_1:
#   for item1 in l_3:
#     if item == item1:
#        l_4.append(item)


#print(l_4)
#count = len(l_4)
#print(count)

county = 0
countz = 0

for i in range(0,k):
    if int(l_1[i]) == int(l_3[i]):
        county = county + 1
    #if int(l_1[i]) == int(l_2[i]):
        #print("l1 elements:",int(l_1[i]))
        #print("l2 elements:",int(l_2[i]))
        #countz = countz + 1
    #if (l_1[i]/l_2[i]) >= 0.9742 and (l_1[i]/l_2[i]) <=1.0491 :
    #if l_1[i] and l_3[i] != 0 :
     #   if (l_1[i]/l_3[i]) >= 0.9742 and (l_1[i]/l_3[i]) <=1.0491 :
      #      countz = countz + 1

count = county + countz
print(county)
print(countz)
print(count)

z = (count/count_1)*100
print("The similarity percentage:",z)





















a = np.arange(1,c.size+1)
plt.figure(figsize=(45, 10))
plt.plot(a,c,'ro-' )
plt.ylabel('Signal Wave')
plt.xlabel('Time (s)')
plt.title('audio signal')
plt.show()


#ca = cr(audio_array_1,audio_array_1)
#ca=[9,8,7,10,6,4,7,8,1,2]
#d = np.arange(1,len(ca)+1)

#plt.plot(d,ca,'gD:' )
#plt.show()



