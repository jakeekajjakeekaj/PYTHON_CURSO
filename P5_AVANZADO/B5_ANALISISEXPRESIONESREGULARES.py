import re;

text = "Este es un ejemplo de una página web: https://www.example.com, equis de"

pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}';     #Con el signo ? nosotros indicamos que nos encuentre 0 coincidencias o 1, si encuentra más no lo correrá, para este caso se está evaluando a lo que es la s, para indicar que puede ser http o https; a diferencia de + que dice que encuentre 1 coincidencia o muchas, o el * que dice que encuentre 0 coincidencias o muchas.

result = re.findall(pattern, text);

print(result);