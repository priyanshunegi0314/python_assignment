import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": [22, 25, 30, 28, 40, 50, 35, 45, 38, 29],
    "BMI": [18, 22, 27, 25, 31, 29, 26, 33, 28, 24],
    "Steps": [5000, 7000, 6000, 8000, 3000, 2000, 9000, 4000, 7500, 6500]
})

df["BMI"].hist()
plt.show()

sns.boxplot(df["Steps"])
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.show()
