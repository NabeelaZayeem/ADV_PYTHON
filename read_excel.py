import pandas as pd
exldata1=pd.read_excel('C://Users/user794/Documents/myexcel.xlsx',sheet_name='Emp')
print(exldata1)
exldata2=pd.read_excel('C://Users/user794/Documents/myexcel.xlsx',sheet_name='department')
print(exldata2)
exldata1.to_html
exldata3=pd.concat([exldata1,exldata2]) #concatinating two sheets
print(exldata3)