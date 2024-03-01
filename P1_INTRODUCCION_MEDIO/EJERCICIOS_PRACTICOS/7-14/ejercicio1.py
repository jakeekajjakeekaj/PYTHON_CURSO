#Faltó el profe y los estudiantes darán la clase

#Conseguir el nombre y edad de los compañeros, a su vez determinar al profesor por el alumno más viejo y al asitente por el alumno más joven
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input(f"Ingrese el nombre {i+1}: ");
        edad = int(input(f"Ingrese la edad {i+1}: "));
        compañero = (nombre, edad);
        compañeros.append(compañero);
    compañeros.sort(key = lambda x:x[1]);   #Esto ordenará a los compañeros por key, en este caso estamos asignando a la edad
    asistente = compañeros[0][0];   #Aquí indicamos que en la tupla 0, campo 0, ya que recordemos que ahorita nuestra lista compañeros se ve en la forma [(nombre, edad), (nombre2, edad2)], entonces al final ya estamos trabajando con arreglos bidimensionales
    profesor = compañeros[-1][0];   #Esto es así para agarrar a la última tupla, en su valor 0 (nombre)
    return asistente, profesor; #De esta manera ya retornamos al asistente (primera tupla) y al profesor (última tupla)

asistente, profesor = obtener_compañeros(4);

print(f"El profesor es: {profesor} y su asistente es: {asistente}");