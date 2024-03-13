#Cuando se trabaja con expresions regulares, básicamente es trabajar con los símbolos que a su vez provocan diferentes tipos de acciones

import re;

texto = '''Hola maestro, esta es la cadena 111. cómo estás mi capitán?
Estaaa tata es la segunda 2 linea de texto.
Y esta es la final definitiva mi capitán.
''';

# resultado = re.search("Hola", texto);   #re.search busca lo indicado en el primer parámetro, y en el segundo parámetro de dóndo lo va a buscar; el resultado indica desde que punto y hasta qué punto lo encontro, así mismo lo regresa en forma de objeto

# print(resultado);

# resultado = re.findall("Esta", texto, flags = re.IGNORECASE);   #findall te encuentra todas las coincidencias. De igual manera hay otro parámetro que se puede estar agregando que son como definir ciertas reglas, en este caso se llaman flags, y para este caso el re.IGNORECASE indica que se realizará la búsqueda sin importar que sean mayúsculas, es por eso que ahorita aunque la búsqueda está escrita con la primer letra minúscula, a la búsqueda no le importará si hay letras minúsculas o mayúsculas

# print(resultado);

# -- COMENZANDO CON EXPRESIONES REGULARES --

#   \d -> Busca dígitos numéricos del 0 al 9
resultado = re.findall(r"\d", texto);   #Con la r, en vez de hacerle como con la f, mientras que la f indica que se concatenará el resultado y podremos mandar a llamar a nuestras variables, con la r nosotros indicamos el uso de expresiones regulares; así mismo con \d como se indicó arriba, nos busca números del 0 al 9

# print(resultado);   #1, esto debido a que dentro del texto se encuentra un '1'

# ** Algo curioso, es que en Python las letras de las expresiones regulares tienden a buscar lo contrario, como en le ejemplo de abajo:
#   \D -> Busca todo, a excepción de los números del 0 al 9
resultado = re.findall(r"\D", texto);   #De esta manera extraemos todo, a excepción de los números del 0 al 9
# print(resultado);

#   \w -> Busca caracteres alfanuméricos [a-z A-Z 0-9 _]así es, también el guión bajo, en otros lenguajes el guón bajo no es considerado caracter alfanumérico, pero en Python si
resultado = re.findall(r"\w", texto);   #De esta manera se encuentran todos los alfanuméricos, es decir que se excluyen las comas, puntos, espacios en blanco, interrogación, etc
# print(resultado);

#   \W -> Busca caracteres no alfanuméricos
resultado = re.findall(r"\W", texto);   #De esta manera se obtiene todo lo no alfanumérico, es decir espacios en blanco, interrogación, puntos, comas, saltos de linea, etc.
# print(resultado);

#   \s -> Busca todo lo que sea espacios, tabs, saltos de linea
resultado = re.findall(r"\s", texto);   #Obtiene espacios, tabs, saltos de linea
# print(resultado);

#   \S -> Busca todo lo que no sea espacios, tabs, saltos de linea
resultado = re.findall(r"\S", texto);   #Obtiene todo lo que no sea espacios, tabs, saltos de linea
# print(resultado);

#   . -> Busca todo menos saltos de linea
resultado = re.findall(".", texto); #De esta manera se obtiene todo menos los saltos de línea
# print(resultado);

#   \n -> Esto busca saltos de linea
resultado = re.findall("\n", texto);    #De esta manera se obtiene todo lo que sea saltos de linea
# print(resultado);

#   \ -> Cancela todos los caracteres especiales, es decir los que no son alfanuméricos, para esto se tiene que colocar la división inversa y colocar el caracter a cancelar, de esta manera se cancela la función anterior para colocar encima la nueva
resultado = re.findall(r"\.", texto); #De esta manera indicamos que se cancelarán todos los puntos
# print(resultado);
resultado = re.findall(r"\?", texto);   #De esta manera indicamos que se cancelarán todos los signos de interrogación
# print(resultado);
#y así con los demás símbolos

# AHORA SE EMPEZARÁ CON UN EJEMPLO UN POCO MÁS COMLEJO, se armará una cadena que busque un número, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", texto);  #Recordemos que usando esto se tiene \d que buscar números, \. que busca caracteres especiales, para este caso indicando puntos, \s busca todos los espacios
# print(resultado);   #De esta manera nosotros buscamos en donde se respete dicha secuencia, es decir que tenga un número, seguido de un punto y seguido de un espacio en blanco, que para el caso del ejemplo, sería una coincidencia con el '1. '

#   ^ -> Busca el comienzo de una linea
resultado = re.findall(r'^', texto);    #De esta manera se encuentra el principio de la linea
# print(resultado);

# - TOMANDO EN CUENTA EL EJEMPLO ANTERIOR, PUEDE PARECER QUE BUSCAR LOS COMIENZOS DE UNA LINEA ES INÚTIL, PERO PARA QUE SEA FUNCIONAL DEBEMOS COMBINARLO CON OTRAS SECUENCIAS, POR EJEMPLO:

