'''
NOMBRE
    porcentaje_AT.py

VERSION
    1.0

AUTOR
    Salvador Gonzalez Juarez <salglzj@lcg.unam.mx>

DESCRIPCION
    Programa capaz de calcular el porcentaje de ocurrencia de los nucleotidos Adenina (A)
    y Timina (T) en una secuencia de nucleotidos ingresada por el usaurio

CATEGORIA
    Analisis de secuencia

USO
    Porcentaje de AT en una secuencia de nucleotidos 

'''

# Pide al usuario que ingrese una secuencia de nucleotidos cualesquiera
sequencia = input("Bienvenido a porcentaje_AT.py. Escriba una secuencia de nucleotidos usando letras mayusculas para calcular su porcentaje de AT: ")

# Metodo para cuantificar la cantidad de A y T en la cadena seq
cont_AT = sequencia.count('A') + sequencia.count('T')

# Calcula el porcentaje de AT dividiendo la variable cont_AT entre la longitud en caracteres de la variable seq, por medio de la funcio len ()
porcent_AT = (cont_AT / len(sequencia)) * 100

# Imprime el valor de la variable porcent_AT, la cual corresponde al porcentaje de AT de la secuencia
print("El porcentaje de AT en la secuencia es", porcent_AT, "%")
