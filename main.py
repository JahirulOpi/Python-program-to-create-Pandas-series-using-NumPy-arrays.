import numpy as np
import pandas as pd

x = np.array([1, 2, 3, 4, 5])
y = np.array(["a", "b", "c", "d", "e"])

series = pd.Series(data = x, index = y)

print(series)
