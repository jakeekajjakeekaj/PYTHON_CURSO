#DICCIONARIOS 2.0

#- dict()
# diccionario = dict(nombre = "Jake", apellido = "Ekaj"); #De esta manera declaramos un diccionario con dict, una ventaja de hacerlo así, es que podemos declarar diccionarios vacíos

# print(diccionario);

#- fromkeys()
# diccionario = dict.fromkeys(["nombre", "apellido"]);    #De esta manera se crean diccionarios con todos los valores none
diccionario2 = dict.fromkeys("nombre", "apellido"); #De esta manera se crea un diccionario en donde el primer valor es un iterable y el segundo valor es el valor que se repetirá por cada key, es decir el resultado para este ejemplo sería: n : apellido, o : apellido, m : apellido y así sucesivamente hasta formar la clave n, o, m, b, r, e

# print(diccionario);