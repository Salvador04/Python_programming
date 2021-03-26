def get_complementary(sequence):
	'''
	Gets and returns tha complementary sequence for a given sequence.
	:param sequence: str, the reverse sequence.
	:return str, the complementary sequence.
	'''
	try:
		complementary_sequence = None
		if not isinstance(sequence, str):
			raise AttributeError("The first parameter isn't a string type")

		complementary_sequence = sequence.replace('A', 't').replace('T', 'a')
		complementary_sequence = complementary_sequence.replace('C', 'g').replace('G', 'c')
		complementary_sequence = complementary_sequence.upper()
		complementary_sequence = complementary_sequence[::-1]

	except AttributeError as err:
		print("error: ", err)

	return complementary_sequence

def get_at_content(sequence, round_number):
	'''
	Returns the AT content for a given sequence, with 2 decimal by default.
	:param sequence: str, The string which we want to calculate its AT content.
	:param round_number: int, decimal number of the result.
	:return: float, AT content value.
	'''
	try:
		at_content_result = None
		if not isinstance(sequence, str):
			raise AttributeError("The first parameter isn't a string type")

		at_content = sequence.count("A") + sequence.count("T")
		sequence_lenght = len(sequence)
		at_content = (at_content / sequence_lenght)* 100
		at_content_result = round(at_content, round_number)

	except TypeError:
		at_content_result = round(at_content, 2)

	except AttributeError as err:
		print("error: ", err)

	return at_content_result

def get_gc_content(sequence, round_number):
	'''
	Returns the GC content for a given sequence, with 2 decimal by default.
	:param sequence: str, The string which we want to calculate its GC content.
	:param round_number: int, decimal number of the result.
	:return: float, GC content value.
	'''
	try:
		gc_content_result = None
		if not isinstance(sequence, str):
			raise AttributeError("The first parameter isn't a string type")

		gc_content = sequence.count("G") + sequence.count("C")
		sequence_lenght = len(sequence)
		gc_content = (gc_content / sequence_lenght)* 100
		gc_content_result = round(gc_content, round_number)

	except TypeError:
		gc_content_result = round(gc_content, 2)

	except AttributeError as err:
		print("error: ", err)

	return gc_content_result

def get_residue_content(sequence, residue):
	'''
	Calculates a residue percentage in an amino acid sequence, by calculating its amount of the residue between its total lenght.
	:param sequence: str, the complete amino acid sequence obtained from the fasta file.
	:param residue: str, one code of the residue searched by the user.
	:return float, percentage of the residue in the amino acid sequence.
	'''
	residue = residue.upper()
	residue_content = sequence.count(residue)
	residue_content = round((residue_content * 100) / len(sequence), 2)
	return residue_content