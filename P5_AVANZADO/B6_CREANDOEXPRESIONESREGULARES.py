import re;

text = "Holaaaa, mi numero es: +54 11 4321-4321 +52 56 3253-2364";

pattern = r'\+\d{2,3}\s\d{2}\s\d{4}-\d{4}';

replace = re.sub(pattern, "(Número Censurado)", text);

print(replace);