#METODOS DICCIONARIOS

diccionario = {
    'nombre' : "Jake",
    'apellido' : "Ekaj",
    'edad' : 24
}

# print(diccionario.keys());  #Esto devuelve las claves de nuestro diccionario en forma de lista (es decir (['nombre', 'apellido', 'edad']));

# print(diccionario.get('laksmd'));   #Esto devuelve el valor de la clave, es decir para este caso requerimos el valor de la clave 'nombre' el cual es "Jake", en caso de no encontrar la key, el valor será none

# diccionario.clear();    #De esta manera se elimina al contenido del diccionario
# print(diccionario);

# diccionario.pop('nombre', 'edad');  #De esta manera eliminamos la key o keys junto con su contenido del diccionario
# print(diccionario);

print(diccionario); #Aquí se muestra un ejemplo de la impresión del diccionario normal mientras que abajo...
print(diccionario.items()); #Abajo se muestra el contenido del diccionario para así poder ser iterable