import A_MODULO1;    #De esta manera se importa un módulo
#ASÍ COMO EN SQL, SI NOSOTROS ESCRIBIMOS import MODULO_1_1 as m_saludar; podemos renombrar al modulo con un nombre más legible
from A_MODULO1 import saludar, saludar2;  #De esta manera importamos únicamente alguna función del MODULO, por lo que ya no es necesario importar todo el MODULO

saludo = A_MODULO1.saludar("Jake");  #De esta manera se manda a llamar al módulo, pasa a funcionar como si fuera un objeto
print(saludo);  #Hola Jake

saludo2 = saludar("Ekaj");  #Así se manda a llamar la función importada del MODULO, como se puede observar ya no se tiene que escribir al MÓDULO como si fuera un método
print(saludo2);

saludo3 = saludar2("Jake2");
print(saludo3);