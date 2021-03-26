def get_at_content(sequence, round_number):
	'''
	Retorna el contenido de AT de una secuencia a dos decimales por default
	:param sequence: str, Cadena a obtener su contenido de AT
	:param round_number: int, numero de decimales del resultado
	:return: float, Valor del contenido de AT
	'''
	try:
		at_content_result = None
		if not isinstance(sequence, str):
			raise AttributeError("El primer parametro no es de tipo cadena")

		at_content = sequence.count("A") + sequence.count("T")
		sequence_lenght = len(sequence)
		at_content = (at_content / sequence_lenght)* 100
		at_content_result = round(at_content, round_number)

	except TypeError:
		at_content_result = round(at_content, 2)

	except AttributeError as err:
		print("error: ", err)

	return at_content_result


print(get_at_content("ATCGCGTGCCT", 3))