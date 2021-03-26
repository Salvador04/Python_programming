Licenciatura en ciencias genomicas - Introduccion a Python.

Por Salvador Gonzalez Juarez.

# Sesion 5 - Condicionales

Las **condicionales** son expresiones que evaluan a un booleano. Se comparan numeros, listas, cademas, archivos, etc. 

## Operadores booleanos

Los operadores booleanos son los siguientes:

```python
== # Comparacion, no confundir con **=** el cual es una asignacion.

and # Se cumple cuando ambas condiciones son verdaderas.

or # Se cumple cuando al menos una de las dos condiciones es verdadera.

is not # Negacion.
```

## if, else, elif

Nos permiten controlar el flujo de nuestro programa, dependiendo si se cumplen o no ciertas condicionales.

### if: 

```python
# Codigo sujeto a que se cumpla una condicion:
if condicion:
	# Bloque de codigo

# Codigo sujeto a que se cumplan forzosamente dos condiciones:
if condicion1 and condicion2:
    # Bloque de codigo
```

### if else:

```python
# Codigo sujeto a que se cumpla una condicion:
if condicion:
    # Bloque de codigo
# Codigo sujeto a que no se cumpla la condicion anterior:
else:
    # Bloque de codigo
```

### if elif else:

```python
# Codigo sujeto a que se cumpla una condicion:
if condicion:
	# Bloque de código
# Codigo sujeto a que no se cumpla la condicion anterior:
elif condicion2:
	# Bloque de código
# Codigo sujeto a que no se cumpla la condicion anterior:
else:
	# Bloque de código
```

## Ciclo while

El ciclo **while** esta compuesto por: la palabra reservada **while**, una condicion que debera evaluar a **True** seguido de los **:**. El bloque de codigo indentado que se ejecutara mientra la condicion siga siendo verdadera.

```Python
while condicion:
	# Bloque de código
```

Es mas facil de leer un ciclo **for** que un **while** a la hora de imprimir elementos. **while** necesita un iniciador para controlar las iteraciones. Manipular un archivo con **while** tambien es mas complicado en comparacion a **for**.

```python
# Diferencias al usar 'while' y 'for' para leer archivos:

file = open("sequence.txt", "r")
while True:
	line = file.readline()
	if not line:
		break
	print(line)
file.seek(0)

for line in file:
	print(line)
```

## Diferencias entre "is" e "=="

- **=** -> compara si el valor de dos variables es el mismo.
- **is** -> compara si dos variables ocupan el mismo espacio de memoria. Se puede corroborar con la funcion **id(*lista*)**.

Si dos listas comparten el mismo espacio de memoria, se alteran los valores de una cuando alteras los valores de la otra.

## Manejo de objetos:

- **lista.copy()** -> Asigna los valores de una lista a otra lista, sin solapar los espacios de memoria.
- **if isinstance(*lista*, list)** -> Compara la clase de un objeto.

- **in** -> Busca una variable dentro de un objeto iterable.
- **pass** -> Silencia un ciclo entero. 

## set():

Es una funcion que transforma una lista en un set. No contiene elementos repetidos, pero va a tener metodo diferentes a los de una lista. 

```python
lista1 = list(set(lista2))
## Donde lista 2 posee elementos repetidos. Lista 1 ya no tendra elementos repetidos.
```

## continue:

Cuando un ciclo llegue a **continue**, se salta el bloque y va a la accion siguiente.Se puede usar para imprimir suprimiendo cosas:

```python
for nucleotide in sequence:
	if nucleotide == "N"
		continue
	print(nucleotide, end="")

index = 0
while index < len (sequence):
	nucleotide = sequence(index)
```
## break:

Cuando un ciclo llegue a **break**, se rompe el ciclo y se continua con lo inmediato despues de el.

```python
for nucleotide in sequence:
	if nucleotide =="N":
		break
	print(nucleotide, end="")
```