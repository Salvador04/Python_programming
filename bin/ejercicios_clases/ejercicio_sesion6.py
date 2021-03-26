'''
NAME
	get_Ecoli_sRNA.py

VERSION
	1.0
Author
	Salvador Gonzalez Juarez <salglzj@lcg.unam.mx>

Description
	This program searches for sRNA genes in an E. coli genes database. It saves the name and the nucleotide sequence of
  	each sRNA gene, as Fasta format, in a new file. Finally, prints to screen the name and the nucleotide sequence
  	lenght of each sRNA gene. 

CATEGORY
	Gene analysis

USAGE
	Get sRNA genes 

ARGUMENTS
	input: /Gene_sequence.txt
	output: /sRNA_genes_Ecoli.txt
'''

def get_complementary(sequence):
	'''
	Obtiene y retorna la secuencia complementara a la secuencia dada
	:param sequence: str, la secuencia reverse
	:return str, secuencia complementaria
	'''
	sequence = sequence.replace('A', 't').replace('T', 'a')
	sequence = sequence.replace('C', 'g').replace('G', 'c')
	sequence = sequence.upper()
	sequence = sequence[::-1]
	return sequence

assert get_complementary("ATCG") == "CGAT", "Checa tu funcion"
print(get_complementary("ATCG"))

def get_at_content(sequence, round_number = 2):
	'''
	Retorna el contenido de AT de una secuencia a dos decimales por default
	:param sequence: str, Cadena a obtener su contenido de AT
	:param round_number: int, numero de decimales del resultado
	:return: float, Valor del contenido de AT
	'''
	at_content = sequence.count("A") + sequence.count("T")
	sequence_lenght = len(sequence)
	at_content = at_content / sequence_lenght
	at_content = at_content * 100
	return round(at_content, round_number)

print(get_at_content("ATCG"))