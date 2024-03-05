import pandas as pd;

df = pd.read_csv("P2_AVANZADO\\E_CSV.csv");

cadena = "0123456789";  #Aquí se declara una cadena oara usar la técnica del slicing
print(cadena[:3]);  #Aquí se indica que se empezará desde la posición 0 hasta la posición 3, es decir que imprimirá los valores 0, 1, 2

print(cadena[1:3]); #Aquí se indica que se empezará desde la posición 1 hasta la posición 3, es decir que imprimirá los valores 1, 2