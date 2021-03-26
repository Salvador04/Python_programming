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
# Opens the file which contains all the gene sequences and the new file where the chosen sRNA genes will be saved.
RegulonDB_file = open("/home/salvador/Documentos/python_curso/source/Gene_sequence.txt", "r")
sRNA_Ecoli = open("/home/salvador/Documentos/python_curso/docs/sRNA_genes_Ecoli.txt", "w") 

# Reads the file line per line, and breaks the loop structure when there are no more lines. Removes the jump line of each end line.
while True:
	line = RegulonDB_file.readline()
	if not line:
		break
	line = line.replace("\n","")
	
# Ignores the header lines and generates a list with the content of each remaining lines.
	if line.startswith("#"):
		continue
	gene_data = line.split("\t")

# Ignores the genes that aren't genes.
	if gene_data[5] != "small RNA":
		continue

# Gets the lenght of each gene's sequence. Ignores the sequences greater than 300bp of lenght. And defines that the gene actually has a sequence.
	seq_lenght = len(gene_data[9])
	if seq_lenght >= 300:
		continue
	gene_sequence = gene_data[9]
	if gene_sequence == "":
		continue

# Defines if the sequence is on the forward or reverse strand. If the gene is on the reverse strand, calculates its complementary reverse. 
	gene_strand = gene_data[4]
	if gene_strand.lower() == "reverse":
		gene_sequence = gene_sequence[::-1]
		gene_sequence = gene_sequence.replace("a","T").replace("t","A").replace("c","G").replace("g","C")
		
# Gets the gene's name and saves it with its sequence as Fasta format, in the new file. Prints to screen the chosen gene's name and lenght.
	gene_name = gene_data[1]
	sRNA_Ecoli.write("> " + gene_name + "\n" + gene_sequence + "\n")
	print(gene_name + "\t" + str(seq_lenght))
	
# Finally, closes both files.
RegulonDB_file.close()
sRNA_Ecoli.close()
