from openpyxl import load_workbook
from openpyxl.drawing.image import Image
workbook=load_workbook(filename='C://Users/user794/Documents/dataformula.xlsx')
sheet=workbook.active
logo=Image('C://Users/user794/image1.png')
logo.height=150
logo.width=150
sheet.add_image(logo,"D10")
workbook.save("C://Users/user794/image1.xlsx")