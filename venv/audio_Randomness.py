
import audio_load as al
import matplotlib.pyplot as plt
import numpy as np
import store_tbl_result


col_name=[];indx_for_csv=[];
def tbl_dot_result_win():
    crt_dynamic_var=globals() # crt_dynamic_var['window_{0}'.format(1)]=0
    wav_file= al.audio_load()
    signal=np.array(wav_file['signal']);  fs=wav_file['fs']; fileName=wav_file['name'];
    # plt.plot(signal)
    # plt.show()
    signal_size=signal.size
    length=int(signal_size/fs)

    window_size=1024*8 # (4410/44100)*1000: 100 ms window
    #calculated number of windows
    total_windows=int(signal_size/window_size)
    index_start=0
    index_end=window_size
    #win_seg_count=0
    padding_value=10 #number of zero's
    tbl_window_500=np.array([]); col_name=[];indx_for_csv=[];
    stop_range=250; str_range=10; step_range=10; window_tbl=np.empty((0,2))
    #for Each window segment.
    for count_win in range(total_windows): #(win_seg_count < total_windows-1):
        tbl_win_row=np.empty((0,1), float)
        window = signal[index_start:index_end]
        #tbl_window_row = np.array([])
        indx_for_csv=[]; col_name.append('win_'+ str(count_win))
        for pad_val in range(str_range, stop_range, step_range):                    #loop: Padding values range; Ex: 10,20,30....100
            bottom_padded_10=np.pad(window,(0,pad_val),'constant')                  #bottom-padded by 10 zeros
            top_padded_10 = np.pad(window, (pad_val,0), 'constant')                 #top-padded by 10 zeros
            vec_dotProduct_result=(top_padded_10 * bottom_padded_10).sum(axis=0);   #dot product calculation
            tbl_win_row=np.append(tbl_win_row, vec_dotProduct_result)               #Creating A row-table
            indx_for_csv.append(str(pad_val))
        if window_tbl.size == 0:
            window_tbl=np.array(tbl_win_row)                                        #Table First row
        else:
    # Collect dot results in a table repeatedly: row: Window segments; col: padding (10,20,30.....)
            window_tbl = np.vstack((window_tbl,tbl_win_row))
        index_start=index_end
        index_end+=window_size
        #win_seg_count += 1
    tbl_final=window_tbl
    return tbl_final, indx_for_csv, col_name, fileName, window_size

csv_Data,indx_for_csv, col_name, fileName, window_size =tbl_dot_result_win()
store_tbl_result.save_csv(csv_Data,indx_for_csv,col_name,window_size,fileName)
#print(tbl_dot_result_win())

# t=np.arange(signal.size)/float(fs)
# plt.plot(t,signal)
# plt.show()
#
# waveFile = wave.open(path, 'rb')
# data, sampleRate= sf.read
#
# sample_width = waveFile.getsampwidth()
# fs=waveFile.getframerate()
# frames=waveFile.readframes()
# waveFile.close()
