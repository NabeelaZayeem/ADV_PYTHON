import openpyxl
import pandas as pd
from pandas import read_excel

from openpyxl import Workbook

from openpyxl.chart import LineChart ,Reference
wb=openpyxl.Workbook
# exldata1=pd.read_excel('C://Users/user794/Documents/sales_monthwise.xlsx',sheet_name='SALES_JAN')
# print(exldata1)
wb=openpyxl.load_workbook('C://Users/user794/Documents/sales_monthwise.xlsx')
sheet=wb.active
# sheet['A1:A6']
chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=6,min_col=1
,max_col=1 )
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save('C://Users/user794/Documents/sales_monthwise1.xlsx')
# sheet=workbook.active
