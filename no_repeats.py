import pandas as pd

data = pd.read_csv('TTT_dataset.csv')
data = data.drop_duplicates()
data.to_csv('TTT_dataset.csv')

print('TTT_dataset.csv has no repeats')
