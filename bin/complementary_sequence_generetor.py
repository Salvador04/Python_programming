'''
NAME
	complementary_sequence_generetor.py

VERSION
	2.0

Author
	Salvador Gonzalez Juarez <salglzj@lcg.unam.mx>

Description
	This program reads a file which contains a nucleotide sequence and generates the complementary of that sequence, using the Watson-Crick
	rules of base pairing. Finally, prints both sequences. Version 2.0 allows the user to choose an input file as an argument in the command.

CATEGORY
	DNA analysis

USAGE
	% python3 Evaluacion.py [-h] -i path/to/file

ARGUMENTS
  -h, --help            show this help message and exit
  -i path/to/file, --input path/to/file
                        File with the nucleotide sequence.
'''
# Creates an object to manipulate arguments.
import argparse
parser = argparse.ArgumentParser(description = "This program generates the complementary of a nucleotide sequence.")

# Adds the input argument to parser object. This argument is required in the command.
parser.add_argument(
  "-i", "--input",
  metavar = "path/to/file",
  help = "File with the nucleotide sequence.",
  required = True)
	
# Ends the creation of the parser object.
args = parser.parse_args()

def get_complement(sequence):
	'''
	This function generates the complemantary sequence of a nucleotide sequence, by changing the nucleotides of the sequence.
	:param sequence: str, the complete nucleotide sequence obtained from the fasta file.
	:return str, complementary sequence of the nucleotide sequence.
	'''
	complement = sequence.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
	complement = complement.upper()
	complement = complement[::-1]
	return complement

# Ensure that the function works correctly, with the next example.
assert get_complement("ATCG") == "CGAT", "Function's error."

# Prints an initial message.
print("\nWelcome to complementary_sequence_generetor.py 2.0")

# Validates that the input file path exists.
try:
	input_file = args.input

	# Creates an empty string where the nucleotide sequence will be concatenated.
	nucleotide_sequence = ""

	# Creates a variable that saves the nucleotide sequence's name.
	gene_name = "No name"

	# Opens the file which contains the nucleoide sequence and reads it line per line.
	with open(input_file, 'r') as file_handler:
		for fasta_sequence in file_handler:

			# Gets the name of the nucleotide sequence and continues with the next line.
			if fasta_sequence.startswith('>'):
				gene_name = fasta_sequence.split(" ")
				gene_name = gene_name[0]
				continue

			# Deletes the end line jumper and concatenates the line's sequence with the others lines' sequences.
			fasta_sequence = fasta_sequence.replace("\n", "")
			nucleotide_sequence = nucleotide_sequence + fasta_sequence

	# Generates the complementary sequence of the nucleotide sequence.
	complementary_sequence = get_complement(nucleotide_sequence)

	# Prints the name of the nucleotide sequence.
	print("\nResults:")
	print("\nIn this nucleotide sequence:", gene_name)

	# Prints the nucleotide sequence and its complementary.
	print("\tThe original sequence is:\n", "\n\t" + nucleotide_sequence, "\n\n\tand its complementary is:\n", "\n\t" + complementary_sequence)

# Indicates if the input file path has not been found.
except FileNotFoundError:
	print("\nError: The input file path doesn't exist.\n\nThe program has ended.")

# Indicates that the program has ended.
else:
	print("\nThe program has ended successfully.")