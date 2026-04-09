import pandas as pd

dict = {'Fruit': ["Apple", "Banana", "Citrus"], 'Amount': [1, 80, 12], 'Price': [100, 40, 60]}

df = pd.DataFrame(dict)

# print(df)

column = df[(df['Amount'] > 10) & (df['Price'] > 50)]

# print(column)

row = df.loc[[1, 0]]

# print(row)

df2 = df.set_index('Fruit')

# row = df2.loc[["Apple", "Banana"]]

# print(df2)

df2 = df2.reset_index()

# print(df2)

df["Weight"] = [0.3, 4, 0.9]

#print(df)

df.loc[3] = ["Cherry", 7, 23, 0.01]

print(df)

df3 = df.drop(columns=["Price"])

print(df3)