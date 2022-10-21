from scipy.io.wavfile import write, read
import numpy as np
from utils import plot

def write_sinwave(path, seconds, channels, fs, samplerate):
    frames = samplerate * seconds
    t = np.linspace(0., seconds, frames)
    amplitude = np.iinfo(np.int16).max
    array1 = np.sin(2. * np.pi * fs * t) * amplitude
    array2 = np.sin(2. * np.pi * fs * t + np.pi/2) * amplitude
    array3 = np.sin(2. * np.pi * fs * t + np.pi) * amplitude
    array4 = np.sin(2. * np.pi * fs * t + np.pi*3/2) * amplitude
    if channels==1:
        data = np.array(array1)
    elif channels==2:
        data = np.array([array1, array2]).transpose()
    elif channels==3:
        data = np.array([array1, array2, array3]).transpose()
    elif channels==4:
        data = np.array([array1, array2, array3, array4]).transpose()
    else:
        print("Error: Number of channels must be 1, 2, 3 or 4")
        return
    write(path, samplerate, data.astype(np.int16))

if __name__=="__main__":
    path = "C:\\Users\\rados\\Desktop\\udost\\audio-steganography\\sinwave1.wav"
    length=3
    channels=2
    samplerate=44100
    write_sinwave(path, seconds=length, channels=channels, fs=2, samplerate=samplerate)
    samplerate, data = read(path)
    plot(length, samplerate, data, channels)