#METODOS LISTAS

lista = list(["hola", "como", 22, True]);   #Se crea una lista con list
lista2 = list([5, 10, 2, 40]);

# print (len(lista)); #Devuelve la cantidad de elemetos que tiene la lista

# lista.append("valor agregado"); #Agrega un elemento a la lista
# print(lista);   #De hace dee sta manera ya que no permite agregar elementos para la impresión

# lista.remove("valor agregado");   #Quita el elemento de la lista
# print(lista);

# lista.insert(2, "Posicion 2");  #Insrta un nuevo elemento, pero en la posición indicada, haciendo que los elementos que estaban a partir de esa ubicación, realicen un recorrimiento
# print(lista);

# lista.extend([False, "jeje", 20]);  #Lo que hace es extender a nuestra lista con estos elementos, es decir a la lista qye ya se tenía, se le agregan estos elementos, es importante agregarlos de igual manera en forma de lista
# print(lista);

# lista.pop(0);   #Elimina al elemento de la lista ependiendo de su índice
# print(lista);
#-- TIP: Al momento de usas el pop, si queremos eliminar el último elemento, se indica el valor '-1' y si queremos eliminar el penúltimo valor indicamos el númro '-2' y así

# lista.clear();  #Elimina los valores de la lista
# print(lista);

# lista2.sort();  #Orden los elementos de forma ascendente ** SI TIENE STRINGS NO ES POSIBLE ORDENAR **
# print(lista2);

# lista2.reverse();   #Esto lo que hace es invertir el orden de la lista, para este caso por ejemplo si primero ordenamos la lista con sort, el recorrido será de menor a mayor, pero si después se usa el reverse el orden se invierte, haciendo que en vez de que sea en forma ascendente, ahora será en orden desdcendente
# print(lista2);

# print(dir(('sdsedñl,d', 5)));   #Como tip, al usar dir recordemos que podemos ver las fucniones que podemos aplicar sobre lo que estemos utilizando el dir, para este caso nosotros estamos declarando una tupla, por lo que las funciones que nos permite colocar es 'count' e 'index'

# -- TIP: Recordemos que el index busca un elemento, pero que pertenezca idéntido a la lista, es decir que si nosotros buscamos un 56 y escribimos 5, nos marcará un valor FALSE, a furzas tenemos que colocar el numero 56.