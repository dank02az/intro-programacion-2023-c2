
# Programacion Funcional

Un programa en un lenguaje funcinal se trata de ***un conjunto de ecuaciones orientadas*** que definen una o mas funciones.

~~_La programacion funcional pertenece a un paradigma declarativo_~~

### Como funciona?

Se van descomoponiendo ***Expresiones Complejas*** reducibles en ***Expresiones Atomicas***, que son irreducibles y solo se pueden evaluar en codiciones basicas: __True__ o __False__.

1.  ***Expresiones Atomicas*** : son expresiones irreducibles que solo se evaluan como True o False.
ejemplo :  (1 > 2) , (True == False)

### Transparencia Referencial

Es una propiedad muy importante, la cual nos dice que el valor de las ***expresiones*** representa siempre **el mismo valor** en cualquier lugar de un programa.


#

### Tipos de Datos y Clases de Tipos

1. <u>__Tipos de Datos__</U>: son conjuntos de valores a los cuales se les puede aplicar diversas operaciones
   * Ejemplos: en Haskell 

     |Tipo|Operaciones|
     |-|-|
     |Int|{ +, -, div }|
     |Float|{ +, -, / }|
     |Char|{ ++ , tail, head }|   

2. <u>__Clases de Tipos__</u>: son conjuntos de Tipos de Datos 
   * Ejemplos: en Haskell

     |Clase| Tipos|operaciones|
     |-|-|-|
     |Fractional|{ Float, Double, ◦..}|{(/),◦..}
     |Floating|{ Int,Float,◦.. }|{sqrt, sin, cos, tan,◦..}|
     |Eq|{ Bool, Int, Integer, Float, Double,◦.. }|{ (==), (/=)}|
     |Num|{ Int, Integer, Float, Double,◦.. }| {(+), (∗), abs,◦.. }|

