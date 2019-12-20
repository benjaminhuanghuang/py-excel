import pandas as pd
from openpyxl.workbook import Workbook


df_excel = pd.read_excel('data/regions.xlsx')
print(df_excel)


df_csv = pd.read_csv('data/Names.csv', header=None)
print(df_csv)

# Add column headers
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', "Number"]
# Save to excel file
df_csv.to_excel('target/modified.xlsx')

df_txt = pd.read_csv('data/data.txt', delimiter='\t')
print(df_txt)
