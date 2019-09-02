import os
from easygui import *
import ntpath
from audio_Randomness import Data_Tbl_toSaveInExcel as DS #data Store

message = 'Select audio file.';
path = fileopenbox(message)
dirName = os.path.dirname(path)
[entry for entry in os.scandir(dirName) if entry.is_file()]
file_list=[entry for entry in os.scandir(os.getcwd()) if entry.is_file()]
for fl in file_list:
    wav_file=al.audio_load()
    ds(wav_file)
#print(fl.count(),fl[0].name)