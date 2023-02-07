from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass
class People():
    name:str
    num:int
    age:int
# p=People('Nabeelaa','5','21')
p=[People('Nabeelaa',1,21),People('zak',2,22),People('san',3,21),People('zuff',4,22)]
data=[[p.name,p.num,p.age]for p in p]
data=[['Name','Num','Age']]+data
for d in data:
    sheet.append(d)
wb.save('C://Users/user794/Documents/dtclassdemo.xlsx')
# print(p)