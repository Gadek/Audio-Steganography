from scipy.io.wavfile import write
import numpy as np

samplerate = 44100; fs = 1
t = np.linspace(0., 1., samplerate)
# print(t)
amplitude = np.iinfo(np.int16).max
array1 = np.sin(2. * np.pi * fs * t) * amplitude
array2 = np.sin(2. * np.pi * fs * t + np.pi/2) * amplitude
array3 = np.sin(2. * np.pi * fs * t + np.pi) * amplitude
data = np.array([array1, array2]).transpose()
# data = np.array([[2,2,3,2,1,2,3,2,1,2,3], [3,3,4,3,2,3,4,3,2,3,4]], np.int16)
# data = np.array([array1, array2], np.int16)
path = "C:\\Users\\rados\\Desktop\\udost\\audio-steganography\\example1.wav"
write(path, samplerate, data.astype(np.int16))