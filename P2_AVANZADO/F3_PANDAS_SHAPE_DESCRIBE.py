#SHAPE, DESCRIBE

#SHAPE SE ENCARGA DE OBTENER LA CANTIDAD DE FILAS O COLUMNAS QUE SE ENCUENTRAN
#DESCRIBE ES USADO MAYORMENTE PARA ANÁLISIS DE DATOS, POR LO QUE AHORITA NO SE VERÁ A FONDO

import pandas as pd;

df = pd.read_csv("P2_AVANZADO\\E_CSV.csv");

print(df);  #Imprimimos el data frame para observar las filas y columnas

# filas_y_columnas_totales = df.shape;    #De esta manera obtenemos el valor de las filas y columnas totales

# print(filas_y_columnas_totales);    #3, 3

#Si nosotros quisiéramos obtener el valor individual, sería tan simple como escribir:
# filas_totales = filas_y_columnas_totales[0];    #De esta manera se obtiene el total de las filas
# print(filas_totales);   #3

# columnas_totales = filas_y_columnas_totales[1]; #De esta manera se obtiene el total de las columnas
# print(columnas_totales);    #3

#OTRA MANERA E OBTENER LAS FILAS Y COLUMNAS TOTALES, ES DESEMPAQUETÁNDOLAS, ES DECIR:

filas_totales, columnas_totales = df.shape; #De esta manera desempaquetamos y obtenemos los valores de las filas totales y las columnas totales

print(filas_totales);   #3

print(columnas_totales);    #3

df_info = df.describe();    #Esto sirve mayormente para análisis de datos

print(df_info);