import pandas as pd;

df = pd.read_csv("P2_AVANZADO\\E_CSV_MODIFICADO.csv");
df['edad'] = df['edad'].astype(str);    #Esto cambia el tipo de dato de una columna, para este caso se convierte en string
print(df['edad']);

df['nombre'].replace("Pepe", "Pepe Modificado", inplace=True);  #De esta manera se reemplazan los datos, para este caso estamos indicando que de la columna 'nombre', reemplazar el nombre de "Pepe" por "Pepe Modificado", y con el inplace=True, cerramos la función
print(df);

df = df.dropna();   #De esta manera eliminamos filas con datos faltantes
print(df);

df = df.dropna(axis=1); #De esta manera eliminamos las columnas con datos faltantes *** POR DEFECTO EL AXIS TIENE UN VALOR DE 0, POR ESO NO ES NECESARIO COLOCARLO PARA EL CASO DE LAS FILAS, PERO SI QUEREMOS HACERLO CON LAS COLUMNAS SE TIENE QUE COLOCAR EL axis=1
print(df);

df = df.drop_duplicates();  #De esta manera se eliminan los datos duplicados
print(df);

df.to_csv("P2_AVANZADO\\EJERCICIOS_PRACTICOS\\A_F_mini_datos_limpios.csv"); #De esta manera se crea un CSV, para este caso por ejemplo ya con toda la información corregida