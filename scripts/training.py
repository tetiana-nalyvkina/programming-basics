file0 = open('data/samples.csv')

import pandas as pd
df = pd.read_csv('data/samples.csv')
print(df.mean)