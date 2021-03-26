Licenciatura en ciencias genomicas - Introduccion a Python

Por Salvador Gonzalez Juarez

#Sesion 2 - Python

Primero repasamos unos cuantos comandos ejecutables de la terminal:

- **cd**: Cambia a otra carpeta de trabajo.
- **pwd**: Muestra el nombre de la carpeta en la que nos encontramos.
- **ls**: Lista los contenidos de una carpeta, sean estos archivos o sub carpetas.
- **mkdir**: Crea directorios (carpetas).
- **rmdir**: Elimina directorios (carpetas) vacias.
- **rm -r**: Elimina directorios (carpetas) llenas.

##Buenas practicas de desarrollo de software:

###Metodologia para resolver un problema:

- **Requisitos**: 
No debemos comenzar a codificar sin saber lo que necesitamos para solucionar el problema, y para ello es necesario conocer el problema. Por lo tanto, se debe identificar los objetivos, los resultados que esperamos, etc.

- **Analisis y diseño**:
Consiste en la creación del algoritmo con el que esperamos resolver el problema. Ademas, podemos probar la efectividad del algoritmo con ejemplos empleando un pseudocodigo.

- **Codificacion**:
Se debe elegir un lenguaje de programacion y utilizar su gramatica y sintaxis para representar el algoritmo, una vez que esta listo.

- **Prueba**:
Se comprueba que el programa devuelve los resultados esperados, haciendo uso de diferentes pruebas que representan instancias del problema.

###Dividir los desarrollos en fases:

Nos permitira marcarnos objetivos en periodos cortos e ir mostrando los resultados.

###Estandarizar las reglas del desarrollo:

La forma de llamar y definir las funciones, las variables, el nombre de los ficheros, atributos, etc. forman parte de las reglas para codificar. 

###Modularizar los desarrollos:

No repetir codigo, preferiblemente emplear funciones o estructuras en bucle.

###Documentar el codigo:

Facilita las modificaciones y el mantenimiento del programa. Un encabezado del programa que describa la funcionalidad, dependencias, datos de entrada y las salidas etc. es indispensable.

- **Name**: Nombre del programa.
- **Version**: Version del progrma.
- **Autor**: Nombre del programador(es) que desarrollo el programa.
- **Description**: Breve descripción de lo que realiza el programa.
- **Category**: Palabra clave de la funcion principal del programa.
- **Usage**: Tipo de problemas para los que puede servir el problema.
- **Arguments**: Descripcion de cada uno de los comandos que puede realizar el usuario.
- **Used**: Descripcion de las variables y funciones utilizadas, ademas de su utilidad. 

##Tipos de datos:

- **Str(ing)**: Cadena de caracteres alfanumericos.
- **Int(eger)**: Numeros enteros con o sin signo.
- **Float**: Numeros decimales.
- **Boolean**: True (verdadero) o False (falso).

##Algunas funciones y metodos de Python:

Cada tipo de dato tiene sus propios métodos y funciones a las que pueden ser sometidos. 

```python
type (Variable) # Nos indica el tipo de dato que posee una variable.

Variable[valor1 : valor2] # Imprime una porcion de una cadena correspondientes a los valores dentro de los corchetes.

Variable.count(caracter): # Imprime el numero de veces que se repite un caracter dentro de una cadena.

len(Variable) # Imprime la longitud en caracteres de una cadena.

Variable.capitalize() # Toma el primer caracter de la cadena y lo convierte en mayuscula.

Variable.replace('caracter1' , 'caracter2') # Reemplaza todos los caracteres del indicado por otro caracter indicado, en una cadena.

Variable.upper() # Convierte todos los caracteres de una cadena en mayusculas.

Variable[::-1] # Invierte el orden de los caracteres en un vector.

Variable.find('caracter') # Devuelve la posicion en caracteres de un caracter indicado.
```

