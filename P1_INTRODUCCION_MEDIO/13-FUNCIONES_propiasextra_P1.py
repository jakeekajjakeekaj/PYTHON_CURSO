def frase(nombre, apellido, adjetivo, expresion = "wuuuuuu"):   #Aquí se muestra un valor por defecto así como las variables que se estarán recibiendo
    return f'Hola {nombre} {apellido}, eres {adjetivo} {expresion}';

frase_resultante = frase("Jake", "Ekaj", "wapo");   #De esta manera pasamos los parámetros, pero los pasamos siguiendo un orden para que automáticamente si asignen los valores junto con las variables puestas en la función; SIN EMBARGO SI LO HACEMOS CON UN ORDEN DIFERENTE, los valores no se asignarían como deberían, es por esto que se hace lo que se muetsra abajo:
frase_resultante2 = frase(adjetivo = "Wapetón", apellido = "Ekaj", nombre = "Jake");    #De esta manera podemos ver que aunque los valores están desordenados, podemos de igual manera asignar cada valor a la variable correspondiente de la función; por ejemplo literalmente los valores se encuentran en un orden inverso, pero la impresión sigue siendo igual a la de arriba ya que desde ahorita estamos indicando hacia dónde se dirigirán los datos

print(frase_resultante);
print(frase_resultante2);