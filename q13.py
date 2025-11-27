import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": [22,25,29,40,50,33,45,38,28,30],
    "Income": [25,35,40,50,80,60,75,55,42,48],
    "Expenses": [10,15,18,25,40,30,35,20,16,22]
})

# 1. Missing values
df.fillna(df.mean(), inplace=True)

# 2. Outliers
sns.boxplot(df["Income"])
plt.show()

# 3. Stats
print(df.describe())

# 4. Histogram
df["Age"].hist(); plt.show()

# 5. Boxplot
sns.boxplot(df["Expenses"]); plt.show()

# 6. Heatmap
sns.heatmap(df.corr(), annot=True); plt.show()
