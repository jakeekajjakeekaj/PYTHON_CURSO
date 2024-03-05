#*** ES IMPORTANTE MENCIONAR QUE LOS .CSV NO DEBEN LLEVAR ESPACIOS EN BLANCO, ES DECIR QUE TODO DEBE SER ESCRITO ENTRE COMILLAS Y JUNTO; ASI MISMO LAS COMAS SON REFERENCIA A NUEVOS VALORES, POR LO QUE SI COLOCAMOS COMAS AL FINAL DE CADA FILA, SE TOMARÁ COMO SI HUBIERA ALGO EXTRA, COSA QUE ESTÁ MAL, LAS COMAS SOLO DEBEN SEPARAR ELEMENTOS DE CADA FILA ***

import csv; #De esta manera mandamos a llamar a la librería de csv

with open("P2_AVANZADO\\E_CSV.csv") as archivo:
    # print(archivo.read());    #Si usamos esta sintaxis, nos lee el contenido, pero lo lee como si estuviera e un .txt
    # print(csv.reader(archivo)); #De esta manera nos arroja el objeto
    reader = csv.reader(archivo);   #Lo mismo de arriba pero asignado a una variable
    for row in reader:
        print(row); #Imprime el conenido del .csv en forma de arreglo

#A pesar de que esto funciona, no se recomienda del todo leer el contenido con esta librería, se recomienda que sea con una librería llamada 'pandas'