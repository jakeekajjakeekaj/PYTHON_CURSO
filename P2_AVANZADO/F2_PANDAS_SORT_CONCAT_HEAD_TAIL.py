#SORT, CONCAT, HEAD, TAIL

#HEAD ES PARA FILTRAR A LAS FILAS, EN VEZ DE HACERLO POR EL MÉTODO DE ENCABEZADOS EN DONDE SOLO FUNCIONA PARA COLUMNAS, SE USA HEAD PARA LAS FILAS
#TAIL ES COMO HEAD, PERO EN VEZ DE BUSCAR DESDE LAS PRIMERAS FILAS, ESTE LO HACE DESDE LAS ULTIMAS FILAS
import pandas as pd;

df = pd.read_csv("P2_AVANZADO\\E_CSV.csv");
df2 = pd.read_csv("P2_AVANZADO\\E_CSV.csv");

df_ordenado = df.sort_values("edad");   #De esta manera dentro de una variable data frame ordenado, almacenamos el contenido del csv en orden ascendente dependiendo de la edad

print(df_ordenado); #Se imprime el data frame ordenado

df_descendente = df.sort_values("edad", ascending=False);   #De esta manera se obtiene el orden descendente, únicamnte tenemos que marcar al ascendente como False

print(df_descendente);  #Se imprime el data frame en orden descendente

df_concatenado = pd.concat([df, df2, df_descendente]);  #De esta manera se concatena a los data frames

print(df_concatenado);  #Se imprime la concatenación de los data frames

primer_fila = df.head(1);   #De esta manera se filtra a las filas, al colocar 1, se obtiene el encabezado y la fila 1; y así sucesivamente

print(primer_fila);

ultimas_filas = df.tail(1); #De esta manera es como usar head, solo que en vez de hacerlo desde el principio, ahora lo hace desde el final

print(ultimas_filas);