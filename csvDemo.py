import pandas as pd
from openpyxl.workbook import Workbook



df_csv = pd.read_csv('data/Names.csv', header=None)
#print(df_csv)

# Add column headers
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', "Number"]

print(df_csv.columns)

print(df_csv['Last'])

print(df_csv[['State' ,'Area Code']])

print(df_csv['Last'][0:3])

# Using iloc function to access data row, or cell
print(df_csv.iloc[1])
print(df_csv.iloc[1, 2])


# Pick data
wanted_values = df_csc[['First', 'Last', 'State']]
# Save to excel file
wanted_values.to_excel('target/modified.xlsx')




