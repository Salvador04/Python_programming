Licenciatura en ciencias genomicas - Introduccion a Python.

Por Salvador Gonzalez Juarez.

# Sesion 1 - Introduccion a Unix

## ¿Que es Unix y para que sirve?

Es un sistema operativo el cual controla los recursos de una computadora y los asigna entre los usuarios. Unix permite a los usuarios correr sus programas y controla los dispositivos de periféricos conectados a la máquina. [1]

## ¿Por que es necesario conocer y saber manejar Unix?

Unix posee características que lo hacen un sistema muy poderoso. Por ejemplo, tiene la capacidad de simular multiprocesamiento y procesamiento no interactivo, ya que se trata de un sistrema operativo multiusuario. Tambien ofrece facilidades para la creacion de programas y diseños de software. Ademas, emplea un sistema jerarquico de archivos con facilidades de proteccion de archivos, cuentas y procesos. [1]

## ¿Que es la estructura de directorios?

La estructura de directorios de Unix esta basado en un modelo arborescente y recursivo, en el cual los nodos pueden ser tanto archivos como directorios, y estos ultimos pueden contener a su vez directorios o subdirectorios. El nivel mas alto del sistema de directorios es / o directorio raiz. Todos los demas directorios estan bajo el directorio raiz. [1]

## ¿Que son las rutas absolutas y relativas?

Una ruta absoluta se basa en la raíz del arbol de Linux. Toda ruta absoluta empieza por /. Las rutas relativas dependen del directorio actual en el que se encuentra el usuario. [2]

## ¿Que son los directorios?

Un directorio es una agrupacion de archivos de datos, atendiendo a su contenido, a su proposito o a cualquier criterio que decida el usuario. Sirven para organizar mejor los archivos en un medio de almacenamiento como un disco duro, un pendrive, un CD, etc. [3]

## Ejercicios de la clase

Las opciones del comando son:

| Comando                 | Funcion                                                      |
| :---------------------- | :----------------------------------------------------------- |
| clear                   | Limpia la pantalla.                                          |
| man                     | Imprime el manual de un comando.                             |
| q                       | Salir del manual.                                            |
| ls                      | Enlista lo que hay dentro del usuario.                       |
| ls -l                   | Enlista con mas detalles (formato largo).                    |
| ls -lt                  | Enlista los archivos por fecha.                              |
| ls -a                   | Imprime todos los archivos y directorios dentro de una carpeta. |
| ls -F                   | Te dice cuales son archivos en un directorio.                |
| ls *                    | Enlista con filtro de inicio de letra.                       |
| ls ?                    | Filtro de cualquier letra en una posicion.                   |
| ls [ ]                  | Filtro de opciones en una posicion.                          |
| pwd                     | Indica la ubicacion dentro del servidor.                     |
| ctrl c                  | Mata la ejecucion del comando.                               |
| cat                     | Abrir el contenido de un archivo.                            |
| cd                      | Vuelve al directorio home.                                   |
| cd /home/carpeta        | Entrar a una carpeta del servidor.                           |
| cd . , cd .. , cd ../.. | Retornar a los directorios anteriores.                       |
| less                    | Abrir el contenido de un archivo por paginacion.             |
| history                 | Historial de todos los comandos usados en la sesion.         |
| ! "linea de codigo"     | Repetir el comando.                                          |
| head                    | Imprime el encabezado de un archivo.                         |
| head -n                 | Imprime la lineas iniciales de un archivo de forma personalizada. |
| tail                    | Imprime el final del archivo.                                |
| tail -n                 | Imprime las lineas finales de un archivo de forma personalizada. |

## Referencias:

1. Menéndez-Barzanallana, R. (19/03/2000). Sistemas operativos UNIX. Recuperado de: https://www.um.es/docencia/barzana/DIVULGACION/INFORMATICA/Unix01.html
2. Pons, N. (2019). Linux Principios básicos de uso del sistema. Recuperado de: https://www.ediciones-eni.com/open/mediabook.aspxidR=5ece86aff93ac988d3040a5c8161611e
3. Alegsa, L. (17/05/2018). Definición de Directorio (informática). DICCIONARIO DE INFORMÁTICA Y TECNOLOGÍA de http://www.alegsa.com.ar/Dic/directorio.php

