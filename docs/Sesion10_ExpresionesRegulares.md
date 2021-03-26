Licenciatura en ciencias genomicas - Introduccion a Python.

Por Salvador Gonzalez Juarez.

# Sesion 10 - Expresiones regulares

Las expresiones regulares nos permiten encontrar ciertos **patrones** en cadenas de caracteres. La importancia de los patrones en la biologia reside en las secuencias, nombres, identificadores y coordenadas de las principales moleculas biologicas estudiadas.

Una **expresion regular** es un modelo (patron) con el que el motor de expresiones regulares intenta buscar. Esto funciona de forma similar al comando **grep**:

```bash
$ grep "araC" sequence.txt
```

Ejemplos de herramientas en linea:

 - regex101
 - regexr
 - regexper

## Elementos de una expresion regular

### Delimitadores / /

Todo lo que este dentro de las diagonales es el **patron a buscar**. Se va a buscar exactamente las literales de caracter que componen el patron. Una expresion regular va a hacer match en el primer patron que coincida. Sin embargo, podemos indicar que se haga una **busqueda global** para encontrar mas matches.

```python
/ATCG/ -> "TATCGC" # True
/ATCG/ -> "CACCGT" # False
/ACCG/ -> "CACCGT" # True
/ACCG/ -> "CACCGATACCGT" # True
```

### Alternacion |

Se coloca entre los patrones **alternativos**. Busca el primer patron o busca el siguiente patron. Pueden hacerse multiples alternaciones.

```python
/ATCG/ -> "TATCGC" # True
/ATCG/ -> "CACCGT" # False
/ATCG|ACCG/ -> "CACCGT" # True
/ATCG|ACCG/ -> "TATCGC" # True
```

### Alternacion y agrupamiento ( | )

Escribimos dentro del patron, un **grupo** de alternacion que es un subpatron y su alternativa, luego se continua con el patron.

```python
/ATCG/ -> "TATCGC" # True
/ATCG|ACCG/ -> "CACCGT" # True
/A(T|C)CG/ -> "CACCGT" # True
/A(T|C)CG/ -> "TATCGC" # True
/A(T|C)CG/ -> "TAGCGC" # False
/A(T|C)CG/ -> "TAACGC" # False
/A(A|T|C|G)CG/ -> "TATCGC" # True
```

### Clase de caracteres positivos [ ] 

Dentro del patron se coloca un **rango** de caracteres dentro de corchetes, sirve de igual forma que la alternacion, pero de forma mas simple. No se puede atrapar el caracter que coincidio, como sucede en el agrupamiento. Debemos tener en cuanta que **la clase de caracteres anula los caracteres especiales de una expresion regular**.

```python
/A(A|T|C|G)CG/ -> "TATCGC" # True	
/A[ATCG]CG/ -> "TATCGC" # True
/A[(T|C)]CG]/ -> "TATCGC" # True
/A[(T|C)]CG]/ -> "A(CGC" # True
/A[(T|C)]CG]/ -> "A|CGC)" # True
```

Se indica, de una lista definida, un rango que se peude considerar para armar el patron. El rango de caracteres va de acuerdo a los valores de cada caracter en **ASCII**.

### Cuantificadores {n , m} 

Se va a repetir las veces indicadas por el valor minimo de **n** y maximo de **m** dentro de las llaves, lo que haya en la unidad, es decir en la clase de caracteres, grupos o literales unicas. 

```python
/[ATCG]/ -> "TATCGC" # True
/[ATCG]{4}/ -> "TATCGC" # True
/[ATCG]{4,6}/ -> "TATCGC" # True	
/[ATCG]{4,}/ -> "TATCGC..." # True
```

El cuantificdaor **?** marca de 0 a 1 coincidencias. El cuantificador **\*** marca de 0 a mas veces. El cuantificador **+** marca de 1 a mas coincidencias.

```python
/A?TCG/ -> "ATCG" # True
/(A)?TCG/ -> "TTCG" # True
/[A]*TCG/ -> "ATCG" # True
/A*TCG/ -> "TTCG" # True
/(A)+TCG/ -> "ATCG" # True
/[A]+TCG/ -> "TTCG" # False
```

### Clase de caracteres negativos [^]

Indica que debe haber matches negativos con los caracteres dentro de la clase de caracteres.

Fuera de la clase de caracteres, el caracter especial **^** sirve para indicar que la cadena debe comenzar con el caracter que le sigue. Por su parte el caracter especial **$** indica que debe terminar con el caracter que va antes de el. 

### Modificador multilinea / /m

Se indica fuera de los de limitadores, y sirve para poder separar la cadena en lineas y hacer un buen uso de los caracteres **^** y **$**.

## Meta caracteres (12):

Caracteres con significado especial, incluye aquellos que vimos en la sección anterior:

- **( )** Capturar y Agrupacion.

- **[ ]** Coincide con cada caracter dentro de los corchetes.

- **expr{n,m}** Coincide exactamente con n o n,m ocurrencias de la expresion.

- **\*** Busca el caracter precedente 0 (cero) o mas veces. Es equivalente a {0,}.

- **?** Busca el caracter precedente 0 (cero) o mas veces. Es equivalente a {0,}.

- **+** Busca el caracter precedente 1 o mas veces. Es equivalente a {1,}.

- **.**  Coincide con cualquier caracter precedente excepto un caracter de nueva linea.

- **|** Alternacion.

- **^** Coincide con el principio de la entrada.

- **$** Coincide con el final de la entrada.

