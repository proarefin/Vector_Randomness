import pandas as pd
import csv
import numpy as np
import xlsxwriter
import os.path
from openpyxl import load_workbook
import os

def Save_InExcel(data,indx_for_csv,col_name,win_size,fileName,dirName):
    index=col_name                              #Row Names
    columns = indx_for_csv                      #column Names
    dir=str(dirName)+'\\Data_inExcel\\'
    path=str(dir)+'instrument_floor'+ str(fileName) + '.xlsx'
    df = pd.DataFrame(data,index,columns)
    img_Dir = dir + fileName;
    #df.to_csv(r'tbl_window_Datafram.csv', index=True, header=col_name)
    if os.path.isfile(path): #Update Excel with adding new sheets
        # df=pd.read_excel(open('instrument_'+ str(fileName) + '.xlsx'), sheet_name=None)
        # with pd.ExcelWriter('instrument_'+ str(fileName) + '.xlsx') as writer:  # doctest: +SKIP
        #     df1.to_excel(writer, sheet_name='Sheet_name_1')
        #     df2.to_excel(writer, sheet_name='Sheet_name_2')
        book = load_workbook(path)
        writer = pd.ExcelWriter(path, engine='openpyxl')
        writer.book = book

       # worksheet = writer.sheets['Win_Size-' + str(win_size)]

        df.to_excel(writer, sheet_name='Win_Size-'+str(win_size), engine='xlsxwriter')
        #
        # workbook = writer.book
        # worksheet = writer.sheets['Win_Size-'+str(win_size)]
        # # Create a chart object.
        # chart = writer.book.add_chart({'type': 'column'})
        # # Configure the series of the chart from the dataframe data.
        # chart.add_series({'values': '=Win_Size-'+str(win_size)+'!$B$2:$B$8'})
        # # Insert the chart into the worksheet.
        # worksheet.insert_chart('D2', chart)

        writer.save()
        writer.close()
    else: # Create the Excel with a first sheet.
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(path, engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name='Win_Size-'+str(win_size))

        # Get the xlsxwriter objects from the dataframe writer object.
        workbook = writer.book
        worksheet = writer.sheets['Win_Size-'+str(win_size)]

        # Create a chart object.
        worksheet.insert_image('AA2', img_Dir+'_Avg_ch.png')
        workbook.close()
        writer.save();
        writer.close()
        #df.to_excel(path, sheet_name='Win_Size-'+str(win_size), engine='xlsxwriter') #single instrument's single music with different window size and padding.

    # pd.concat(df).to_csv('tbl_window_Datafram.csv')
    #print(df)


#data = [[1, 2], [2, 4], [5, 6]]
#Save_InExcel(data,indx_for_csv=['10','20','30'],col_name=['w1','w2'])

    # csvData = data
    # with open('tbl_window.csv', 'w') as csvFile:
    #     writer = csv.writer(csvFile)
    #     writer.writerows(csvData)
    # csvFile.close()
    # # list of strings
    # lst = ['Geeks', 'For', 'Geeks', 'is',
    #        'portal', 'for', 'Geeks']
    #    # Calling DataFrame constructor on list
    # #d = {'Win_' + str(count=count+1): pd.Series(row, index),
    # #   'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c'])}
    # #da=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])