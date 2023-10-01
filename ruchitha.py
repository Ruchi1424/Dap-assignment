import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("TIMES_WorldUniversityRankings_2024.csv")
dataframe = pd.DataFrame(data)
dfh = dataframe.head(20)
dfh.plot(x="name", y="scores_citations_rank",
         kind="bar", title="University citation ranks")
plt.show()