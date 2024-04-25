import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

iris=pd.read_csv('/content/iris.csv')


sns.heatmap(iris.corr(numeric_only=True), annot=True, cmap='summer')
plt.show()
