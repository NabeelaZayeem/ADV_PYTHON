import openpyxl
from openpyxl.utils import FORMULAE
wb=openpyxl.load_workbook('C://Users/user794/Documents/dataformula.xlsx')
sheet=wb.active
sheet['A7']='=SUM(A1:A6)'
# wb.save('C://Users/user794/Documents/dataformula.xlsx') #applying formula and saving result in same file
wb.save('C://Users/user794/Documents/newsheet.xlsx')# after addition saving result in another file


