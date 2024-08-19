import numpy as np
import wave
import matplotlib.pyplot as plt
from scipy.signal import correlate as cr
from matplotlib.pyplot import step, show

file_1 = wave.open('sample_6.wav', 'rb')

sample_freq_1 = file_1.getframerate()
frames_1 = file_1.getnframes()
signal_wave_1 = file_1.readframes(-1)
print(sample_freq_1)
print(frames_1)
#print(signal_wave_1)

file_1.close()
time = frames_1 / sample_freq_1

file_2 = wave.open('sample_7.wav', 'rb')

sample_freq_2 = file_2.getframerate()
frames_2 = file_2.getnframes()
signal_wave_2 = file_2.readframes(-1)
print(sample_freq_2)
print(frames_2)
#print(signal_wave_1)

file_2.close()
time = frames_2 / sample_freq_2

audio_array_1 = np.frombuffer(signal_wave_1, dtype=np.int16)
audio_array_2 = np.frombuffer(signal_wave_2, dtype=np.int16)
print(sample_freq_1)
t_1 = np.linspace(0, time, num=frames_1)
t_2 = np.linspace(0, time, num=frames_1)

l_1 = list(audio_array_1)
l_2 = list(audio_array_2)
a = len(l_1)
b = len(l_2)
print("No of analog data:",a)
print("No of analog data:",b)
l_3 = []
l_4 = []
count= 0
count_1 = len(l_1)
x_1 = audio_array_1
x_2 = audio_array_2

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
#plt.show()

for i in xq_1:
    item_1 = bin(i)[2:]
    l_3.append(item_1)

print(len(l_3))
#print(l_3)

l_5 = []
l_6 = []

for i in range(0,len(l_3)):
    item_1 = str(l_3[i])
    a = len(item_1)
    for j in range (0,a):
        c = item_1[j]
        l_5.append(c)
#print("the lenght of l_5:",len(l_5))
#print(l_5)


for i in xq_2:
    item_2 = bin(i)[2:]
    l_4.append(item_2)

print(len(l_4))
#print(l_4)

for i in range(0,len(l_4)):
    item_2 = str(l_4[i])
    a = len(item_2)
    for j in range (0,a):
        c = item_2[j]
        l_6.append(c)
#print("the lenght of l_6:",len(l_6))
#print(l_6)
    
#def binary_data(data):
#    return [1 if x in data else 0 for x in range(data[-1] + 1)]

#data = xq_1
#bindata = binary_data(data)
#xaxis = np.arange(0, len(bindata))
#yaxis = np.array(bindata)
#step(xaxis, yaxis)
#show()

#def binary_data_1(data):
 #   return [1 if x in data else 0 for x in range(data[-1] + 1)]

#data_1 = xq_2
#bindata_1 = binary_data_1(data)
#xaxis_1 = np.arange(0, len(bindata_1))
#yaxis_1 = np.array(bindata_1)
#step(xaxis_1, yaxis_1)
#print("the binary data of signal_1 :",list(xq_1))
#print("the binary data of signal_1 :",list(xq_2))

#for i in range(0,count_1):
 #   item_1 = bin(l_1[i])[2:]
  #  l_3.append(item_1)
   # item_2 = bin(l_2[i])[2:]
    #l_4.append(item_2)

#signal 1
#time_1 = frames_1 / sample_freq_1
#times_1 = np.linspace(0, time_1, num=frames_1)
#plt.figure(figsize=(45, 10))
#plt.plot(times_1, l_3)
#plt.ylabel('Signal Wave')
#plt.xlabel('Time (s)')
#plt.title('audio signal')
#plt.show()

#signal 2
#time_2 = frames_2 / sample_freq_2
#plt.figure(figsize=(45, 10))
#plt.plot(times_2, l_4)

#plt.ylabel('Signal Wave')
#plt.xlabel('Time (s)')
#plt.title('audio signal')
#plt.show()

c = len(l_5)
d = len(l_6)
print("No of digital data:",c)
print("No of digital data:",d)

for i in range(0,c):
    if l_5[i] == l_6[i]:
        count = count + 1

z = (count/count_1)*100

print("Total no of similar elements:",count)
print("The similarity precentage is : ",z)

# converting list to array
arr_1 = np.array(l_5)
arr_2 = np.array(l_6)

print(len(arr_1))
print(len(arr_2))
c = cr(l_5,l_6)
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




    

    
