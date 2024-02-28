#Promedio duracion
otros_cursos_min = 2.5;
otros_cursos_max = 7;
otros_cursos_promedio = 4;
dalto_curso = 1.5;

#Diferencia de duracion

diferencia_con_min = (otros_cursos_min * 100 / dalto_curso) - 100;
diferencia_con_min = round(diferencia_con_min, 2);

diferencia_con_max = (otros_cursos_max * 100 / dalto_curso) - 100;
diferencia_con_max = round(diferencia_con_max, 2);

diferencia_con_promedio = (otros_cursos_promedio * 100 / dalto_curso) - 100;
diferencia_con_promedio = round(diferencia_con_promedio, 2);

print(f'La diferencia es de: {diferencia_con_min}%');
print(f'La diferencia es de: {diferencia_con_max}%');
print(f'La diferencia es de: {diferencia_con_promedio}%');