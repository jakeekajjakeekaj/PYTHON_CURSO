import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

df = pd.read_csv("P3_AVANZADO_GRAFICOS\\D_bigotes.csv");

sns.boxplot(x = "categoria", y = "valor", data = df);   #De esta manera se crea el diagrama de cajas, que es escribiendo boxplot

plt.show();