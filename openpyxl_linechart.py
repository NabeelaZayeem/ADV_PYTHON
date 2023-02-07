from openpyxl import Workbook
from openpyxl.chart import LineChart ,Reference
wb=Workbook()
sheet=wb.active
sales_data=[[ "Year" ," Sales" ],
            [2010,1000],
            [2011,2005],
            [2012,5010],
            [2013,4000],
            [2014,5020],
            [2015,6000],
            [2016,4020]
    ]
for row in sales_data:
    sheet.append(row)
chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2
,max_col=3  )
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save('C://Users/user794/Documents/openpyxl_Linechart.xlsx')
