import re;

text = "The quick brown fox jumps over the lazy dog";

x = re.search("^The.*dog$", text);  #Lo que se indica aquí es ^Búscame una cadena en donde 'The' aparezca al principio, . encuentra cualquier cosa que no sea un salto de línea, *afecta al caracter anterior, el asterisco indica que encuentra 0 o más ocurrencias, es decir que a pesar de no encontrar ningún salto de línea, lo deja continuar y no para, o si encuentra muchisimos saltos en linea, también los deja pasar (IMPORTANTE MENCIONAR QUE FUNCIONA CON CUALQUIER COSA), dog busca que se cumpla la palabra 'dog', $ indica que dog tiene que encontrarse al final de la linea

if x:
    print("Si");
else:
    print("No");