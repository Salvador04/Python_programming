Licenciatura en ciencias genomicas - Introduccion a Python.

Por Salvador Gonzalez Juarez.

# Sesion 11 - Introduccion a Programacion Orientada a Objetos

Representar cualquier objeto real a base de codigo. Cada objeto tiene clases y metodos. En python, todo lo que declaramos es en forma de objeto.

## Abstraccion: 

Las clases ya tienen sus atributos y metodos definidos. Las **instancias** de una clase, es cuando se le da valor a los atributos de las clases. Este proceso es conocido como **instanciar**. Para crear una clase en python debemos definirla de la siguiente forma.

```python
class Gene:
	# Atributos de la clase
	
# Instanciando un objeto y guardando la referencia en "gene"
gene = Gene(# Valores a instanciar)
```

## Construyendo un gen:

Para construir una clase con los atributos de un gen, podemos implementar el siguiente codigo.

```python
# Se debe utilizar CamelCase y usar "object":
class Gene(object):
	def __init__(self, name, sequence):
		'''
		Documentacion
		:param name:
		:param sequence:
		'''
		self.name = name
		self.sequence = sequence
		
# Guardar en una variable:
gene = Gene("araC", "ATCG")
gene.name = "araJ"
print(gene.name)
# >> araJ

# Forma no idonea de agregar nuevos atributos a la clase
gene.start_position = 1000
```

Podemos instanciar valores por default de los atributos de la clase.

```python
class Gene(object):
	def __init__(self, name, sequence, start_position = 0, end_position = 0):
		'''
		Documentacion
		:param name:
		:param sequence:
		'''
		self.name = name
		self.sequence = sequence
		self.start_position
		self.end_position
```

Podemos agregar metodos a la clase recien creada, este proceso se conoce como **encapsulamiento**.

```python
class Gene(object):
	def __init__(self, name, sequence, start_position, end_position):
		'''
		Documentacion
		:param name:
		:param sequence:
		:param start_position:
		:param end_position:
		'''
		self.name = name
		self.sequence = sequence
		self.start_position
		self.end_position
		
	def get_gc_content(self):
		'''
		Documentacion
		:return:
		'''
		gc_content = ((self.sequence.count("g") + self.sequence.count("c")) / len(self.sequence)) *100
		return gc_content
		
gene = Gene("araC", "ATCG", 1000, 1300)
print(gene.get_gc_content())
```

Podemos poner condicionales que evitan la creacion de la clase en caso de no ser cumplidas. Posteriormente podemos manejar esas **excepciones**.

```python
class Gene(object):
	def __init__(self, name, sequence, start_position, end_position):
		'''
		Documentacion
		:param name:
		:param sequence:
		:param start_position:
		:param end_position:
		'''
		self.name = name
		self.sequence = sequence
		
		if start_position < 0:
			raise Exception("Start position less than 0")
		self.start_position
		
		if end_position_ <= start_position:
			raise Exception("End position less than Start position")
		self.end_position
		
	def get_gc_content(self):
		'''
		Documentacion
		:return:
		'''
		gc_content = ((self.sequence.count("g") + self.sequence.count("c")) / len(self.sequence)) *100
		return gc_content
		
gene = Gene("araC", "ATCG", -1, 1300)
print(gene.get_gc_content())
```

Podemos usar un metodo para hacer la validacion de las condicionales:


```python
class Gene(object):
	def __init__(self, name, sequence, start_position, end_position):
		'''
		Documentacion
		:param name:
		:param sequence:
		:param start_position:
		:param end_position:
		'''
		self.name = name
		self.sequence = sequence
		self.set_start_position(start_position)
		self.set_end_position(end_position)
	
	def get_gc_content(self):
		'''
		Documentacion
		:return:
		'''
		gc_content = ((self.sequence.count("g") + self.sequence.count("c")) / len(self.sequence)) *100
		return gc_content
		
	# Aqui los metodos se encargan de asignar los valores de las clases:
		
	def set_start_position(self, start_position):
		if start_position < 0:
			raise Exception("Start position less than 0")
		else:
			self.start_position = start_position
			
	def set_end_position(self, end_position):
		if end_position_ <= start_position:
			raise Exception("End position less than Start position")
		else:
			self.end_position = end_position

		
gene = Gene("araC", "ATCG", -1, 1300)
print(gene.get_gc_content())
```



