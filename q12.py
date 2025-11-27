import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": [20,25,30,35,40,45],
    "Gender": ["M","F","M","F","M","F"],
    "Steps_per_day": [6000,8000,4000,7000,3000,5000],
    "Sleep_Hours": [7,6,8,5,6,7],
    "BMI": [22,25,28,30,32,27],
    "Workout_minutes": [30,45,20,40,10,25]
})

df.fillna(df.mean(), inplace=True)

print(df[["Workout_minutes","BMI","Sleep_Hours"]].corr())

df["Steps_per_day"].hist()
plt.show()

plt.scatter(df["Workout_minutes"], df["BMI"])
plt.xlabel("Workout Minutes")
plt.ylabel("BMI")
plt.show()
