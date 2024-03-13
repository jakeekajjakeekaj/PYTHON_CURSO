import re;

email = "example@example.com";

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'; #Aquí se indica [a-zA-Z0-9._%+-] pueden ser válidos todos los caracteres que vayan de la a hasta la z, de la A hasta la Z, del 0 hasta el 9, . todo lo que no sea un salto de linea, _ los guines bajos también están permitidos, % es como un comodín que toma en cuenta a todo lo que está antes y después, + mientras que el * buscaba 0 o más coincidencias, el + busca 1 o más coincidencias, - permite guines;
# + indica que se encuentre al menos una coincidencia con el patrón anterior, @ indica que debe ir
# [a-zA-Z0-9.-] indica que se permite toda letra de a hasta z, de A hasta Z, de 0 hasta 9, no se permiten saltos de linea y a su vez puede llevar un guión
# + indica que debe contener todo el patrón anterior, \. se busca específicamente al punto
#[a-zA-Z]{2,} Indica que se puede tener toda letra de a hasta z, de A hasta Z y que los caracteres deben reptirse en un mínimo de 2, ya que no existen dominios que sean de 1 

result = re.match(pattern, email);

if result:
    print("Dirección de correo válida");
else:
    print("Dirección de correo inválida");