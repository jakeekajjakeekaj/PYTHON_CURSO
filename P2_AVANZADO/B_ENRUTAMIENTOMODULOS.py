#Enrutamiento de módulos

#Suponiendo que tenemos nuestro archivo .py módulo en una carpeta llamada "funciones_buenas, la manera en que se accedería al archivo sería: "

# imoprt funciones_buenas.modulo    #De esta manera estamos indicando el enrutamiento conectando la carpeta y el archivo

# import sys  #Esta es una librería incluida con python

# print(sys.builtin_module_names);    #De esta manera se pueden ver todas las funciones que se pueden utilizar

# print(sys.path);    #De esta manera se pueden ver todas las rutas, la primer ruta es la nuestra y las demás son de los módulos instalados; si nosotros quisiéramos agregar un nuevo módulo, la manera de declararlo sería:
# sys.path.appen("C:\\Users\\yaric\\Documents\\PROGRAMACION\\CURSOS\\PYTHON\\P2_AVANZADO\\funciones_buenas")  #De esta manera se agregar un nuevo módulo y al momento de ver tosas las direcciones, esta ya aparecerá actualizada