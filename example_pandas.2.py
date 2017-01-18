
import csv
import codecs
import pandas as pd
import numpy as np


listok=[]
''', parse_dates=['CDR date'], dayfirst=True'''
with codecs.open("report.csv", "r", "utf-8") as csvfile:
    country_reader=pd.read_csv(csvfile,delimiter=';' ,parse_dates=[0] )
    for row in country_reader:
                   listok.append(row)
'''CDR_date=[]
lengh=1
for line in range(lengh):
    temp=country_reader['CDR date'][lengh]
    temp=temp.date()
    #country_reader['CDR date'][lengh]=0'''

country_reader['CDR date']=country_reader['CDR date'].dt.date    
    
duration_1=country_reader.pivot_table(
    values=['Duration', 
            'Customer price System currency Ext',
            'Vendor cost System currency Ext'],
    index=['CDR date','Vendor'],
    aggfunc='sum', fill_value = 0)

duration_2=list(duration_1)


import os
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook

from openpyxl.cell.cell import WriteOnlyCell
wb = Workbook(write_only=True)
ws = wb.create_sheet()



#wb.save("openpyxl_stream.xlsx")