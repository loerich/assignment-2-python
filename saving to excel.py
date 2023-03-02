import xlwt
from xlwt import Workbook
wb =Workbook()
sheet1=wb.add_sheet('sheet 1')
sheet1.write(1,0,'bananas iris golf')


wb.save('xlt examples.xls')


