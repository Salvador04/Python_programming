Licenciatura en ciencias genomicas - Introduccion a Python.

Por Salvador Gonzalez Juarez.

# Sesion 6 - Funciones

Son bloques de codigo que son reutilizados al ser llamados. Ayudan a disminuir las lineas de codigo.

Ejemplos:

``` python
print() # Imprime a pantalla.
len() # Calcula la longitud de una cadena.
input() # Pide al usuario introducir una cadena.
```

## ¿Como definir una funcion?

La forma correcta para definir una funcion es la siguiente:

``` python
def hello_world():
	print("hello world")
hello_world()
# > hello world
```

## Parametro vs argumentos:

- **Parametro**: esta en la definicion de la funcion.
- **Argumento**: valor que recibe una funcion cuando es llamada.

```python
# La funcion tiene 1 parametro:
def hello_message(name):
	print(f"hello {name}!")
	
# Llamando a la funcion con un argumento:
hello_message("Emilio")
# > hello Emilio!
```

## Default parameters vs keyword arguments:

``` python
def hello_message(name, last_name):
	print(f"hello {name} {last_name}!")
	
# Utilizando funcion con keyword arguments
hello_message(name="Emilio", last_name="Peña")
# > hello Emilio Peña!

# Al usar keyword arguments, no importa el orden en el que fueron ingresados
hello_message(last_name"Peña", name="Emilio")
# > hello Emilio Peña

# Caso contrario a cuando no se utilizan, si importa el orden
hello_message("Peña", "Emilio")
# > hello Peña Emilio!

# DEFAULT PARAMETERS:

def hello_message(name="Alumno", last_name="UNAM")
	print(f"hello {name} {last_name}!")

hello_message()
# > hello Alumno U}NAM

hello_message("Emilio")
# > hello Emilio UNAM
```

## Return:

Debemos hacer uso explicito del **return** para poder manipular la variable a la que le aplicamos la funcion de forma correcta. 

``` python
def suma(number_1, number_2):
	number_1 + number_2
# Por default las funciones retornan None si no se le indica que retornar
print(suma(2,5))
# >None

def suma(number_1, number_2):
	resultado = number_1 + number_2
	return resultado
# Aqui indicamos que queremos retornar el valor de la operacion
print(suma(2,5))
# > 7
```

## Docstrings:

Es una propiedad de la funcion. Entreamos a ella atraves de **.__doc__**. El docstring debe de ir inmediatamente despues de nombrar la fucion.

``` python
def hello_world():
	'''
	Prints hello world string
	'''
	print("hello world")
	
print(hello_world.__doc__)
# > Prints hello world string

def suma(number_1, number_2):
	'''
	Retorna el resultado de la suma de dos numeros
	:param number_1: valor del numero 1
	:param number_2: valor del numero 2
	: return: int, valor de la resta de los valores
	'''
	resultado = number_1 + number_2
	return resultado
	
print(suma.__doc__)
```
