import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook



df = pd.read_csv('data/Names.csv', header=None)

df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', "Income"]

# Filter
wanted = df.loc[(df['City'] == 'Riverside') & (df['First'] == 'John')]

print(wanted)

## Add column
df['Tax %'] = df['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .2 if 40000< x < 80000 else .25)

df['Tax owed'] = df['Tax %'] * df['Income']

print(df['Tax owed'])

## Drop columns 
to_drop = ['First', 'Address']
df.drop(columns=to_drop, inplace=True)
print(df)

## Modify column
df['Test Col'] = False
print(df)
df.loc[df['Income'] < 60000, 'Test Col'] = True
print(df)

## Gropu and colculate in group
print(df.groupby(['Test Col']).mean())

## Sort
print(df.groupby(['Test Col']).mean().sort_values('Income'))

## Add Index
df = df.set_index('Area Code')
print(df.loc[8074])
print(df.iloc[0])

## Replace
df = df.replace(np.nan , 'N/A', regex =True)