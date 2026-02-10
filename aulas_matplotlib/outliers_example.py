import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('matplotlib/titanic.csv')

sns.boxplot(x=df['age'])

plt.show()