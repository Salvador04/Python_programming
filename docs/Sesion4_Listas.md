Licenciatura en ciencias genomicas - Introduccion a Python.

Por Salvador Gonzalez Juarez.

#Sesion 4 - Listas

**Una lista es una estructura que permite guardar cualquier tipo de dato.**

## Moverse e imprimir la lista:

Los siguientes metodos y funciones son muy utiles para moverse dentro de una lista, y para imprimir ciertos elementos de ella:

```python
lista[indice] # Acceder a los elementos de la lista a traves de su indice.

lista.split(",") # Utilizar un string como lista.

print(lista) # Imprimir todo el contenido se pone enre parentesis el nombre de la lista.

print(lista[inicial : final]) # Imprimir un rango. Es importante que el indice final ya no pertenezca al rango.

print(len(lista)) # Imprime la longitud de la lista. No funciona para listas anidadas.

print(lista[-1]) # Imprime el ultimo elemento de una lista.
```

## Agregar un elemento a la lista:

Los siguientes metodos nos ayudan a adicionar elementos en ciertas partes de una lista:

```python
lista.append(elemento) # Agrega un elemento al final de la lista.

lista.insert(indice , elemento) # Agrega un elemento en cualquier posicion de la lista.

lista.append(nueva_lista) # Para agrefar una nueva lista a la lista original (lista anidada).

lista + nueva_lista # Concatenar dos listas.

lista.extend(nueva_lista) # Agregar los elementos de una nueva lista a la lista original.
```

## Eliminar un elemento de la lista:

Los siguientes metodos son empleados para eliminar un elemento de la lista:

```python
lista.remove(elemento) # Eliminar un elemento por su valor.

lista.pop(indice) # Eliminar un elemento por su indice.
```

## Modificar el orden de los elementos de una lista:

Podemos utilizar estos metodos para modificar el orden de los elementos que estan dentro de una lista:

```python
lista.sort() # Ordena alfabeticamente los elementos de la lista.

lista.reverse() #  Invertir los elementos de la lista.
```

# Loops

Son utilizados para ejecutar un bloque de codigo multiples veces. Se ejecutan mientras una condicion sea verdadera. Pueden ser utilizados para manejar listas.

##Tipos de loop: for

El **for** nos ayuda a movernos a traves de una lista, de las siguientes maneras:

```python
# Identacion para imprimir toda la lista:
for lista_name in lista:
	print(lista_name)

# Leer un archivo con ciclos:
file = open("archivo.txt")
for line in file:
	print (line)

# Imprimir un rango de la lista (es importante que el indice final ya no pertenezca al rango):
for step in range (inicial : final):
	print (step)

# Imprimir con un rango que comienza en el inicio de la lista (es importante que el indice final ya no pertenezca al rango):
for step in range (final):
	print(step)

# Imprimir de una forma mas especifica (es importante que el indice final ya no pertenezca al rango):
for step in range (inicial, final, salto)
	print(step)
# Ejemplo: Imprimir una cadena crecsiente:
for aa in range (3, len(lista), +1)
print(lista[:aa])
```
