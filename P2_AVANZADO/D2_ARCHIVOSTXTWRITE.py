with open('P2_AVANZADO\\D_texto.txt', 'w', encoding="UTF-8") as archivo:    #Aquí se indica la 'w' de write
    archivo.write("equis de\n");  #De esta manera escribe en el archivo, pero no solo escribe, si no que lo reescribe, es decir al no leer la información del txt, lo que hace es eliminar todo el contenido para posteriormente escribir sobre el mismo

    # archivo.writelines("Esto fue anexado"); #De esta manera se escribe, pero así funciona igual que usando el .write, para que este módulo se aproveche de verdad, lo que se debe hacer es:

    archivo.writelines(["Esto ha sido anexado 1 \n", " y esto ha sido anexado 2\n"]);    #De esta manera escribimos múltiple contenido dentro del .txt, pudiendo escribir saltos de linea o dejando todo en un renglón


with open('P2_AVANZADO\\D_texto.txt', 'a', encoding="UTF-8") as archivo:    #Aquí se indica la 'a' de append para así ir anexando más contenido al .txt
    archivo.write("después del append\n");
    archivo.writelines("Usando write lines despues del append");

#COMO SE PUEDE VER, SI ANEXAMOS TODO, SE PUEDE OBSERVAR QUE TODO EL CONTENIDO SE ANEXA, ES DECIR NOSOTROS ESCRIBIMOS EL .WRITE, Y SE ANEXA, POSTERIOR A ESTO ESCRIBIMOS WITELINES Y TAMBIÉN SE AGREGA EL CONTENIDO, posterior escribimos el 'a' de append y todo el contenido de igual manera se sigue anexando