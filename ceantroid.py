import librosa
import matplotlib.pyplot as plt
audio = 'sample_1.wav'
x, sr = librosa.load(audio)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize = (10, 5))
librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'hz')
plt.colorbar()
import sklearn
spectral_centroids = librosa.feature.spectral_centroid(y=x, sr = sr)#[0]
#spectral_centroids.shape(775, )
# Computing the time variable
#for visualization
plt.figure(figsize = (12, 4))
frames = range(len(spectral_centroids))
t = librosa.frames_to_time(frames)
# Normalising the spectral centroid
#for visualisation
def normalize(x, axis = 0):
  return sklearn.preprocessing.minmax_scale(x, axis = axis)
#Plotting the Spectral Centroid along the waveform
librosa.display.waveshow(x, sr = sr, alpha = 0.4)
plt.plot(t, normalize(spectral_centroids), color = 'b')
spectral_bandwidth_2 = librosa.feature.spectral_bandwidth(x + 0.01, sr = sr)[0]
spectral_bandwidth_3 = librosa.feature.spectral_bandwidth(x + 0.01, sr = sr, p = 3)[0]
spectral_bandwidth_4 = librosa.feature.spectral_bandwidth(x + 0.01, sr = sr, p = 4)[0]
plt.figure(figsize = (15, 9))
librosa.display.waveshow(x, sr = sr, alpha = 0.4)
plt.plot(t, normalize(spectral_bandwidth_2), color = 'r')
plt.plot(t, normalize(spectral_bandwidth_3), color = 'g')
plt.plot(t, normalize(spectral_bandwidth_4), color = 'y')
spectral_rolloff = librosa.feature.spectral_rolloff(x + 0.01, sr = sr)[0]
plt.figure(figsize = (12, 4))
librosa.display.waveshow(x, sr = sr, alpha = 0.4)
plt.plot(t, normalize(spectral_rolloff), color = 'r')
