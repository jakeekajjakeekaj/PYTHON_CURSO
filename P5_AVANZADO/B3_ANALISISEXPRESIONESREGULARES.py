import re;

text = "reemplazando todas las variables por el asterisco";

new_text = re.sub("[aeiou]", "*", text);    #De esta manera nosotros indicamos con re.sub que se reemplazará un patrón por otras variables, para este caso indicamos [aeiou] en donde gracias a los corchetes, en vez de indicar que busque en esta secuencia, le indicamos que busque cualquier valor que esté dentro de los corchetes, es decir que busque si está presente la a, e, i, o, u; y que a su vez se reemplacen por lo que se indica que se va a sustituir, es decir '*', y esta búsqueda la realizará dentro de lo que es el text

print(new_text);    #Imprimirá todo, pero censurará con * a las letras a, e, i, o, u