#FUNCIONES LAMBDA

multiplicar_por_dos = lambda x : x*2;   #Este es un ejemplo de la creación de una función lambda para multiplicar por 2, **ES IMPORTANTE MENCIONAR QUE ESTAS SON APTAS PARA CUANDO SON INSTRUCCIONES PEQUEÑAS**, si nosotros quisiéramos tener instucciones más complejas, las funciones lambda no son útiles

#Sin la función lambda, el código sería:
# def multiplicar_por_dos (x):
#     return x*2;

#-- OTRO EJEMPLO
#Abjo se verá la manera normal de trabajar sin funciones lambda
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9];

def es_par(num):
    if(num%2 == 0):
        return True;

numeros_pares = filter(es_par, numeros);    #Con filter lo que se hace es que se filtran los valores True, de numeros

print(list(numeros_pares)); #2, 4, 6, 8

#Abajo se muestra cómo se haría con una función lambda:
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)    #lambda indica que se realizará una función anónima, la función filter al final lo que hace es ejecutar cada valor de un iterable, por lo que aquí sirve más ya que no tiene sentido crear una función desde 0
print(list(numeros_pares));