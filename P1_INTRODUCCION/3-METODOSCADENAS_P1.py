#MÉTODOS DE CADENAS

cadena1 = "Soy la Cadena 1";
cadena2 = "y esta es la cadena 2 :D";

# print(dir(cadena1));    #Esto arroja todo lo que se puede hacer con este objeto, si le pasamos numeros o listas también podemos ver todas las posibilidades que se pueden hacer con los mismos.

# print(cadena2.upper()); #Arroja todo en mayusculas

# print(cadena2.lower()); #Convierte a minúsculas

# print(cadena2.capitalize());    #Convierte todo a minúscula, y después convierte la primer letra a mayúscula

# print(cadena2.find("e"));   #Encuentra la posición en la que se encuentra la letra, muestra un valor de -1 en caso de no encontrar nada dentro de la cadena

# print(cadena2.index("e"));  #El index funciona como el find, sin embargo su única diferencia es que mientras que el find nos arroja un resultado de -1 al no encontrar nada, el index nos lanza una excepción (un error)

# print(cadena2.isnumeric()); #Devuelve False si no es un valor numérico y True si es un valor numérico

# print(cadena2.isalpha());   #Devuelve False si no es alfanumérico y True si es alfanumérico (los valores alfanuméricos son aquellos que solo tienen letras, no deben llevar espacios, comas, guines, etc.)

# print(cadena2.count("a"));  #Devuelve la cantidad de veces que se repite una letra

# print(len(cadena2));    #Cuenta la cantidad de caracteres (la longitud)

# print(cadena1.startswith("So")); #Devuelve True si se empieza con lo escrito y False si no se empieza con lo escrito

# print(cadena2.endswith(":D"));  #Devuelve True si termina con lo indicado y False si no termina con lo indicado

# print(cadena1.replace("la", "lu")); #Reemplaza la primer cadena con la segunda cadena, en caso de no encontrar coincidencias no se modifica

# print(cadena1.split(" "));  #Esto devuelve una lista, lo que pasa es que cada que se encuentre el caracter indicado dentro de una cadena, split se encargará de separarlo todo en forma de lista