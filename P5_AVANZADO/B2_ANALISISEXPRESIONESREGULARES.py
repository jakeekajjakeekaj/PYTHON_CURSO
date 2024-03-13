import re;

text = "La fecha es 23/06/2021 y el teléfono es +1-555-555-5555";

pattern = r'\d{2}/\d{2}/\d{4}'; #De esta manera nosotros indicamos que \d búsqueda de números, {2} que se repitan 2 veces, / búsqueda de decho caracter, y se repite a excepción del final en donde se buscan 4 caracteres; que como se muestra en el texto, esto encaja perfectamente con la fecha de 23/06/2021

replacement = "Fecha Oculta";

new_text = re.sub(pattern, replacement, text);  #re.sub encuentra la cadena y realiza un reemplazo, es decir que primero obtiene el patrón, después obtiene la variable con la que se reemplazará dicho patrón de ser encontrado, y para finalizar se indica el texto que se analizará

print("Texto modificado: ", new_text);  #Se imprime todo el texto, pero ocultando a la fecha con el mensaje de 'Fecha Oculta'