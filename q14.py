import numpy as np
import pandas as pd
from scipy import stats

data = [50,52,49,55,60,500,48,51,53,49]   
df = pd.DataFrame(data, columns=["Amount"])

df["z"] = np.abs(stats.zscore(df["Amount"]))
z_outliers = df[df["z"] > 3]

Q1 = df["Amount"].quantile(0.25)
Q3 = df["Amount"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
iqr_outliers = df[(df["Amount"] < lower) | (df["Amount"] > upper)]

print(z_outliers)
print(iqr_outliers)

df["Corrected"] = np.where(df["Amount"] > upper, upper, df["Amount"])
