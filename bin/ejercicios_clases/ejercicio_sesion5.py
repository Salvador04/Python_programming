# 1. Abrir el archivo
file_handler = open(" ")
new_file_handler = open(" ")
# 2. Recorrer el archivo linea por linea
while True:
	line = file_handler.readline()
	if not line:
		break
	line = line.replace("\n","")
# 3. Ignorar lineas que son encabezados
	if line.startswith("#"):
		continue
# 4. Generar una lista con el contenido de cada linea.
	gene_data = line.split(",")
# 5. Obtener tipo de gen.
	gene_type = gene_data[3]
# 6. Ignorar genes que no sean de tipo gene
	if gene_type != "gene":
	continue
# 7. Determinar que la secuencia existe
	gene_sequence = gene_data[1]
	if gene_sequence == "":
	continue
# 8. Determinar si la secuencia esta en direccion forward o reverse
	gene_strand = gene_data[5]
# 9. Si es reverse calcular su reverso complementario. 
	if gene_strand.lower() == "reverse":
		gene_seqence = gene_sequence[::-1]
		gene_sequence = gene_sequence.replace("a","T").replace("a","T").replace("c","G").replace("g","C")
# 10. Calcular el contenido de AT
	at_content = gene_sequence.count("A") + gene_sequence.count("T")
	sequence_lenght = len(gene_sequence)
	at_content = (at_content/sequence_lenght) * 100
# 11. Guardar el resultado en un nuevo archivo
	new_file_handler.write(f'{at_content}, {gene_sequence}\n')
# 12. Cerrar ambos archivos
new_file_handler.close()
file_handler.close()