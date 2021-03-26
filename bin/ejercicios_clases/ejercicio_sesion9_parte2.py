import argparse

# Creando un objeto para manipular argumentos
parser = argparse.ArgumentParser(description="Programa que obtiene el contenido de AT del archivo de entrada")
# Agregando un argumento al objeto parser y que es requerido
parser.add_argument(
  "-i", "--input",
  metavar="path/to/file",
  help="Archivo con secuencias de genes",
  required=True)
# Agregando otro argumento al objeto parser y que no es requerido
parser.add_argument(
    "-o", "--output",
    help="Ruta que tendra el archivo de salida",
    required=False)
# Convierto el valor del argumento al especificado
parser.add_argument(
  "-r", "--round",
  help="Número a utilizar al redondear",
  type=int,
  required=False
)
# Agregando argumento cuya función es servir como bandera	
parser.add_argument(
  "-f", "--flag",
  help="Argumento que sirve como bandera",
  action='store_true')
args = parser.parse_args()
print(args.input, args.output, args.flag)

input_file = args.input

with open(input_file, 'r') as file_handler:
	for line in file_handler:
		print(line)
