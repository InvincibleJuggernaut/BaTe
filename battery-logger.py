from xlrd import open_workbook
from xlutils.copy import copy
import xlwt

file="battery-report.html"
html_file=open(file,'r')
source_code=html_file.read()
report_day_title=source_code.find('REPORT TIME')
report_day=source_code[report_day_title+66:report_day_title+76]

report_time=source_code[report_day_title+103:report_day_title+111]

full_charge_title=source_code.find('FULL CHARGE CAPACITY')
full_charge=source_code[full_charge_title+36:full_charge_title+46]

excel_file='battery-stats.xlsx'
wb=open_workbook(excel_file)
sheet=wb.sheet_by_name('Sheet1')
data=copy(wb)
rows=sheet.nrows

current_row=rows
worksheet=data.get_sheet('Sheet1')
worksheet.write(current_row,0,report_day)
worksheet.write(current_row,1,report_time)
worksheet.write(current_row,2,full_charge)

data.save(excel_file)

print("Logged successfully")
