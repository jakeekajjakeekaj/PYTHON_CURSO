#ARCHIVOS TXT

archivo = open("P2_AVANZADO\\D_texto.txt", encoding="UTF-8"); #De esta manera estamos abriendo eñ archivo .txt y a u vez asignamos el valor a una variable llamada "archivo"; a su vez asignamos el encoding en UTF-8, esto para que la codificación sea universal, es lo mismo que cuando en HTML escribimos charset = "UTF-8"

# print(archivo.read());  #De esta manera podemos leer el contenido de nuestra variable

# linea1 = archivo.readline();    #Para este caso se asigna la linea 1 del texto a nuestra variable linea1
# print(linea1);  #Se imprime la linea 1 del texto

# linea_longitud = archivo.readline(10);  #Lee la longitud del .txt que nosotros indicamos en el paréntesis
# print(linea_longitud);  #Se imprime el texto

# lineas = archivo.readlines();
# print(lineas)

#Una vez que el archivo se acaba de leer *** ES IMPORTANTE CERRARLO, ESTO ES PORQUE UNA VEZ QUE EL ARCHIVO SE LEE, NO SE PUEDE VOLVER A LEER POR ASPECTOS DE SEGURIDAD, ENTONCES SI NOSOTROS UTILIZAMOS ALGÚN readline(), ya no podremos volver a utilizarlo o algún otro hasta que se cierre el archivo ***

# archivo.close();  #De esta manera se cierra el archivo

#*** DE IGUAL MANERA ES IMPORTANTE MENCIONAR QUE NOSOTROS PODREMOS SEGUIR TRABAJANDO CON LAS VARIABLES ASIGNADAS, SIN EMBARGO SI QUEREMOS TRABAJAR CON NUEVAS VARIABLES APLICANDO NUEVAS FUNCIONES, TENEMOS QUE VOLVER A DECLARAR EL open para volver a abrir el archivo ***

# *** DE IGUAL MANERA ES IMPORTANTE MENCIONAR QUE CERRAR EL ARCHIVO ES DE VITAL IMPORTANCIA PARA ASÍ EVITAR LA PÉRDIDA DE DATOS DE NUESTROS TEXTOS ***