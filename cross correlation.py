import statsmodels.api as sm
import numpy as np
import wave  
import matplotlib.pyplot as plt
from scipy.signal import correlate as cr
import pandas as pd
import seaborn as sns
from scipy.stats import norm

file_1 = wave.open('sample_10.wav', 'rb')

sample_freq_1 = file_1.getframerate()
frames_1 = file_1.getnframes()
signal_wave_1 = file_1.readframes(-1)

file_1.close()

file_2 = wave.open('sample_11.wav', 'rb')

sample_freq_2 = file_2.getframerate()
frames_2 = file_2.getnframes()
signal_wave_2 = file_2.readframes(-1)

file_2.close()

audio_array_1 = np.frombuffer(signal_wave_1, dtype=np.int16)
audio_array_2 = np.frombuffer(signal_wave_2, dtype=np.int16)
audio_array_1 = [1.625,5.64,3.78]
audio_array_2 = [1.2655,5.999,-3.0001]

print(audio_array_1)
print(audio_array_2)
print(len(audio_array_1))
print(len(audio_array_2))
c=sm.tsa.stattools.ccf(audio_array_1, audio_array_2, adjusted=False)
c = np.correlate(audio_array_1, audio_array_2, mode = 'valid')
print(c)
print(len(c))


start = 0
mid_point_1 = int((len(c)/2)-0.5)
mid_point_2 = int(mid_point_1 + 1)
end = len(c)
l_1 = list(c[start:mid_point_1])
l_2 = list(c[mid_point_2:end])
l_3 = []
print(l_1)
print(l_2)
#print(l_3)
print(len(l_1))
print(len(l_2))
for i in l_2:
    l_3.insert(0, i)
print(l_3)
k = len(l_1)-1
count_1 = len(l_1)
l_4 = []

for item in l_1:
   for item1 in l_3:
     if item == item1:
        l_4.append(item)


print(l_4)
count = len(l_4)
print(count)

count = 0

for i in range(0,k):
   if l_1[i] == l_3[i]:
        count = count + 1
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


statisticcs.corrrelation(x,y)

corrmat = data.corr()

np.correlate(array1, array2)

 #Pre-allocate correlation array
corr = (len(sig1) - len(sig2) + 1) * [0]
 #Go through lag components one-by-one
for l in range(len(corr)):
    corr[l] = sum([sig1[i+l] * sig2[i] for i in range(len(sig2))])
print(corr)

import scipy.signal  
corr = scipy.signal.correlate(sig1, sig2)
 #Remove padded correlations
corr = corr[(len(sig1)-len(sig2)-1):len(corr)-((len(sig1)-len(sig2)-1))]
print(corr)

import numpy as np
nsig1 = sig1 - np.mean(sig1) # Demean
nsig2 = sig2 - np.mean(sig2) # Demean
corr = np.correlate(a=nsig1, v=nsig2)
corr = (len(sig2) * np.std(sig1) * np.std(sig2)) # Normalization
print(corr)

import statsmodels.api as sm
corr = sm.tsa.stattools.ccf(sig2, sig1, adjusted=False)
 #Remove padding and reverse the order
corr[0:(len(sig2)+1)][::-1]
