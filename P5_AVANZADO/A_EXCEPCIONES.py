# Para entender lo que son las excepciones, primero se debe entender lo que es un evento; un evento es cualquier cosa que suceda dentro de nuestro programa, ed decir hacer click, soltar el click, mover el mouse sobre alguna zona, etc.
# Las excepciones TAMBIÉN SON EVENTOS, pero este evento lo que hace es interrumpir el flujo normal de ejecución, es decir que hace que se detenga el programa en el paso 5 de 10, si es que se encuentra una excepción aquí; el objetivo de las excepciones es saber manejarlas, para que a pesar de encontrar un error, el programa no finalice.
# CABE MENCIONAR QUE NO ESTÁ MUY BIEN VISTO EN PROGRAMACIÓN EL MANEJO DE EXCEPCIONES, PERO A VECES LLEGA A SER BASTANTE ÚTIL

# def sumar_docs():
#     a = input("Numero 1: ");
#     b = input("Numero 2: ");
#     resultado = int(a) + int(b);    #Si nosotros colocamos un caracter y un número por ejemplo, esto nos generaría un error, osea nos arrojaría una excepción; por lo que la manera de resolver esto sería en la forma de abajo
#     return resultado;

# print(sumar_docs());

# -- INICIO DEL USO DE EXCEPCIONES --

# def sumar_docs():
#     while True: # Para empezar se crea un bucle, para que en caso de que haya algún fallo, el usuario pueda volver a meter los valores, pero esta vez de forma correcta
#         a = input("Numero 1: ");
#         b = input("Numero 2: ");
#         try:    #Para este caso ya se empieza a trabajar con las excepciones, lo que se indica es que se va a intentar lo que se encuentra dentro del mismo
#             resultado = int(a) + int(b);    #Esta es la función que se va a intentar, pero en caso de que salte una excepción se brincará al except; si no brinca ninguna excepción se finalizará el bucle gracias al break ubicado en el else
#         except: #Este es el except, el cuál dentro del mismo indica el funcionamiento dle programa en caso de brincar alguna excepción
#             print("Se detectó un error, pero el programa continuará");  #Se indica un mensaje y gracias al ciclo declarado en un principio, esto se repetirá hasta que el usuario escriba de forma correcta a los valores; así mismo es gracias al try - except; o mejor dicho saber manejar a las excepciones que en ingún momento el programa finaliza
#         else:   #Este else se ejecuta si durante el try no hubo ninguna excepción, en caso de existir una excepción, se brinca al except y se repite el ciclo
#             break;
#         finally:    #El finally provoca que lo que esté dentro siempre será ejecutado, es decir que aún si la excepción se ejecuta o no se ejecuta, lo que está dentro del finally SIEMPRE SE EJCUTARÁ; cabe mencionar que esto es rara vez usado
#             print("Esto se ejecuta sieeeeempre");
#     return resultado;

# print(sumar_docs());

#-- De igual manera se puede acceder a la excepción y hasta renombrarla:

# def sumar_docs():
#     while True:
#         a = input("Numero 1: ");
#         b = input("Numero 2: ");
#         try:
#             resultado = int(a) + int(b);
#         except Exception as e:  #De esta manera renombramos a nuestra excpeción, lo que se hace es acceder a la clase Exception y la renombramos como e
#             print("Indica solo números");
#             print(f"ERROR: {e}");   #De esta manera le hacemos un catch al error e indicamos cuál ha sido el error
#         else:
#             break;
#     return resultado;

# print(sumar_docs());

# -- ARRIBA SE VIÓ COMO RENOMBRA A NUESTRA EXCEPCIÓN, SIN EMBARGO NOSOTROS PODEMOS CREAR UNA EXCEPCIÓN POR CADA COSA, ES DECIR:

def sumar_docs():
    while True:
        a = input("Numero 1: ");
        b = input("Numero 2: ");
        try:
            resultado = int(a) + int(b);
        # except Exception as e:
        #     print("Excepción lanzada");
        #     print(type(e).__name__);    #De esta manera podemos visualizar cuál es el nombre del error, para este caso si sumamos 1 + b por ejemplo, el nombre del error es value error, por lo tanto ahora nosotros podemos crear excepciones para este tipo de situaciones, por ejemplo
        except ValueError as e: #De esta manera, gracias que nosotros pudimos ver el error que tiraba, en vez de generar una excepción, podemos generar múltiples excepciones para cada caso diferente
            print(f"La excepción es un value error, favor de indicar números {e}");
        except ZeroDivisionError as e:  #Este es otro ejemplo de que s epueden manejar múltiples excepciones, para este caso, si el programa se centrara en realizar divisiones, si un usuario intenta dividir un 0 entre algún número, saltaría esta excepción y nosotros podemos abordarla de manera personalizada de esta forma
            print(f"No se puede dividir un 0 entre algún número {e}");
        else:
            break;
    return resultado;

print(sumar_docs());
