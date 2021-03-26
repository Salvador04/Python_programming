Licenciatura en ciencias genomicas - Introduccion a Python.

Por Salvador Gonzalez Juarez.

# Sesion 8 - Diccionarios

## Problema:

```python
# Dada la secuencia, contar el numero de veces que se repite el nucleotido "A".

dna = "ACTGAGCTGACGTAGC"

a_count = dna.count("A")

# Y ahora en dinucleotidos?

aa_count = dna.count("AA")
at_count = dna.count("AT")
ac_count = dna.count("AC")
ag_count = dna.count("AG")

# Se vuelve un problema con trinucleotidos.

all_counts = []

for base1 in ['A','T', 'C', 'G']:
	for base2 in ['A', 'T', 'C', 'G']:
		for base3 in ['A', 'T', 'C', 'G']:
		trinucleotide = base1 + base2 + base3
		count = dna.count(trinucleotide)
		print("count is " + str(count) + " for " + trinucleotide)
		all_counts.append(count)
		
print(all_counts)

```

Sin embargo esto puede causar confusion, queda mas claro asi:

```python
dna = "ACTGAGCTGACGTAGC"

# Agregamos:
all_trinucleotides = []

all_counts = []

for base1 in ['A','T', 'C', 'G']:
	for base2 in ['A', 'T', 'C', 'G']:
		for base3 in ['A', 'T', 'C', 'G']:
		trinucleotide = base1 + base2 + base3
		count = dna.count(trinucleotide)
		
		# Agregamos:
		all_trinucleotides.append(trinucleotide)
		
		print("count is " + str(count) + " for " + trinucleotide)
		all_counts.append(count)
		
print("Todos los conteos: ", all_counts)
```

Pero todavia queda mejor con el uso de **DICCIONARIOS**. Los diccionarios nos permiten almacenar valores asociados a una **llave unica**. A continuacion se muestra como definir un diccionario:

```python
# Diccionario = {KEY : VALUE}
gen = {"name" : "araC"}
		# ITEM 1

gen = {"name" : "araC", "sequence" : "ATCG"}
		# ITEM 1				ITEM2

```

Si se utiliza una llave ya usada, se reemplaza el valor a su ultima asociacion. Se puede asociar de las siguientes dos formas:

```python
# Forma 1:
all_counts = {
    "AAA" : 0,
    "AAT" : 1,
    "AAC" : 0,
    "AAG" : 0,

# Forma 2:
all_counts = {}
all_counts["AAA"] = 0
all_counts["AAT"] = 1
all_counts["AAC"] = 0
all_counts["AAG"] = 0
}
```

## Contando valores repetidos:

```python
genes = ["araC", "araJ", "tyrR", "crp", "araB", "araC"]
genes_info = {}
for gene_name in genes:
	if "araC" in genes:
		genes_info[gene_name] = genes_info[gene_name] + 1
	else:
	genes[gene_name] = 1

# Si la llave no existe, inserta la llave, con el valor especificado '.setdefault()' es un metodo que retorna el valor del item con la llave especifica:

genes = {}
for gene_name in genes:
	genes.setdefault(gene_name, 1)
	genes[gene_name] += 1
```

## Obteniendo un valor:

```python
all_counts = { "AAA" : 0, "AAT" : 1, "AAC" : 0, "AAG" : 0 }

# Obteniendo el valor de una llave:
print(all_counts["AAT"])
# > 1

# La siguiente linea causa un error, porque no encuentra esa llave:
print (all_count["TTT"])

# Utilizar una condicional para evitar el error. Ademas, usar el metodo '.get' el cual asigna un valor por default en caso de querer obtener el valor de una llave no asignada:

if "TTT" in all
	print(all_counts["TTT"])
print (all_counts.get("TTT", None))
# > None
```

## Obteniendo todas las llaves de un diccionario:

```python
all_counts = { "AAA" : 0, "AAT" : 1, "AAC" : 0, "AAG" : 0 }

# El metodo 'keys()' retorna un objeto visible, el cual va a reflejar cualquier cambio realizado al diccionario:
keys = all_counts.keys()

# Agregar una nueva llave al diccionario.
all_counts["ATCG"] = 10
print(keys)
```

## Elimanar una llave:

