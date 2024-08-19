import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd
from scipy.signal import correlate as cr

Audio_1 = "sample_5.wav"
Audio_2 = "sample_4.wav"


Aud_1, sr = librosa.load(Audio_1)
Aud_2, _ = librosa.load(Audio_2)

FRAME_SIZE = 1024
HOP_LENGTH = 512

def amplitude_envelope(signal, frame_size, hop_length):
    """Calculate the amplitude envelope of a signal with a given frame size nad hop length."""
    amplitude_envelope = []
    
    # calculate amplitude envelope for each frame
    for i in range(0, len(signal), hop_length): 
        amplitude_envelope_current_frame = max(signal[i:i+frame_size]) 
        amplitude_envelope.append(amplitude_envelope_current_frame)
    
    return np.array(amplitude_envelope)

ae_audio_1 = amplitude_envelope(Aud_1, FRAME_SIZE, HOP_LENGTH)
ae_audio_2 = amplitude_envelope(Aud_2, FRAME_SIZE, HOP_LENGTH)

frames = range(len(ae_audio_1))
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)

plt.figure(figsize=(15, 17))

ax = plt.subplot(3, 1, 1)
librosa.display.waveshow(Aud_1, alpha=0.5)
plt.plot(t, ae_audio_1, color="r")
plt.title("AUD_1")


plt.subplot(3, 1, 2)
librosa.display.waveshow(Aud_2, alpha=0.5)
plt.plot(t, ae_audio_2, color="r")
plt.title("AUD_2")
plt.show()

c = cr(ae_audio_1,ae_audio_2)
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
    if float(l_1[i]) == float(l_3[i]):
        county = county + 1
    if int(l_1[i]) == int(l_2[i]):
        #print("l1 elements:",int(l_1[i]))
        #print("l2 elements:",int(l_2[i]))
        countz = countz + 1
    if (l_1[i]/l_2[i]) >= 0.9742 and (l_1[i]/l_2[i]) <=1.0491 :
        if (l_1[i]/l_3[i]) >= 0.9742 and (l_1[i]/l_3[i]) <=1.0491 :
            countz = countz + 1

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
