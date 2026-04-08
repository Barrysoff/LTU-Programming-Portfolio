import pandas as pd

filnamn = "Session_2/smhi_data/ECA_kommun_tmean_w41.csv"

data = pd.read_csv(filnamn, index_col="kommun")
names = pd.read_csv("Session_2/smhi_data/kommun_names.csv", sep=';', index_col="id")
names = names.sort_index()

data['tmean'] = data['tmean'] / 10
data['tmax'] = data['tmax'] / 10
data['tmin'] = data['tmin'] / 10


# Find the 10 most humid kommuner. Print their names.

data = data.sort_values(['humidity'], ascending=False)

topp_10_data = data.head(10)

topp_10_komplett = topp_10_data.join(names)

namn_lista = topp_10_komplett['label'].tolist()

print("De tio fuktigaste kommunerna är:")
for namn in namn_lista:
    print(f"- {namn}")
print()


# Find the kommun with the median humidity. List all kommuner with humidity lesser than the median.

median_kommuner = (data[data['humidity'] == data['humidity'].median()])
median_kommuner_komplett = median_kommuner.join(names)
namn_lista_median = median_kommuner_komplett['label'].tolist()

print("De kommuner som utgör medianen är:")
for namn in namn_lista_median:
    print(f"- {namn}")
print()

torra_kommuner = (data[data['humidity'] < data['humidity'].median()])
torra_kommuner_komplett = torra_kommuner.join(names)
namn_lista_torr = torra_kommuner_komplett['label'].tolist()

print("De torraste kommunerna är:")
for namn in namn_lista_torr:
    print(f"- {namn}")
print()


# Which kommun saw the largest difference in mean temperatures during the period?