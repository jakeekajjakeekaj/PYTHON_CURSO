# Esta es la manera óptima de trabajar con archivos, ya que aparte de ser menos código, es más eficiente, da menos margen de errores, etc.

#WITH OPEN

with open("P2_AVANZADO\\D_texto.txt", encoding="UTF-8") as texto:  #De esta manera se abre el archivo y también se va a cerrar en cuanto se acabe de ejecutar; IMPORTANTE MENCIONAR QUE EL as ES OPCIONAL
    # print("hola");  #Esto se ejecuta si el archivo .txt se abre
    print(texto.read());