resultado = re.findall(r'^Hol', texto);   #De esta manera solo muestra lo que se encuentra al principio de la linea, es decir si nosotros escribimos 'ola', no aparecerá el texto, debido a que no se encuentra al principio de la linea, pero si nosotros escribimos 'H' o 'Hol' esto si aparecerá ya que si se encuentra al principio de la linea
# print(resultado);

# - AHORA BIEN SI NOSOTROS ESCRIBIMOS Esta, no aparecerá, esto es debido a que si lo dejamos sin flags, solo tomará en cuenta a la primer linea, para tomar en cuenta todas las demás lineas como inicios de linea, se debe colocar:

resultado = re.findall(r'^Est', texto, flags = re.M);   #La flag re.M indica que se activa la multilinea, es decir que tras cada salto de linea, la linea será una nueva linea por lo que se podrá tomar el principio de cada linea
# print(resultado);

#   $ -> Busca al final de cada linea
resultado = re.findall(r'capitán.$', texto, flags = re.M);  #Funciona igual que con ^ solo que ahora se coloca el signo de $ al final, como ejemplo al colocar el ., toma en cuenta también al símbolo de interrogación
# print(resultado);

# -- GRUPOS --

#   {n} -> Busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}', texto);    #Esto indica que encuentre n cantidad de veces lo que se le indique, en este caso con el \d le estamos indicando que busque números, y si encuentra el númro repetido 3 veces dentro de texto se ejecuta
# print(resultado);

# -- RANGOS --

#   {n, m} -> Desde mínimo n, hasta máximo m
resultado = re.findall(r'\d{1,4}', texto);  #De esta manera nosotros estamos indicando un límite, estamos indicando que los números se repitan al menos una vez, y que lleguen a un máximo de 4 veces
# print(resultado);

#   TAMBIÉN SE PUEDEN BUSCAR CARACTERES ESPECÍFICOS:
resultado = re.findall(r'ta{2,3}', texto);  #De esta manera nosotros estamos indicando que se tenga una t seguido de una a, y que la a se repita minimo 2 veces y máximo 3
# print(resultado);   #'taaa'

#   SI QUEREMOS QUE TAMBIÉN ENCIERRE A LA t, es decir para buscar algo que diga 'tatata' por ejemplo, sería:
resultado = re.findall(r'(ta){2}', texto);  #Aquí se indica que gracias a los paréntesis, cada que se encuentre el ta, repetido 2 veces, nos devolderá como respuesta un ta
# print(resultado);

resultado = re.findall(r'[ta]{2}', texto);  #Aquí lo que se indica gracias a los corchetes, que nos devolverá todos los ta que se encuentren en un mínimo de 2 y máximo de 3
print(resultado);

#   | -> Busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola', texto); #De esta manera le indicamos que nos devuelva todo lo que ha ido encontrando, es decir nos devolcerá los números que se repitan minimo 2 y maximo 4; y nos devolverá Hola
# print(resultado);   #'Hola', '111'

x = re.search("^The.*dog$", text);  #Lo que se indica aquí es ^Búscame una cadena en donde 'The' aparezca al principio, . encuentra cualquier cosa que no sea un salto de línea, *afecta al caracter anterior, el asterisco indica que encuentra 0 o más ocurrencias, es decir que a pesar de no encontrar ningún salto de línea, lo deja continuar y no para, o si encuentra muchisimos saltos en linea, también los deja pasar (IMPORTANTE MENCIONAR QUE FUNCIONA CON CUALQUIER COSA), dog busca que se cumpla la palabra 'dog', $ indica que dog tiene que encontrarse al final de la linea

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'; #Aquí se indica [a-zA-Z0-9._%+-] pueden ser válidos todos los caracteres que vayan de la a hasta la z, de la A hasta la Z, del 0 hasta el 9, . todo lo que no sea un salto de linea, _ los guines bajos también están permitidos, % es como un comodín que toma en cuenta a todo lo que está antes y después, + mientras que el * buscaba 0 o más coincidencias, el + busca 1 o más coincidencias, - permite guines;
# + indica que se encuentre al menos una coincidencia con el patrón anterior, @ indica que debe ir
# [a-zA-Z0-9.-] indica que se permite toda letra de a hasta z, de A hasta Z, de 0 hasta 9, no se permiten saltos de linea y a su vez puede llevar un guión
# + indica que debe contener todo el patrón anterior, \. se busca específicamente al punto
#[a-zA-Z]{2,} Indica que se puede tener toda letra de a hasta z, de A hasta Z y que los caracteres deben reptirse en un mínimo de 2, ya que no existen dominios que sean de 1 

pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}';     #Con el signo ? nosotros indicamos que nos encuentre 0 coincidencias o 1, si encuentra más no lo correrá, para este caso se está evaluando a lo que es la s, para indicar que puede ser http o https; a diferencia de + que dice que encuentre 1 coincidencia o muchas, o el * que dice que encuentre 0 coincidencias o muchas.