- **\\** Buscara coincidencias conforme a ciertas reglas (short codes: \w \s \b ...).

Entre mas explicita sea la expresion regular, mas eficiente se vuelve la busqueda.

## Creando una expresión regular

1. Iniciar con un codon ATG.
	. Seguido por cualquiera de las bases A, T, G o C, entre 30 hasta 1000 veces.	
3. Seguido de una cola poli-A de entre 5 a 10 bases al final de la secuencia.

**/^ATG[ATGC]{30,100}A{5,10}$/

Ahora podemos atrapar la secuencia que coincide en las iteraciones de la clase de carcteres de la siguiente forma:

**/^ATG([ATGC]{30,100})A{5,10}$/

## Regex en Python

Para utilizar las expresiones regulares en python es necesario importar la libreria **re**. Luego utlizamos el metodo **.search()** para iniciar la busqueda.

```python
import re

sequence = "ATGATCGTTTTGC"
result = re.search("ATCG", sequence)
	
print (result)
# <re.Match object; span=(3, 7), match='ATCG'>
```

El resultado de la busqueda incluye tambien algunos atributos, como la posicion (**.span()**), inicio incluyente (**.start()**) y final excluyente (**.end()**).

```python
import re

sequence = "ATGCTCGTTTTGC"
result = re.search("ATGC", sequence)
	
print (result)
# <re.Match object; span=(3, 7), match='ATCG'>

print (result.span())
# (3, 7)

print (result.start())	
# 3

print (result.end()
# 7
```

### Buscar todas las ocurrencias

El método **re.findall()** sirve para buscar de forma global el patron. Sin embargo se pierde la informacion de los atributos del resultado.

```python
import re

sequence = sequence = "ATGCTCGTTTATGCATGCTGC"

# findall vendría siendo el modificador "global"
result = re.findall("ATGC", sequence)

print (result)
# ['ATGC', 'ATGC', 'ATGC']
```

El modificador **re.IGNORECASE** sirve para ignorar la diferencia entre mayusculas y minusculas.

```python
import re

sequence = sequence = "ATGatgcCTCGTTTATGCATGCTGC"

# re.IGNORECASE vendría siendo el modificador i, ignore case
result = re.findall("ATGC", sequence, re.IGNORACASE)

print (result)
# ['atgc', 'ATGC', 'ATGC']
```

El método **.finditer()** sirve para mostrar los resultados con atributos para cada match en la secuencia.

```python
import re

sequence = sequence = "ATGatgcCTCGTTTATGCATGCTGC"
result = re.finditer("ATGC", sequence, re.IGNORECASE)

for ocurrence in result:
  print (ocurrence)
  print ("inicio:", ocurrence.start())
  print ("final:", ocurrence.end())

# <re.Match object; span=(3, 7), match='atgc'>
# inicio: 3
# final: 7
# <re.Match object; span=(14, 18), match='ATGC'>
# inicio: 14
# final: 18
# <re.Match object; span=(18, 22), match='ATGC'>
# inicio: 18
# final: 22
```

Una forma mas limpia de utilizar Regex es asignar el patron que bucamos a una variable. Esto se logra usando el metodo **.compile()**. Asi nos ahorramos escribir de nuevo el patron en busquedas posteriores en el programa.

```python
import re

regex = re.compile("GA[ATGC]{3}AC[ATGC]{2}AC")
sequence = "GAATGACATAC"
result = regex.search(sequence)

print (result)
# <re.Match object; span=(0, 11), match='GAATGACATAC'>

print (result.group())
# 'GAATGACATAC'
```

### Agrupamiento con Python

Utilizando el metodo **.groups()** podemos acceder a los grupos que hicieron match durante la busqueda.

```python
import re

regex = re.compile("GA([ATGC]{3})AC([ATGC]{2})AC")
sequence = "GAATGACATAC"
result = regex.search(sequence)

print (result)
# <re.Match object; span=(0, 11), match='GAATGACATAC'>

print (result.groups())
# ('ATG', 'AT')

print (result.group(0)) # (result.group())
# 'GAATGACATAC' 

print (result.group(1))
# 'ATG'

print (result.group(2))
# 'AT'
```

Ya que podemos acceder a los grupos del patron, podemos incluso usar los mismos metodos que muetran los atributos del resultado para encontrar la posicion, el inicio incluyente y el final excluyente.

```python
import re

regex = re.compile("GA([ATGC]{3})AC([ATGC]{2})AC")
sequence = "GAATGACATAC"
result = regex.search(sequence)

print (result.groups())
# ('ATG', 'AT')

print (result.group(1))
# 'ATG'

print (result.start(1))
# 2

print (result.end(1))
# 5

print (result.span(1))
# (2, 5)
```

### Separando una cadena con regex

Podemos recortar una cadena en fragmentos de nuestro patron utilizando el metodo **.split()**. Asi excluiremos todo aquello que no haga match en la busqueda.

```python
import re

regex = re.compile("[^ATGC]")
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
dna_splitted = regex.split(dna)

print (dna_splitted)
# ['ACT', 'GCAT', 'GCTACGT', 'ACGAT', 'CGA', 'TCG']
```

Finalmente, si lo que queremos es remover los caracteres que no hacen match, pero sin dividir la cadena como en el metodo anterior, utilizamos el metodo **.sub()**.

```python
import re

regex = re.compile(r"[^ATGC]")
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
new_dna = regex.sub('', dna)

print (new_dna)
# ACTGCATGCTACGTACGATCGATCG
```









