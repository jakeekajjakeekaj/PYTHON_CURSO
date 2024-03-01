#VARAIBLES 2.0

#- Desempaquetado

# datos = ("Jake", "Ekaj");   #TAMBIÉN FUNCIONA CON LISTAS

# nombre, apellido = datos;

# print(nombre)   #Jake
# print(apellido) #Ekaj

#A esto se le llama desempaquetado, es decir en este caso declaramos una tupla, y "desempaquetamos" el contenido de la tupla en variables. ** ES IMPORTANTE MENCIONAR QUE PARA QUE EL DESEMPAQUETADO SEA CORRECTO, SE DEBE TENER LA MISMA CANTIDAD DE VARIABLES POR EL VALOR DE LA LISTA O TUPLA **

#- Tuple

# La de abajo es una manera de crear una tupla con tuple
# tupla = tuple(["dato1", "dato2"]);
# print(tupla);

# LA OTRA MANERA ES:

# tupla = "dato1", "dato2";
# print(tupla);

# Queriendo aplicar la forma de arriba pero son un solo dato y seguir sin poner parentesis así como arriba:

# tupla = "dato1",
# print(tupla);

#** LA VENTAJA DE USAR TUPLAS EN VEZ DE LISTAS, ES QUE LAS LISTAS ES COMO SI OCUPARAN 2 ESPACIOS DE MEMORIA, UNO TEMPORAL Y OTRO PERMANENTE, ES DECIR TIENE EL VALOR ORIGINAL, Y EN CUANTO RECIBE EL NUEVO VALOR, LO MANTIENE DE MANERA TEMPORAL Y LO PASA AL ORIGINAL PARA ASÍ MODIFICARLO; MIENTRAS QUE LA TUPLA A PARTE DE SER INMUTABLE, POR ESTA MISMA CARACTERÍSTICA NO ES NECESARIO RESERVAR UNA ESPACIO TEMPORAL. **

#- Conjunto con set

# conjunto = set(["dato1", "dato2"]);   #Con set es como si fura una tupla ya que es inmutable, sin embargo la gran diferencia es que los datos usados no tienen un orden, mientras que a los datos de la tupla los puedes llamar como tupla[0], con el set no funciona de esta manera.
# conjunto_tupla = set(["dato1", ("list1", "list2")]);    #Con esto se puede ver que dentro de la propia tupla, se accede a usar otras tuplas (datos inmutables), pero no se pueden usar LISTAS O DICCIONARIOS(datos mutables) por ejemplo

# print(conjunto);
# print(conjunto_tupla);

# conjunto1 = frozenset(["dato1", "dato2"]);  #De esta manera se indica que este set se quedará ahí, sin modificarse para así poder ser utilizado en otro set. 
# conjunto2 = {conjunto1, "dato3"};

# print(conjunto2);

#- Teoria de conjuntos

# El Superconjunto es aquél que contiene todos los datos, es decir lo que sería el conjunto1 del ejemplo de abajo sería el superconjunto ya que es el que cuenta con todos los datos; mientras que el subconjunto es aquél que contiene los datos extraídos del superconjunto, es decir el conjunto2 sería el subconjunto del conjunto1, porque se muestra que el conjunto2 contiene datos iguales a los del conjunto1

# conjunto1 = {1, 3, 5, 7};
# conjunto2 = {1, 3, 7};

# resultado = conjunto2.issubset(conjunto1);  #issubset sirve para determinar si algo es subconjunto, en este caso el conjunto2 es subconjunto de conjunto1? La respuesta es si

# resultado2 = conjunto2.issuperset(conjunto1);    #Es lo mismo de arriba, solo que ahora se vrifica si es superconjunto, por lo que la respuesta es False, ya que el conjunto2 no es el superconjunto

# resultado3 = conjunto2.isdisjoint(conjunto1);   #Es lo mismo de arriba, solo que ahora se verifica si tiene algún valor en común, en caso de tener algún valor en común idnicará False, ya que no es distinto; pero si NO tiene algún valor en común, marcará True ya que es distinto

# print(resultado);
# print(resultado2);