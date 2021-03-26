'''
NAME
	at_content_files

VERSION
	o.0

Author
	Salvador Gonzalez Juarez <salglzj@lcg.unam.mx>

Description
	Calcular el contenido de AT de secuencias en forma de listas almacendas en un archivo de texto.

CATEGORY
	DNA analysis

USAGE
	

ARGUMENTS
	N/A

'''


# 1. Definir los pasos a realizar.
# 2. Abrir el archivo y asignarlo a la variable del archivo
file = open("../source/sequence_sesion4.txt", "r")
# 3. Recorrer el archivo linea por linea
for gene in file:

# Eliminando el salto de linea
	gene_list = gene.rstrip()

# 4. Obtener la secuencia de linea
	gene_list = gene_list.split(",")

	gene_sequence = gene_list[1]

	at_count = gene_sequence.count("A") + gene_sequence.count("T")

	at_content = (at_count/len(gene_sequence)) *100

	print(at_content)

file.close()




# 5. Calcular el contenido de AT
# 6. Imprimir resultados