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
import audio_Randomness as ad #data Store

# message = 'Select audio file.';
# path = fileopenbox(message)

def audio_load(path):
    fileName=ntpath.basename(os.path.splitext(path)[0])
    (fs, data)=read(path)
    audiodata = data.astype(float)
    signal =audiodata.sum(axis=1) / 2
    #signal_ceil = np.ceil(audiodata.sum(axis=1) / 2)
    signal_floor = np.floor(signal)
    #signal = (audiodata[:, 0] + audiodata[:, 1]) / 2
    file = {'fs': fs, 'signal': signal_floor,'name': fileName}

    sound = AudioSegment.from_wav(path)
    sound = sound.set_channels(1).get_array_of_samples()
    #sound.export("path.wav", format="wav")

    # path = fileopenbox(message)
    # (fs, audiodata) = read(path)
    # A=audiodata.astype('float64')
    # n=np.array_equal(A, signal)

#For analzing the data medium: is it at zero or shifted?
#If the medium of the data is at zero then its a good music file to embed the text for Echo Hiding.
    fig1=figure('Left_channel')
     #plt.hist(audiodata[:,0], bins=201, range=[-100,+100]) #indibidual channel.
    img_Dir=os.path.dirname(path)+'\\Data_inExcel\\' + fileName ;
    plt.hist(data[:,0], bins=301,density=True)  # indibidual channel. #bin: Catagories/group/intervel/elements/occerances of a non-overlapperd range.
    plt.savefig(img_Dir + '_1st_channel.png')
    #plt.show()

    fig2=plt.figure('Avg_channel')
    plt.hist(signal_floor,bins=301,density=True,)
    fig2.savefig(img_Dir + '_Avg_ch.png', dpi=fig2.dpi)
    # plt.show()

# #Analyzing the mono medium music.
#     fig2=figure('Right_channel')
#     plt.hist(data[:,1], bins=201, range=[-200,+200])
#     plt.show()

    # plt.plot(audiodata)
    # plt.show()

    return file
# message = 'Select audio file.';
# path = fileopenbox(message)
# file=audio_load(path)

## program start from this function
def read_music_fileName():
    message = 'Select audio file.';
    path = fileopenbox(message)
    dirName = os.path.dirname(path)
    file_list = [entry for entry in os.scandir(dirName) if entry.is_file()]
    #[entry for entry in os.scandir(os.getcwd()) if entry.is_file()]
    for fl in file_list:
        wav_file = audio_load(fl.path)
        ad.Data_Tbl_toSaveInExcel(wav_file,dirName)


read_music_fileName()