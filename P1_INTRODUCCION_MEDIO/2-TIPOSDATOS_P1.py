#Datos Compuestos

#breve recordatorio
#-- LISTA
# lista = ["Hola", "Hola 2", True, 1.85];
# print(lista);   #Imprime todo
# print(lista[2]);    #true

#-- TUPLAS
# Es muy parecido a una lista, sin embargo una tupla a diferencia de la tupla, NO SE PUEDE MODIFICAR Y LLEVAN PARENTESIS.
# tupla1 = ("no modifica", False, 3.7);

#mini-ejercicio INVERTIR LISTA
# i = 0;
# length = len(lista);

# while i < length // 2:  #El simbolo // indica una división, pero se redondea al floor
#     lista[i], lista[length - 1 - i] = lista[length - 1 - i], lista[i];
#     i+=1;

# print(lista)

# -- CONJUNTO (SET)
# Funciona como las tuplas, ya que no se pueden modificar, sin embargo a diferencia de con las tuplas, para este caso no puedes acceder por índices ya que son datos desordenados, es decir si escribimos ejemplo[2], de esta manera no se puede acceder, solo puedes acceder a ella nombrando al conjunto y te imprimirá todos los valores; así mismo no permite que hayan elementos duplicados.
conjunto1 = {"Jake Ekaj", True, 1.85};

#-- DICCIONARIO}
# Es como un objeto pero sin contener cosas como funciones (métodos)
# diccionario1 = {
#     'nombre' : "Jake",
#     'apellido' : "Ekaj",
#     'wapo' : True,
#     'Edad' : 24
# }

# DATO INTERESANTE, SI NOSOTROS UTILIZAMOS EL OPERADOR /, EL RESULTADO SERPIA UN TIPO FLOAT, AUN SI LA DIVISIÓN FUERA: 6 / 3, EL RESULTADO DE 2 NO ES ENTERO, SERÍA UN DATO FLOAT.