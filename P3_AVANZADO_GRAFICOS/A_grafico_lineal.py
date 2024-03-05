import pandas as pd;
import matplotlib.pyplot as plt;    #Librería para visualizar datos de forma gráfica, si no se tiene instalado, se debe ir al cmd y escribir py -m pip install matplotlib
import seaborn as sns;  #Librería de gráficos estadísticos, si no se tiene instalado hacer lo mismo de arriba, pero esta vez escribiendo seaborn

df = pd.read_csv("P3_AVANZADO_GRAFICOS\\A_chocolates.csv"); #Accedemos a nuestro csv

sns.lineplot(x = "fecha", y = "chocolates", data = df); #Aquí usamos la librería seaborn, de esta manera indicamos que en el eje x irá fecha, en el eje y irá chocolates, y la información será proveniente de df (data frame); de igual manera para definir que sea un gráfico lineal, se debe escribir lineplot

plt.plot("01-09", 17, "o"); #De esta manera indicamos que en el valor x 01-09 y en el valor y 17, se escribirá una o simulando un punto e indicando el valor más alto

plt.show(); #De esta manera se muestra al gráfico