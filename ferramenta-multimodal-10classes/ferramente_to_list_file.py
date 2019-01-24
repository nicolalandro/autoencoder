import pandas as pd

data = pd.read_csv('train.csv', sep='\t')

with open('../input_data.txt', 'w') as outfile:
    for i, row in data.iterrows():
        text = str(row['prodotto']) + ' ' + str(row['descrizione']) + '\n'
        outfile.writelines(text)
