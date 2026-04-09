import pandas as pd

list = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c", "d"]
list3 = [1, False, "Bulle"]

dict = {"Ett": 1, "Två": 2, "Tre": 3}

s = pd.Series(dict)

s1 = pd.Series(data=list, index=[1, 2, 3, 4, 5, 6])

s1[2] = 9800

s2 = s.drop(labels=["Tre"])

print(s2,"\n",s)