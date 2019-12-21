from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.drawing.image import Image
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

wb = load_workbook('data/Pie.xlsx')
ws = wb.active

tab = Table(displayName='Table1', ref='A1:B5')

style = TableStyleInfo(name='TableStyleMedium9', 
showFirstColumn =False,
showLastColumn=False,
showRowStripes=True,
showColumnStripes=True)

tab.tabelStyle = style
ws.add_table(tab)
wb.save('target/table.xlsx')


