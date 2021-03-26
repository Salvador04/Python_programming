'''
NAME
	amino_acid_percentage.py

VERSION
	4.1

Author
	Salvador Gonzalez Juarez <salglzj@lcg.unam.mx>

Description

	This program reads a fasta file that contains amino acid sequences and calculates the percentage of
	one or more amino acids in that sequences. User can choose between one or more amino acids. Version
	4.1 allows the read of a fasta file that contains more than one amino acid sequence.

CATEGORY
	Amino acid sequence analysis

USAGE
	% usage: amino_acid_percentage.py [-h] -i path/to/file [-a one letter codes] [-r number] [-f]


ARGUMENTS
	-h, --help          show this help message and exit
  	-i path/to/file, --input path/to/file
                        Fasta file with the amino acid sequence.
  	-a One letter code(s), --amino_acids one letter code(s)
                        The amino acids that you choose. Separate each amino
                        acid only by a comma.
  	-r number, --round number
                        Number of decimals in the percentage result.
  	-f, --flag          Displays a graphic result when is active.
'''

# Imports a module which helps to the visual display.
from tabulate import tabulate

# Creates an object to manipulate arguments.
import argparse
parser = argparse.ArgumentParser(description = "This program calculates the percentage of one or more amino acid residues in amino acid sequences.")

# Adds the input argument to parser object. This argument is required in the command.
parser.add_argument(
  "-i", "--input",
  metavar = "path/to/file",
  help = "Fasta file with the amino acid sequence.",
  required = True)

# Adds the amino acids argument to parser object. This argument is not required in the command.
parser.add_argument(
  "-a", "--amino_acids",
  metavar = "one letter code(s)",
  default = "A,R,N,D,C,E,Q,G,H,I,L,K,M,F,P,S,T,W,Y,V",
  help = "The amino acids that you choose. Separate each amino acid only by a comma.",
  required = False)	

# Adds the round argument to parser object. This argument is not required in the command.
parser.add_argument(
  "-r", "--round",
  metavar = "number",
  default = 2,
  help = "Number of decimals in the percentage result.",
  type = int,
  required = False
  )

# Adds the flag argument to parser object. This argument is not required in the command.
parser.add_argument(
  "-f", "--flag",
  help = "Displays a graphic result when is active.",
  action = "store_true",
  required = False)
	
# Ends the creation of the parser object.
args = parser.parse_args()

def get_amino_acid_content(sequence, amino_acid, round_number):
	'''
	This function calculates a residue percentage in an amino acid sequence, by calculating its
	amount of the residue in its total lenght.
	:param sequence: str, the complete amino acid sequence obtained from the fasta file.
	:param residue: str, one code of the residue searched by the user.
	:param [OPTIONAL] round_number: int, the number of decimals of the result.
	:return float, percentage of the residue in the amino acid sequence.
	'''	
	amino_acid_content = sequence.count(amino_acid)
	amino_acid_content = round((amino_acid_content * 100) / len(sequence), round_number)		
	return amino_acid_content

# Ensure that the function works correctly, with the next examples.
assert get_amino_acid_content("MSRSLLLRFLLFLLLLPPLP", "M", 2) == 5.0, "Function's error."
assert get_amino_acid_content("MSRSLLLRFLLFLLLLPPLP", "L", 2) == 50.0, "Function's error."
assert get_amino_acid_content("msrslllRFLLFllllPPLP", "Y", 2) == 0, "Function's error."

# Validates that the input file path exists.
try:
	input_file = args.input

	# Saves the value of the arguments "round" and "flag".
	decimals = args.round
	graphical_mode = args.flag

	# Creates an empty dictionary where the peptides and their amino acid sequences will be associated.
	peptide_list = {}

	# Opens the file which contains the amino acid sequences and reads it line per line.
	with open(input_file, "r") as file_handler:
		for fasta_sequence in file_handler:

			# Ignores all the lines that aren't peptide info or amino acid sequences.
			if fasta_sequence.startswith("#"):
				continue

			# Gets the name of the amino acid sequence and continues with the next line.
			if fasta_sequence.startswith(">"):
				peptide_name = fasta_sequence.split(" ")
				peptide_name = peptide_name[0]
				amino_acid_sequence = ""
				continue

			# Deletes the end line jumper and concatenates the line's sequence with the others
			# lines' sequences of the same peptide.
			fasta_sequence = fasta_sequence.replace("\n", "")
			amino_acid_sequence = amino_acid_sequence + fasta_sequence.upper()
			peptide_list[peptide_name] = amino_acid_sequence

	# Validates that the file is not empty.
	if peptide_list:

		# Assigns the one letter codes to their respective amino acids name in a dictionary.
		one_letter_codes = {
			"A" : "Alanine",
			"R" : "Arginine",
			"N" : "Asparagine",
			"D" : "Aspartic acid",
			"C" : "Cysteine",
			"E" : "Glutamic acid",
			"Q" : "Glutamine",
			"G" : "Glycine",
			"H" : "Histidine",
			"I" : "Isoleucine",
			"L" : "Leucine",
			"K" : "Lysine",
			"M" : "Methionine",
			"F" : "Phenylalanine",
			"P" : "Proline",
			"S" : "Serine",
			"T" : "Threonine",
			"W" : "Tryptophan",
			"Y" : "Tyrosine",
			"V" : "Valine"
			}

		# Saves the value of the argument "amino acids" and makes it a list.
		searched_amino_acids = args.amino_acids
		searched_amino_acids = searched_amino_acids.upper().split(",")

		# Filters the correct one letter codes in the previous list.
		amino_acid_list = [each_amino_acid for each_amino_acid in searched_amino_acids if len(each_amino_acid) == 1 and each_amino_acid in one_letter_codes]

		# Creates an empty list if the graphical mode is on.
		if graphical_mode:
			results_table = []

		# Validates that the user wrote, at least one valid one letter code.
		if amino_acid_list:

			# Calculates the percentage of each amino acid in each peptide sequence.
			for peptide, sequence in peptide_list.items():
				percentage_results = {each_amino_acid : str(get_amino_acid_content(sequence, each_amino_acid, decimals)) for each_amino_acid in amino_acid_list}
		
				# Creates a list that saves the results of the amino acid percentages of all peptides
				# sequences, if the graphical mode is on.
				for each_amino_acid, value in percentage_results.items():	
					if graphical_mode:				
						results_table.append([peptide, each_amino_acid, one_letter_codes[each_amino_acid], value, str(sequence.count(each_amino_acid))])

				# Prints the results of the amino acid percentages of all peptides sequences, if the
				# graphical mode is off.
					else:
						print(peptide, "\t", each_amino_acid, "\t", one_letter_codes[each_amino_acid], "\t", value, "\t", str(sequence.count(each_amino_acid)))

			# Prints the results in a graphic form if graphical mode is on.
			if graphical_mode:
				print(tabulate(results_table, headers = ["Peptide","OLC", "Amino acid", "Percentage", "Appearances"]))

		# Indicates if the user didn't write any one letter code.
		else:
			print("Error: You didn't write any valid one letter code.")

	# Indicates if the file is empty.
	else:
		print("Error: No sequence found in the file.")

# Indicates if the input file path has not been found.
except FileNotFoundError:
	print("Error: The input file path doesn't exist.")

# Indicates if the input file is not a fasta file.
except NameError:
	print("Error: The input file is not a fasta file.")



