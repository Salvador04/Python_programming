# Corre el archivo y solamente lo hace legible
archivo = open("/home/salvador/Documentos/python_curso/source/archivo.txt", "r")

# Lee el archivo y lo almacena en una variable, para poder manipularlo
lectura_archivo = archivo.read()

# Imprime el contenido del archivo
print(lectura_archivo)

# Imprime los primeros 10 caracteres del archivo
print(lectura_archivo[0:10])

# Imprime la longitud del archivo
print(len(lectura_archivo))

# Reemplaza un caracter por otro
lectura_archivo = lectura_archivo,replace()

# Elimina el ultimo caracter de la cadena
lectura_archivo = lectura_archivo.rstrip("\n")

# Elimina el primer caracter de la cadena
lectura_archivo = lectura_archivo.lstrip("\n")

# Elimina el primer y ultimo caracter de la cadena
lectura_archivo = lectura_archivo.lstrip("\n")

# Reescribe el archivo
archivo = open("/home/salvador/Documentos/python_curso/source/archivo.txt", "w")

# Coloca la nueva informacion al final del archivo
archivo = open("/home/salvador/Documentos/python_curso/source/archivo.txt", "a")

# Editar el archivo de texto vacio
lectura_archivo = archivo.write("\nsaltodelinea")

# Cierra el archivo
archivo.close()

# Lee un archivo a partir de una ruta relativa
my_file = open("../source/archivo.txt", "w")

# Escribe sobre el archivo
my_file.write("ruta relativa")

# Cierra el archivo
my_file.close()

# Lee un archivo a partir de una ruta absoluta
my_file = open("/Documentos/python_curso/source/archivo.txt", "r")

# Creando archivo, con escritura y lectura
file = open(".../source/archivo_secuencia.txt", "w+")

# Ingresando secuencia al archivo
file.write("ATCGT")

