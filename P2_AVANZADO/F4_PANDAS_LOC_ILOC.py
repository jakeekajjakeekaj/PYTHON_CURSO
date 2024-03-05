#LOC, ILOC

import pandas as pd;

df = pd.read_csv("P2_AVANZADO\\E_CSV.csv");

elemento_especifico_loc = df.loc[1, "edad"];    #De esta manera obtenemos un dato específico, le indicamos que obtenga la información de nuestra fila en la posición 1, de la columna "edad", ES IMPORTANTE MENCIONAR QUE EN LAS FILAS SOLO SE ADMITEN A LOS ENCABEZADOS NOMBRADOS, SI SE QUIERE INDICAR POR MEDIO DE SU NUMERO, SE UTILIZA LO DE ABAJO

print(elemento_especifico_loc); #36

elemento_especifico_iloc = df.iloc[1, 1];   #Con iloc accedemos solo con los índices, de hecho iloc hace referencia a indexed loc, esto quiere decir que al indicar ambos numeros ya nos arrojaría un resultado filtrado

print(elemento_especifico_iloc);    #Lopez

apellidos = df.iloc[:,1];   #De esta manera obtenemos todos los valores de una columna
print(apellidos);

fila_2 = df.iloc[2,:];  #De esta manera obtenemos todos los valores de una fila
print(fila_2);

#Si queremos aplicar un filtro de ocndicional, por ejemplo filtrando a las edades mayores a 30, se tiene que:
mayor_que_30 = df.loc[df["edad"]>30,:]; #De esta manra se obtiene el filtro de las edades mayores que 30; a su vez se tiene que escribir de la manera df["edad"], ya que si solo lo dejamos como "edad", no se leería el operador >
print(mayor_que_30);