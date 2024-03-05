#TRABAJANDO CON ARCHIVOS minip

#2 listas, 1 con nombres y otra con apellidos

nombres = ["Jake1", "Jake2", "Jake3", "Jake4", "Jake5"];
apellidos = ["Ekaj1", "Ekaj2", "Ekaj3", "Ekaj4", "Ekaj5"];

with open ("P2_AVANZADO\\EJERCICIOS_PRACTICOS\\A_F_mini_nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son:\n\n");
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------\n") for n, a in zip(nombres, apellidos)];   #Recordemos que zip se usa para unir los valores de 2 listas en forma de tupla, si se quiere imprimir se debe colocar list(variablezip)