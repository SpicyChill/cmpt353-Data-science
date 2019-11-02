import time
import numpy as np
import pandas as pd
from implementations import all_implementations
# ...
data = pd.DataFrame(columns=['qs1', 'qs2', 'qs3', 'qs4', 'qs5', 'merge1', 'partition_sort'],index=np.arange(100))


for i in range(100):
    random_array = np.random.rand(10000)
    for sort in all_implementations:
        st = time.time()
        res = sort(random_array)
        en = time.time()
        num = en - st
        data.iloc[i][sort.__name__] = num



data.to_csv('data.csv', index=False)