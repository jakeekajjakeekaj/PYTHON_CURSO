#BUCLE FOR

# for i in range (5): #De esta manera se va a iterar 5 veces
#     print("hola");

# for i in range (2, 5):  #De esta manera se va a iterar 3 veces
#     print("hola 2");

animales = ["gato", "perro", "loro"];
numeros = [10, 22, 36];

# for animal in animales: #De esta manera se imprime la lista en un ciclo for
#     print(animal);

# for animal, numero in zip(animales, numeros):   #De esta manera podemos recorrer 2 listas al mismo tiempo ** ES IMPORTANTE MENCIONAR QUE PAR QUE FUNCIONE CORRECTAMENTE, LA LINGITUD DEBE SER LA MISMA DE AMBAS LISTAS**
#     print(f"El animal representa al {animal}, mientras que el numero es {numero}");

# for animal in enumerate(animales):  #De esta manera se genera una tupla, en donde se guarda la posición y el valor; la otra manera es obtener la longitud desde el principio con len(animales)
    # print(f"El animal en la posición {animal[0]+1} es: {animal[1]}");

# for numero in numeros:
#     print(numero);
# else:
#     print(f"El bucle terminó {numero}");    #De esta manera se puede ver que usando un else para el bucle, este se ejecutará cuando el bucle finalice

# diccionario = {
#     "nombre" : "Jake",
#     "Apellido" : "Ekaj",
#     "Edad" : 23
# }

# for datos in diccionario.items():   #De esta manera nosotros podemos usar un diccionario dentro de un for, esto es debido a que si lo usamos de la manera común, solo nos mostrará las keys de nuestro diccionario, es decir "nombre", "apellido"; pero si utilizamos .items(), nos devuelve una tupla con la key y el contenido
#     print(f"La posición {datos[0]} es {datos[1]}");

frutas = ["mamey", "uva", "melon"];

# for fruta in frutas:
#     if fruta == 'mamey':
#         print(f"No quiero {fruta} no me gusta, no quiero >:c");
#         continue;   #De esta manera se usa el continue, esto quiere decir que si se lee esta sentencia, todo lo que se encuentra abajo no se lee y se pasa a la siguiente iteración, no funciona como el break ya que el break finaliza todo el bucle
#     print(f"Quiero {fruta}");

numeros2 = [2, 4, 6];
# numeros_duplicados = [x*2 for x in numeros2];   #De esta manera con una sola linea de código, nosotros asignamos que en una lista se guarde el valor de otra lista, y aparte manipular sus datos, en este caso por ejemplo estamos multiplicando *2 a los valores, osea el resultado final sería (4, 8, 12) *** REALMENTE ESTO ESTÁ LIMITADO A COSAS MÁS SENCILLAS, MAYORMENTE ES A COSAS COMO OPERACIONES ALGEBRAICAS ***
# print(numeros_duplicados);