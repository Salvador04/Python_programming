Licenciatura en ciencias genomicas - Introduccion a Python.

Por Salvador Gonzalez Juarez.

# Sesion 9 - List Comprehension, Dictionary Comprehension y Argumentos en la linea de comando

## List comprehension:

Otra forma de construir listas:

```python
# 1. Nueva variable tipo lista
# 2. Elemento que se guardara en la nueva lista
# 3. Elemento N del iterable
# 4. Objeto iterable
'1'list_variable = ['2'elem for '3'elem in '4'iterable]
```

Agregar los elementos a la nueva lista:

```python
# Normalmente:
gene_sequence = "ATCG"
nucleotides = []
for nucleotide in gene_sequences:
	nucleotides.append(nucleotide)
	
# Comprension de listas:

gene_sequence = "ATCG"
nucleotides = [nucleotide for nucleotide in gene_sequence]
```

Aplicar cambios al valor que se guardará en la nueva lista:

```python
# Normalmente:
at_contents = [.13141, .53123, .65123123]
at_contents_formatted = []
for content in at_contents:
	at_contents_formatted.append(content*100)

# Comprension de listas:
at_contents = [.13141, .53123, .65123123]
at_contents_formatted = [content*100 for content in at_contents]
```
Aplicar metodos al valor que se guardara en la nueva lista:

```python
# Normalmente:
sequences = ["ATCG", "ATCG\n", "ATCG\n"]
new_sequences = []
for sequence in sequences:
	new_sequences.append(sequence.strip())

# Comprension de listas:
sequences = ["ATCG", "ATCG\n", "ATCG\n"]
new_sequences = [sequence.strip() for sequence in sequences]
```

Aplicar condicionales en la comprension de listas:

```python
# Normalmente:
genes = ["araC", "araB", "araD", "crp", "tyrR"]
new_genes = []
for gene in genes:
	if gene.startswith("a");
		new_genes.append(gene)

# Comprension de listas:
genes = ["araC", "araB", "araD", "crp", "tyrR"]
new_genes = [gene for gene in genes if gene.starswith("a")]
```

Aplicar ciclos anidados:

```python
# Normalmente:
all_trinucleotides = []
for base1 in ["A", "T", "C", "G"]:
	for base2 in ["A", "T", "C", "G"]:
		for base3 in ["A", "T", "C", "G"]:
			trinucleotide = base1 + base2 + base3
			all_trinucleotides.append(trinucleotide)

# Comprension de listas :
all_trinucleotides = [base1 + base2 + base3 for base1 in ["A", "T", "C", "G"] for base2 in ["A", "T", "C", "G"] for base3 in ["A", "T", "C", "G"]]
```

## Dictionary comprehension:

Construyendo un diccionario a partir de un ciclo:

```python
gene_names = ["araC", "araD", "araJ"]
gene_sequences = ["ATCG", "TTCT", "GTAC", "CATG"]
genes = {}
for index, gene_name in enumerate(gene_names):
	genes[gene_name] = gene_sequences[index]
```

Otra forma de construir diccionarios:

```python
# 1. Nueva variable de tipo diccionario.
# 2. Llave que tendra el nuevo diccionario.
# 3. Valor enlazado a la llave del diccionario.
# 4. Llave del elemento iterado.
# 5. Valor del elemento iterado.
# 6. Diccionario a iterar.
'1'new_dictionary = {'2'key : '3'value for '4'key, '5'value in '6'dictionary.items()}
```

Copiar el contenido de un diccionario en otro:

```python
# Normalmnte:
gene = {"gene" : "araC", "sequence" : "ATCG"}
new_gene = {}
for key, value in gene.items():
	new_gene[key] = value 

# Comprension de diccionarios:
gene = {"gene" : "araC", "sequence" : "ATCG"}
new_gene = {key : value for key, value in gene.items()}
```

Aplicar cambios al valor que se guardara en el nuevo diccionario: 

```python
# Normalmente:
at_contents = {"araC" : .1314, "araB" : .53123, "araD" : .65123123}
at_contents_formatted = {}
for gene_name, at_content in at_contents.items():
	at_contents_formatted[gene_name] = at_content * 100

# Comprension de diccionarios:
at_contents = {"araC" : .1314, "araB" : .53123, "araD" : .65123123}
at_contents_formatted = {gene_name : at_content * 100 for gene_name, at_content in at_contents.items()}
```

Aplicar metodos al valor que se guardara en el nuevo diccionario:

```python
# Normalmnte:
genes = {"araC": "ATCG", "araD" : "ATCG\n", "araB" : "ATCG\n"}
genes_formatted = {}
for gene_name, seqquence in gene.items():
	genes_formatted[gene_name] = sequence.strip()

# Comprension de diccionarios:
genes = {"araC": "ATCG", "araD" : "ATCG\n", "araB" : "ATCG\n"}
genes_formatted = {gene_name : sequence.strip() for gene_name, sequence in genes.items()}
```

Aplicar condicionales en la comprension de diccionarios:

```python
# Normalmente:
genes = {"araC": "ATCG", "araD" : "ATCT", "araB" : "ATTA", "crp" : "GCTT", "tyrR" : "ATCT"}
new_genes = {}
for gene_name, gene_sequence in genes.items():
	if gene_name.startswith("a"):
		new_genes[gene_name] = gene_sequence
		
# Comprension de diccionarios:
genes = {"araC": "ATCG", "araD" : "ATCT", "araB" : "ATTA", "crp" : "GCTT", "tyrR" : "ATCT"}
new_genes = {name : sequence for name, sequence in genes.items() if name.startswith("a")}
```

Iterar otro tipo de objetos para realizar la comprension de diccionarios:

```python
# Normalmente:
gene_names = ["araC", "araD", "araJ"]
gene_sequences = ["ATCG", "CGTA", "AACT"]
genes = {}
for index, gene_name in enumerate(gene_names):
	genes[gene_name] = gene_sequences[index]
	
# Comprension de diccionarios:
gene_names = ["araC", "araD", "araJ"]
gene_sequences = ["ATCG", "CGTA", "AACT"]
genes = {name : gene_sequences[index] for index, name in enumerate(gene_names)}
```

## Command line arguments:

###  ¿Que es un argumento?

Valores que se pueden utilizar dentro del programa y que son especificados en la terminal depues del nombre del programa:

```bash
python3 get_at_content.py ruta_de_mi_archivo
```

### Formas distintas de utilizar los argumentos:

- Sin opciones, 1 argumento:
```bash
python get_at_content.py gene_sequences.txt
```

- Sin opciones, 2 argumentos, es necesario respetar el orden en que se ingresan los argumentos:
```bash
python get_at_content.py gene_sequences.txt output/gene_at_content.txt
```

- Con opciones, n argumentos, no importa el orden en que se ingresan los argumentos:
```bash
python get_at_content.py -input gene_sequences.txt -output output/gene_at_content.txt
```

### Utilizando argumentos con python:

**sys.argv** es un arreglo con los argumentos que se le dan al programa, siendo el elemento en la posicion 0 el nombre del programa:

```python
import sys
arguments = sys.argv
```
Utilizando el argumento dentro del scipt:

```python
import sys
arguments = sys.argv
file_path = arguments[1]
with open(file_path, 'r') as file_handler:
	for line in file_handler:
		print(line)
```

### Utilizando argparse, biblioteca para manejo de argumentos:

```python
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
  required=False)
	
# Agregando argumento cuya función es servir como bandera
parser.add_argument(
  "-f", "--flag",
  help="Argumento que sirve como bandera",
  action='store_true')
	
args = parser.parse_args()
print(args.input, args.output, args.flag)
```


