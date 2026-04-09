import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

djia_data = pd.read_csv('Session_2/geeksforgeeks/Pandas Introduction/historical_data.csv')

#print(djia_data.head())

djia_data = djia_data.rename(columns = {' Open': 'Open', ' High': 'High', ' Low': 'Low', ' Close': 'Close'})

#print(djia_data.head())

djia_data['Date'] = pd.to_datetime(djia_data['Date'], format='%m/%d/%y')
djia_data = djia_data.sort_values(by = 'Date')

#print(djia_data.head())

plt.scatter(djia_data['Date'], djia_data['Open'])
plt.scatter(djia_data['Date'], djia_data['Close'])
plt.legend()
#plt.show()

plt.savefig("djia_plot.png")
print("Graf sparad som djia_plot.png!")