import pandas as pd
import matplotlib.pyplot as plt


data = {"Education": ["Highscool", "BS", "Master", "PhD", "Master", "BS", "Highscool", "PhD"],
        "Income": [20000, 50000, 70000, 200000, 81919, 59020, 28289, 100000]}
df = pd.DataFrame(data)

df['Education'] = pd.Categorical(df['Education'])

grouped = df.groupby("Education")["Income"].mean()
print(grouped)

fig, ax = plt.subplots(1,1)
ax.bar(grouped.index, grouped.values/1000, color='skyblue')

ax.grid(visible=True, color="grey", linestyle="-.", linewidth=0.5, alpha=0.2, axis="y")

ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False) 
ax.set_title("Average Income based on Education level")
ax.set_xlabel("Education Level")
ax.set_ylabel("Average Income in thousends of $")
plt.show()

#print(df["Income"].mean())
