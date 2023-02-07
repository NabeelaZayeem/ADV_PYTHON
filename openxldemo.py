import openpyxl
wb=openpyxl.load_workbook('C://Users/user794/Documents/marks.csv')
sheet=wb.active
data=sheet['A3'].value
data3=sheet.cell(row=2,column=3).value
