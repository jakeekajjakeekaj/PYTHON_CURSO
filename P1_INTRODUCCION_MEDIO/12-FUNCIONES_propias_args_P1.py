def saludar():
    print("Hola Mundo");

def saludar_nombre(nombre):
    print(f"Hola {nombre}, ¿Cómo estás?");

saludar();  #Ejecutar función
saludar_nombre('Jake'); #Ejecutar función con parámetro

def retornar(num):
    num += 20;
    return num; #De esta manra se indica que un valor se va a retornar

numero = retornar(20);  #Se asigna el valor retornado
print(numero);  #Se imprime el valor retornado

# def suma(lista):    #Esta es una manera óptima de pasar parámetros en la función, esto es porque al pasar los valores por ejemplo para una lista, si nos limitamos a indicar num1, num2; si queremos agregar más datos se tendrá un problema, debido a lo limitante que puede ser el indicar los parámetros con los que se trabajará, en cambio si desde un principio pasamos una lista, ya no nos tenemos que preocupar por la cantidad de datos.
#     numeros_sumados = 0;
#     for numero in lista:
#         numeros_sumados += numero;
#     return numeros_sumados;

# resultado = suma([1, 2, 3]);
# print(resultado);

# **SIN EMBARGO LA MANERA DE ARRIBA NO ES LA MANERA MÁS ÓPTIMA DE HACERLO, LA MANERA MÁS ÓPTIMA DE HACERLO ES CON EL PARÁMETRO ARGS**

def suma(*numeros): #De esta manera nosotros estamos indicando que se pasarán varios valores en una variable
    return sum(numeros);

resultado = suma(1, 2, 3);
print(resultado);