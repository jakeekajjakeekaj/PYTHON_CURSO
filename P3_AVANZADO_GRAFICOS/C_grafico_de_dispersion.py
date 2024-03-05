import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

df = pd.read_csv("P3_AVANZADO_GRAFICOS\\C_dispersion.csv");

sns.scatterplot(x = "tiempo", y = "dinero", data = df); #Para el grafico de dispresion se esribe scatterplot

plt.show();