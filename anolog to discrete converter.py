import numpy as np
import matplotlib.pyplot as plt
import wave
import scipy
from scipy.signal import correlate as cr
from scipy import signal

file_1 = wave.open('sample_6.wav', 'rb')

sample_freq_1 = file_1.getframerate()
frames_1 = file_1.getnframes()
signal_wave_1 = file_1.readframes(-1)

file_1.close()

file_2 = wave.open('sample_7.wav', 'rb')

sample_freq_2 = file_2.getframerate()
frames_2 = file_2.getnframes()
signal_wave_2 = file_2.readframes(-1)

file_2.close()

audio_array_1 = np.frombuffer(signal_wave_1, dtype=np.int16)
audio_array_2 = np.frombuffer(signal_wave_2, dtype=np.int16)
#audio_array_1 = [1.625,5.64,3.78]
#audio_array_2 = [1.2655,5.999,-3.0001]

#print(audio_array_1)
#print(audio_array_2)
print(len(audio_array_1))
print(len(audio_array_2))
time = frames_1 / sample_freq_1
t_1 = np.linspace(0, time, num=frames_1)

x_1 = audio_array_1
plt.figure(figsize = (10,8)) # set the size of figure




#signal 1
# 1. Plotting Analog Signal
plt.subplot(4, 2, 1)
plt.title('Analog Signal', fontsize=20)

plt.plot(t_1, x_1, linewidth=3, label='x(t) = (0.85)^t')
plt.xlabel('t' , fontsize=15)
plt.ylabel('amplitude', fontsize=15)
plt.legend(loc='upper right')

# 2. Sampling and Plotting of Sampled signal
plt.subplot(4, 2, 2)
plt.title('Sampling', fontsize=20)
plt.plot(t_1, x_1, linewidth=3, label='x(t) = (0.85)^t')
n_1 = t_1

markerline, stemlines, baseline = plt.stem(n_1, x_1, label='x(n) = (0.85)^n')
plt.setp(stemlines, 'linewidth', 3)
plt.xlabel('n' , fontsize = 15)
plt.ylabel('amplitude', fontsize = 15)
plt.legend(loc='upper right')

# 3. Quantization
plt.subplot(4, 2, 3)
plt.title('Quantization', fontsize = 20)

plt.plot(t_1, x_1, linewidth =3)
markerline, stemlines, baseline=plt.stem(n_1,x_1)
plt.setp(stemlines, 'linewidth', 3)
plt.xlabel('n', fontsize = 15)
plt.ylabel('Range of Quantizer', fontsize=15)

plt.axhline(y = 0.1, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.2, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.3, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.4, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.5, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.6, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.7, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.8, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.9, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 1.0, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)

plt.subplot(4, 2, 4)
plt.title('Quantized Signal', fontsize = 20)
xq_1 = np.around(x_1,1)
markerline, stemlines, baseline = plt.stem(n_1,xq_1)
plt.setp(stemlines, 'linewidth', 3) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('Range of Quantizer', fontsize=15)

plt.axhline(y = 0.1, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.2, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.3, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.4, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.5, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.6, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.7, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.8, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.9, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 1.0, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)

t_2 = np.linspace(0, time, num=frames_1)

x_2 = audio_array_2

#signal 2
# 1. Plotting Analog Signal
plt.subplot(4, 2, 5)
plt.title('Analog Signal', fontsize=20)

plt.plot(t_2, x_2, linewidth=3, label='x(t) = (0.85)^t')
plt.xlabel('t' , fontsize=15)
plt.ylabel('amplitude', fontsize=15)
plt.legend(loc='upper right')

# 2. Sampling and Plotting of Sampled signal
plt.subplot(4, 2, 6)
plt.title('Sampling', fontsize=20)
plt.plot(t_2, x_2, linewidth=3, label='x(t) = (0.85)^t')
n_2 = t_2

markerline, stemlines, baseline = plt.stem(n_2, x_2, label='x(n) = (0.85)^n')
plt.setp(stemlines, 'linewidth', 3)
plt.xlabel('n' , fontsize = 15)
plt.ylabel('amplitude', fontsize = 15)
plt.legend(loc='upper right')

# 3. Quantization
plt.subplot(4, 2, 7)
plt.title('Quantization', fontsize = 20)

plt.plot(t_2, x_2, linewidth =3)
markerline, stemlines, baseline=plt.stem(n_2,x_2)
plt.setp(stemlines, 'linewidth', 3)
plt.xlabel('n', fontsize = 15)
plt.ylabel('Range of Quantizer', fontsize=15)

plt.axhline(y = 0.1, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.2, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.3, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.4, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.5, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.6, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.7, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.8, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.9, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 1.0, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)

plt.subplot(4, 2, 8)
plt.title('Quantized Signal', fontsize = 20)
xq_2 = np.around(x_2,1)
markerline, stemlines, baseline = plt.stem(n_2,xq_2)
plt.setp(stemlines, 'linewidth', 3) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('Range of Quantizer', fontsize=15)

plt.axhline(y = 0.1, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.2, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.3, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.4, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.5, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.6, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.7, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.8, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.9, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 1.0, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)


plt.tight_layout()
plt.show()

l_1 = list(xq_1)
l_2 = list(xq_2)
county = 0
countz = 0
count_1 = len(l_1)

for i in range(0,count_1):
    if l_1[i] == l_2[i]:
        county = county + 1
    elif l_1[i] and l_2[i] != 0 :
        if (l_1[i]/l_2[i]) >= 0.9742 and (l_1[i]/l_2[i]) <=1.0491 :
            countz = countz + 1

count = county + countz 
print(count)
count_1 = len(l_1)
similarity = (count/count_1)*100

print("The similarity of the two signals:",similarity)
c = cr(xq_1,xq_2)
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
print("The similarity percentage with correlation:",z)





















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




    
