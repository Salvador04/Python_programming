'''
NAME
	delete_adapters

VERSION
	2.0

Author
	Salvador Gonzalez Juarez <salglzj@lcg.unam.mx>

Description
	This program removes a varible length of nucleotides adapter from some nucleotide sequences in a file. The remaining sequences are written
	in a new file. Finally, prints the lenght of each remaining sequence. Version 2.0 allows the user to choose an input file and an output
	file as arguments in the command.

CATEGORY
	DNA analysis

USAGE
	% delete_adapters.py [-h] -i path/to/file -o path/to/file [-n number]

ARGUMENTS
	-h, --help			show this help message and exit
  	-i path/to/file, --input path/to/file
                        File with the nucleotide sequence.
  	-o path/to/file, --output path/to/file
                        File where the results will be printed.
  	-n number, --nucleotides number
                        Number of nucleotides that will be deleted as adapter.
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

# Adds the output argument to parser object. This argument is required in the command.
parser.add_argument(
  "-o", "--output",
  metavar = "path/to/file",
  help = "File where the results will be printed.",
  required = True)

# Adds the nucleotides argument to parser object. This argument isn't required in the command.
parser.add_argument(
  "-n", "--nucleotides",
  metavar = "number",
  help = "Number of nucleotides that will be deleted as adapter.",
  type = int,
  required = False)
	
# Ends the creation of the parser object.
args = parser.parse_args()

def remove_nucleotides(sequence, nucleotides_removed):
	'''
	This function removes a nucleotide length from the begining of a nucleotide sequence.
	:param sequence: str, the nucleotide sequence obtained from the file.
	:param [OPTIONAL] nucleotides_removed: int, the number of nucleotides that will be removed. It's 14 by default.
	:return str, processed sequence without adapters.
	'''
	try:
		if nucleotides_removed >= 0:
			new_sequence = sequence[nucleotides_removed:]

	except TypeError:
		new_sequence = sequence[14:]		
	
	return new_sequence

# Ensure that the function works correctly, with the next examples.
assert remove_nucleotides("ATCGATCG", 4) == "ATCG", "Function's error."

# Prints an initial message.
print("\nWelcome to delete_adapters 2.0")

# Validates that the input file path exists.
try:
	input_file = args.input

	# Saves the value of the argument 'nucleotides'.
	adapter_length = args.nucleotides

	# Opens the file where the results will be written.
	output_file = args.output
	with open(output_file, 'w') as output_file_handler:

		# Opens the file which contains the nucleotide sequences and reads it line per line.
		with open(input_file, 'r') as input_file_handler:
			print("\nResults:")
			for nucleotide_sequence in input_file_handler:

				# Deletes the end line jumper for each line.
				nucleotide_sequence = nucleotide_sequence.replace("\n", "")

				# Creates a processed sequence without adapters for each sequence and writes it in the output file.
				processed_sequence = remove_nucleotides(nucleotide_sequence, adapter_length)
				output_file_handler.write(processed_sequence + "\n")

				# Prints the lenght of each processed sequence.
				print("\n\tThe lenght of the processed sequence is " + str(len(processed_sequence)) + " nucleotides.")

# Indicates if the input file path has not been found.
except FileNotFoundError:
	print("\nError: The input file path doesn't exist.\n\nThe program has ended.")

# Indicates that the program has ended.
else:
	print("\nThe program has ended successfully.")






