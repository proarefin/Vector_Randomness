import pandas as pd
import csv
import numpy as np
import xlsxwriter
import os.path
from openpyxl import load_workbook


def save_csv(data,indx_for_csv,col_name,win_size,fileName):
    csvData = data
    with open('tbl_window.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)
    csvFile.close()
    # list of strings
    lst = ['Geeks', 'For', 'Geeks', 'is',
           'portal', 'for', 'Geeks']
    index=col_name#indx_for_csv
       # Calling DataFrame constructor on list
    #d = {'Win_' + str(count=count+1): pd.Series(row, index),
    #   'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c'])}
    #da=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    columns = indx_for_csv#col_name
    path='instrument_'+ str(fileName) + '.xlsx'
    df = pd.DataFrame(data,index,columns)
    #df.to_csv(r'tbl_window_Datafram.csv', index=True, header=col_name)
    if os.path.isfile(path):
        # df=pd.read_excel(open('instrument_'+ str(fileName) + '.xlsx'), sheet_name=None)
        # with pd.ExcelWriter('instrument_'+ str(fileName) + '.xlsx') as writer:  # doctest: +SKIP
        #     df1.to_excel(writer, sheet_name='Sheet_name_1')
        #     df2.to_excel(writer, sheet_name='Sheet_name_2')
        book = load_workbook(path)
        writer = pd.ExcelWriter(path, engine='openpyxl')
        writer.book = book

        df.to_excel(writer, sheet_name='Win_'+str(win_size), engine='xlsxwriter')
        writer.save()
        writer.close()
    else:
        df.to_excel(path, sheet_name='Win_'+str(win_size), engine='xlsxwriter') #single instrument's single music with different window size and padding.
    # pd.concat(df).to_csv('tbl_window_Datafram.csv')
    print(df)


#data = [[1, 2], [2, 4], [5, 6]]
#save_csv(data,indx_for_csv=['10','20','30'],col_name=['w1','w2'])
