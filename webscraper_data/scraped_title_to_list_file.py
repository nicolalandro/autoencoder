import pandas as pd

data = pd.read_csv('tp_all.csv')

with open('../input_data.txt', 'w') as outfile:
    for i, row in data.iterrows():
        title = row['title']
        if type(title) is str:
            for w in title.split(' '):
                word = w + '\n'
                outfile.writelines(word)