```python
all_counts = { "AAA" : 0, "AAT" : 1, "AAC" : 0, "AAG" : 0 }

# Usando la palabra reservada 'del':
del all_counts["AAA"]

# El metodo '.pop' retorna el valor de la llave eliminada:
value = all_counts.pop("AAT")
```

## Recorriendo un diccionario:

```python
all_counts = { "AAA" : 0, "AAT" : 1, "AAC" : 0, "AAG" : 0 }

# Imprimindo todos los valores de un diccionario:

for key in all_counts:
	print(key)

# Para que tambien imprima el valor de cada llave:
for key in all_counts:
	print(key, '->', all_counts[key])
	
# El metodo '.items()' nos ayuda a imprimir cada llave co su respectivo valor en formato de tupla:

for item in all_counts.items():
	print(item)

# Para deshacer la tupla cuando usamos el metodo '.items()':
for llave, valor in all_counts.items():
	print(llave, valor)
```

## Solucionando el problema con diccionarios:

Regresamos al problema inicial, pero vamos a aplicar lo aŕendido hasta ahora:

```python
dna = "AATGATCGATCGTACGCTGA"

trinucleotide_count {}

for base1 in ['A','T', 'C', 'G']:
	for base2 in ['A', 'T', 'C', 'G']:
		for base3 in ['A', 'T', 'C', 'G']:
		
			trinucleotide = base1 + base2 + base3
		
			trinucleotide_count[trinucleotide] = dna.count(trinucleotide)
		
print(trinucleotide_count)
```

Ahora el dicionario se ve bastante bien. Vamos a guardar ahora solo aquellas llaves cuyo valor sea mayor a 1:

```python
dna = "AATGATCGATCGTACGCTGA"

trinucleotide_count {}

for base1 in ['A','T', 'C', 'G']:
	for base2 in ['A', 'T', 'C', 'G']:
		for base3 in ['A', 'T', 'C', 'G']:
			trinucleotide = base1 + base2 + base3
			
		# Agregamos:
		count = dna.count(trinucleotide)
		if count > 1:
			trinucleotide_count[trinucleotide] = count
		
print(trinucleotide_count)
```

## Listas dentro de diccionarios:

Existen dos formas de asociar listas dentro de diccionarios:

```python
# Tenemos dos listas:
genes = ["araC", "araD", "araA"]
products = ["AraC", "CRP", "TyrR"]

# Forma 1:
ecoli= {}
ecoli["genes"] = genes
ecoli["products"] = products

# Forma 2:
ecoli ={
    "genes" : genes,
    "products" : products
}

print(ecoli)

# Como acceder a ciertos elementos:

ecoli["genes"][2]
# > "araA"
ecoli["products"][1]
# > "CRP"

# Podemos manipular las listas dentro de diccionarios con los mismos metodos de las listas normales:

# Agregamos un nuevo gen a la lista:

ecoli["genes"].append("araE")
ecoli["genes"].insert(0, "araB")

# Ahora si queremos eliminar un gen:

del ecoli["genes"][0]
ecoli["genes"].remove("araE")
```

## Diccionarios dentro de diccionarios:

```python
# Tenemos un diccionario:
genes = {
	"araC" : "ATG...",
    "araD" : "ATG...",
    "araA" : "ATG..."
}

# Y tenemos otro diccionario:
products = {
    "AraC" : "ATG...",
    "CRP" : "ATG...",
    "TyrR" : "ATG..."
}

# Asociamos ambos a un diccionario diferente de la siguiente forma:
ecoli = {}
ecoli["genes"] = genes
ecoli["products"] = products

# Entrar a un elemento:

ecoli["genes"]["araC"]

# Agregar un nuevo elemento:

ecoli["products"][Prot] = "MGT"

ecoli["products"].setdefault('proteina','sec')
```

## Agregando elementos a una lista dentro de un diccionario:

```python
transcription_factors = {
    "AraC" : ["araC", "araB", "araD", "araC"],
    "CRP" : ["araC", "crp", "deoR"]
}

new_regulated_genes = {
    "AraC" : "feuR",
    "CRP" : "aoxR",
    "TyrR" : "ajaJ"
}

for transcription_factor, regulated gene in new_regulated_genes.items():
	transcription_factor.setdefault(transcription_factor, []).append(regulated_gene)
```
