import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import sys

newfile = sys.argv[1]

dataframe = pd.read_csv(newfile)

anova = stats.f_oneway(dataframe['qs1'], dataframe['qs2'], dataframe['qs3'], dataframe['qs4'], dataframe['qs5'], dataframe['merge1'], dataframe['partition_sort'])
data_melt = pd.melt(dataframe)
data_melt['value'] = data_melt['value'].astype('float64')

posthoc = pairwise_tukeyhsd(
    data_melt['value'], data_melt['variable'], alpha=0.05)

print(posthoc)

fig = posthoc.plot_simultaneous()