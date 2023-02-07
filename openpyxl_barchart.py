from openpyxl import Workbook
from openpyxl.chart import BarChart ,Reference
wb=Workbook()
sheet=wb.active
sales_data=[[ "product" ," Sales" ," Store"],
            [1,30,45],
            [2,40,30],
            [3,50,60],
            [4,50,30],
            [5,60,70],
            [6,40,25],
            [7,50,40]
    ]
for row in sales_data:
    sheet.append(row)
chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2
,max_col=3  )
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")


wb.save('C://Users/user794/Documents/openpyxl_Barchart.xlsx')
