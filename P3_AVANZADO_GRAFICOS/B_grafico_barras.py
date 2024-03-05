import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

df = pd.read_csv("P3_AVANZADO_GRAFICOS\\B_cofla_ingresos.csv");

sns.barplot(x = "fuente", y = "ingresos", data = df);   #Para definir que sea un grafico de barras, se debe colocar barplot

total_ingresos = df['ingresos'].sum();  #De esta manera se obtiene el total de ingresos

print(f"El total de ingresos es de ${total_ingresos} USD");

plt.show();