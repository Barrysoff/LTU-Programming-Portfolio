import pandas as pd
import numpy as np

data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}
df = pd.DataFrame(data1)
print(df)
print()

df.groupby('Name')
print(df.groupby('Name').groups)
print()

gk = df.groupby('Name')
print(gk.first())
print()

df.groupby(['Name', 'Qualification'])
print(df.groupby(['Name', 'Qualification']).groups)
print()

print(df.groupby('Name')['Age'].sum())
print()

grp = df.groupby('Name')
for name, group in grp:
    print(name)
    print(group)
    print()

print()

grp = df.groupby(['Name', 'Qualification'])
for name, group in grp:
    print(name)
    print(group)
    print()

print()

grp = df.groupby('Name')
print(grp.get_group('Jai'))

print()

grp1 = df.groupby('Name')
print(grp1['Age'].aggregate(np.sum))