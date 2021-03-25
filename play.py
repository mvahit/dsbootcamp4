from dsbootcamp4.hi import hello, hello2
# from dsbootcamp4.hi import *

hello()

hello2()


from dsbootcamp4.eda.eda import check_df

import seaborn as sns
df = sns.load_dataset("tips")

check_df(df)

import dsbootcamp4

help(dsbootcamp4)

help(dsbootcamp4.eda)

import dsbootcamp4.data_prep

help(dsbootcamp4.data_prep)

help(dsbootcamp4.eda.eda)
import pandas as pd
help(pd.tseries)


