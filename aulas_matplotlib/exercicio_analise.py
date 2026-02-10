import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('matplotlib/icecreams.csv')

sorted_df = df.sort_values(by='Temperature', ascending=True)
print(sorted_df)