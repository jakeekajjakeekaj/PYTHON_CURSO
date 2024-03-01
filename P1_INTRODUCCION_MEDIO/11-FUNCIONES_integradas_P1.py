#FUNCIONES INTEGRADAS (FUNCTIONS BUILD IN)

numeros = [4, 2, 7, 10, 9];

# print(max(numeros));    #Esta función encuentra el valor más alto

# print(min(numeros));    #Esta función encuentra el valor más pequeño

num = round(12.23452, 3);   #Esto lo que hace es mostrar los decimales de algún número en forma redondeada, antes lo que se hacía era multiplicar por algún valor como 100 y después dividir el número, pero esta función lo hace todo de mejor manera; 
# print(num); #12.235 COMO SE MUESTRA, EN VEZ DE APARECER UN 4, APARECE UN 5 YA QUE EL 4 FUE REDONDEADO TOMANDO EN CUENTA QUE EL SIGUINETE VALOR ERA 5

# print(bool("hola"));  #True  
# print(bool());  #False
# print(bool(""));    #False
# print(bool(False)); #False
# print(bool(True));  #True
# print(bool(0)); #False
# print(bool(None)); #False

#COMO SE PUEDE VER ARRIBA, LA FUNCIÓN BOOL DA COMO RESULTADO True a cualquier valor diferente de 0 o null; mientras que da resultado False a todos los valores null o 0

# print(all([1, True, "Hola"]));  #True
# print(all([0, True, "Hola"]));  #False
# print(all([1, "", True]));  #False

#LO DE ARRIBA FUNCIONA COMO LA FUNCIÓN bool; SIN EMBARGO EN VEZ DE AGARRAR UN SOLO ELEMENTO, AGARRA TODOS LOS ELEMENTOS DE LA LISTA

# print(sum(numeros));    #32 ESTO DEVUELVE LA SUMA TOTAL DE TODOS LOS VALORES