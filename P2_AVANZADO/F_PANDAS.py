#COMO DATO INTERESANTE, LA MAYORÍA DE USUARIOS USAN pandas as pd, es como algo que se ha ido regularizando para que todo mundo pueda entenderlo bien; A SU VEZ PANDAS NO ES UNA LIBRRÍA INCLUIDA CON PYTHON, POR LO QUE SE DEBE INSTALAR POR APARTE
#SE DEBE ABRIR EL CDM, POSTERIOR SE ESCRIBE pip, SI NO PASA ALGO ESCRIBIR py pip, SI NO PASA ALGO ESCRIBIR py -m pip
#SI CON ESTO NO APARECE NADA, SIGNIFICA QUE TENEMOS QUE INSTALAR pip, PARA ESTO NOS VAMOS A INTERNET PARA INSATALARLO Y VER EN LA DOCUMENTACIÓN LOS COMANDOS PARA INSTALARLO.
#PARA VERIFICAR SI SE INSTALÓ CORRECTAMENTE, SE ESCRIBEN LOS COMANDOS DICHOS ARRIBA.
#PARA INSTALAR pandas, SE DEBE ESCRIBIR py -m pip install pandas

import pandas as pd;

# print(type(pd));    #De esta manera verificamos que todo se haya instalado correctamente, aquí nos debería de salir como resultado que es un módulo

# df = pd.read_csv("P2_AVANZADO\\E_CSV.csv");    #De esta manera asignamos a una variable la información .csv recabada a través de pandas
#DE IGUAL MANERA EL NOMBRE ELEGIDO FUE df, esto por DATA FRAME, NOSOTROS PODEMOS ASIGNAR EL NOMBRE QUE QUERAMOS, PERO ES BUENO MANEJARLO COMO UN DATA FRAME YA QUE SON ESTRUCTURAS DE DATOS BIDIMENSIONALES SIMILARES A UNA HOJA DE CÁLCULO
# print(df); #De esta manera ya solo se imprime y verifica que toda la información se haya recabado de forma correcta

#EJEMPLO DE LO MENCIONADO RESPECTO AL DATA FRAME:
# print(df["nombre"]);    #De esta manera obtenemos la columna 'nombre' gracias al uso de DF

# df = pd.read_csv("P2_AVANZADO\\E_CSV.csv", names=["name", "lastname", "age"]);  #De esta manera se agregarían encabezados para trabajar con los datos, para este caso no se hará de esta manera ya que se agregaron encabezados directamente en el .csv, pero para que se sepa la manera en que se agregarían dichos encabezados

# print(df);