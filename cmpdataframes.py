import pandas as pd
import numpy as np

data1=pd.read_excel('C://Users/user794/Documents/CMP.xlsx',sheet_name='Sheet1')
data2=pd.read_excel('C://Users/user794/Documents/CMP.xlsx',sheet_name='Sheet2')
# print(data1)
# data3=np.where(data1['price']==data2['price'],True,False)
# print(data1.compare(data2))
# print(data3)
# data4=np.where(data1['price']==data2['price'],True,data2['price']-data1['price'])
# print(data4)
data1.to_excel('C://Users/user794/Documents/price1.xlsx',sheet_name='price_list',index=False)
print(data1.to_dict())
print(data1.to_html('demo.html'))