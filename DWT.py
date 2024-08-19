from scipy.io import wavfile
import wave
import numpy as np
from skimage.restoration import denoise_wavelet
import matplotlib.pyplot as plt
#x = sud data
#sigma = 0.5
fs,x_n = wavfile.read('sample_6.wav')
#x_n = (x_n1)/(max(x_n1))
x_denoise = denoise_wavelet(x_n,method='VisuShrink',mode ='soft',wavelet_levels=3,wavelet='sym8',rescale_sigma='True')


file_1 = wave.open('sample_6.wav', 'rb')

sample_freq_1 = file_1.getframerate()
frames_1 = file_1.getnframes()
signal_wave_1 = file_1.readframes(-1)
print(sample_freq_1)
print(frames_1)
audio_array_1 = np.frombuffer(signal_wave_1, dtype=np.int16)

#print(signal_wave_1)

file_1.close()
plt.figure(figsize=(20,10),dpi=100)
#plt.plot(audio_array_1)
plt.plot(x_denoise)
plt.show()
#x_write = wave.open('sample_5.wav','wb')
#x_write.setnchannels(1)
#x_write.setsampwidth(2)
#x_write.setframerate(fs)
#x_write.writeframes(x_denoise)
#x_write.close()
k = len(audio_array_1)
county = 0
countz = 0
for i in range(0,k):
    if int(audio_array_1[i]) == int(x_denoise[i]):
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

z = (count/k)*100
print("The similarity percentage:",z)

print(audio_array_1)

print(x_denoise)
