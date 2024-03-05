import csv; #De esta manera mandamos a llamar a la librería de csv

with open("P2_AVANZADO\\E_CSV.csv") as archivo:
    # print(archivo.read());    #Si usamos esta sintaxis, nos lee el contenido, pero lo lee como si estuviera e un .txt
    print(csv.reader(archivo)); #De esta manera nos arroja el objeto