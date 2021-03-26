Licenciatura en ciencias genomicas - Introduccion a Python.

Por Salvador Gonzalez Juarez.

# Sesión 7: Manejo de errores, importando módulos

## Errores en python:

Para el manejo de errores necesitamos "try, except, else y finally". Con esta estructura se detecta cualquier error en el codigo.

```python
try:
	# Bloque de codigo que queremos ejecutar.

except:
	# Bloque de codigo que se ejecuta en caso de ocurrir un error.
	
else:
	# Bloque de codigo que se ejecuta si el bloque de try se pudo ejecutar.
    
finally:
	# Bloque de codigo que se ejecuta si ocurre un error o no.

# Por ejemplo:

numero_1 = input("Ingrese el primer numero")
numero_2 = input("Ingrese el segundo numero")

try:
	suma = int(numero_1) + int(numero_2)
	print (suma)
	
except:
	print ("no se pudo hacer la suma")
	
finally:
	print ("gracias"")
```

## EAFP vs LBYL:

EAFP es utlizado por python.

```python
# EAFP:

lista = "araC"

try:
	lista.append("araB")
	
except:
	lista = lista + ", araB"
	lista = lista.split(",")
	
print(lista)

# LBYL:

lista = "araC"

if isinstance(lista, list):
	lista.append("araB")
	
else:
	lista = lista + ", araB"
	lista = lista.split(",")
	
print(lista)
```

## Importando modulos:

Para importar modulos necesitamos la palabra reservada **import**. Los imports siempre se deben de poner al principio del archivo, despues de los comentarios del modulo y los docstrings y antes de las variables globales o constantes del modulo.

Se deberan agrupar en el siguiente orden:
1. Standard library imports
2. Related third party imports
3. Local application/libraty specific imports

Separados por un salto de linea entra cada grupo. No se sugiere importar partes de la libreria solamente utilizando **from** y tampoco apodar a la función de una libreria.

Debe de ser utilizado de la siguiente forma:

```python
import random

for i in range (5):
	print(random.randint(1, 10), end = " ")
```

## Formas de importar nuestros módulos:

**Esto fue lo que hice en la clase:**

Primero instale **pip** para **python3**, con el siguiente comando:

```bash
sudo apt install python3-pip
```

Se pueden ver todos los paquetes que tengo instalados con el siguiente comando, llamado **pip**:

```bash
pip3 list
```

Posteriormente actualize la version de **pip** e instale **setuptools wheel**:

```bash
python3 -m pip install --upgrade pip

python3 -m pip install --user --upgrade setuptools wheel
```

Ademas instale **tree** para poder ver los directorios de una forma mas ordenada:

```bash
sudo apt install tree
```

A continuacion, modifique la estructura del directorio **lib**, de tal forma que tenga dentro un directorio llamado **curso**. Este directorio esta estructurado de la siguiente manera:

.
└───curso
    ├── python_class
    │     └── funciones.py
    └── setup.py



Donde **funciones.py** es el script donde estan las funciones que he creado y esta dentro de un subdirectorio llamado **python_class**. Por su parte, **setup.py** es un script que debe estar en la misma jerarquía que el directorio **python_class**, y debe tener el siguiente formato:

```python
import setuptools	
setuptools.setup(
      name='python_class',
      version='0.1',
      description='Functions from the python class',
      author='Salvador Gonzalez',
      author_email='salglzj@lcg.unam.mx',
      packages=["python_class"]
)
```

Despues ejecute el siguiente comando, con el objetivo de adicionar nuevos subdirectorios al directorio **curso**:

```bash
python3 setup.py sdist bdist_wheel

```
El directorio quedo de la siguiente manera:

.
└───curso
    ├── bdist.linux-x86_64
    │     └── lib
    │             └── python_class
    │                    └── funciones.py
    ├── dist
    │     ├── python_class-0.0.0-py3-none-any.whl
    │     └── python_class-0.0.0.tar.gz
    ├── python_class
    │     └── funciones.py
    ├── python_class.egg-info
    │     ├── dependency_links.txt
    │     ├── PKG-INFO
    │     ├── SOURCES.txt
    │     └── top_level.txt
    └── setup.py



Me enfoque en el subdirectorio **dist**, pues contiene dos archivos importantes: **python_class-0.0.0-py3-none-any.whl** y **python_class-0.0.0.tar.gz**. A continuación, ejecute el siguiente comando:

```bash
pip3 install python_class-0.0.0-py3-none-any.whl
```

A partir de ahora, puedo ver el paquete **python-class** al ejecutar el comando **pip3 list**, que vi anteriormente.

Finalmente puedo utilizar las funciones dentro del paquete en un script de python, de la siguiente forma:

```python
# Para importar las funciones de mi paquete:
from python_class import funciones

# Para poder ver las propiedades de cada función:
help(funciones)

# Haciendo uso de una funcion del paquete:
print(funciones.get_at_content(("ATCG"),2))

# >> 50.0
```
