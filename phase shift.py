# importing modules
import numpy
import matplotlib.pyplot as plt
from scipy.io import wavfile 

AudioName = "sample_5.wav" # Audio File
fs, Audiodata = wavfile.read(AudioName)

# Plot the audio signal in time
import matplotlib.pyplot as plt
#plt.plot(Audiodata)
#plt.title('Audio signal in time',size=16)

# assigning time values of the signal
# initial time period, final time period and phase angle
#signalTime = numpy.arange(5, 10, 0.25);

# getting the amplitude of the signal
#signalAmplitude = numpy.sin(signalTime)

# plotting the signal
#pyplot.plot(signalTime, signalAmplitude, color ='green')
#pyplot.show()

#pyplot.xlabel('Time')
#pyplot.ylabel('Amplitude')
#pyplot.title("Signal")


# plotting the phase spectrum of the signal
plt.phase_spectrum(Audiodata, color ='green')

plt.title("Phase Spectrum of the Signal")
plt.show()
