import openpyxl
workbook=openpyxl.Workbook
sheet=workbook.active
for row in data:
    sheet.append(row)
workbook