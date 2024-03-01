#Cuenta la cantidad de palabras en una oracion
frase = input("Indica una oración y te digo la cantidad de palabras que contiene: ");
palabras_separadas = frase.split(" ");
cantidad_de_palabras = len(palabras_separadas);
print(f"La cantidad de palabras que contiene la oración es de: {cantidad_de_palabras}");