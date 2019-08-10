# import soundfile as sf
# import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from easygui import *
import matplotlib.pyplot as plt
from pylab import figure
import ntpath
from pydub import AudioSegment
import numpy as np
import math as m
import os

def audio_load():

    message = 'Select audio file.';
    path = fileopenbox(message)
    fileName=ntpath.basename(os.path.splitext(path)[0])
    (fs, audiodata)=read(path)
    audiodata = audiodata.astype(float)
    signal =audiodata.sum(axis=1) / 2
    signal_ceil = np.ceil(audiodata.sum(axis=1) / 2)
    signal_floor = np.floor(audiodata.sum(axis=1) / 2)
    #signal = (audiodata[:, 0] + audiodata[:, 1]) / 2
    file = {'fs': fs, 'signal': signal,'name': fileName}

    sound = AudioSegment.from_wav(path)
    sound = sound.set_channels(1).get_array_of_samples()
    #sound.export("path.wav", format="wav")

    # path = fileopenbox(message)
    # (fs, audiodata) = read(path)
    # A=audiodata.astype('float64')
    # n=np.array_equal(A, signal)

#For analzing the data medium: is it at zero or shifted?
#If the medium of the data is at zero then its a good music file to embed the text for Echo Hiding.
#     fig1=figure('firstchannel')
#     #plt.hist(audiodata[:,0], bins=201, range=[-100,+100]) #indibidual channel.
#     plt.hist(signal_ceil, bins=201, range=[-200, +200])  # indibidual channel.
#     #plt.show()
#     fig2=figure('Floor_channel')
#     plt.hist(signal_floor, bins=201, range=[-200,+200])
# #Analyzing the mono medium music.
#     fig2=figure('AVG_channel')
#     plt.hist(signal, bins=201, range=[-200,+200])
#     plt.show()

    # plt.plot(audiodata)
    # plt.show()

    return file
#file=audio_load()




