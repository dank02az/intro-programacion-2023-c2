# Preguntas para Coloquio

__<u>pregunta 1</u>__:
¿Qué diferencia hay entre testing de caja blanca y de caja negra? 

- <u>__respuesta 1__</u>:<br>
  - __Caja Blanca__ se hace sobre la __implementacion__, sin conocer la especificacion.<br>
*En la materia se usa CFG para hacer caja Blanca.<br>
  - __Caja Negra__ se hace sobre la __especificacion__, sin conocer la implementacion.<br>
*En la materia se hace Caja Negra con HUnit en Haskell.

#
__pregunta 2__:
¿Qué diferencia hay entre una 6-tupla y una lista de 6 elementos en Haskell?


- <u>__respuesta 2__</u>:<br>
En Haskell; 
  - Las __6-uplas__ pueden tener __diferente tipo de Dato__.<br>
  - Una __lista__ de 6 elementos siempre tiene el __mismo tipo de Dato_.

#
__pregunta 3__:
¿Qué es un estado de un programa en los lenguajes imperativos? ¿Qué relación hay entre una especificación y un programa?

- <u>__respuesta 3__</u>:
  - Un __estado__ es un valor de una variable en __un punto de la ejecucion__ de un programa.<br>
  - Una __especificacion__ describe __cual es problema__ y que __propiedades__ debe tener su posibles soluciones.<br>
  - Un __programa__ es la implementacion de una especificacion en un lenguaje de programacion.<br>
  - Una especificacion ayuda a __construir__, a __entender mejor__ y a __encontrar errores__ en un programa.

#

__pregunta 4__:
¿Qué conclusiones sacás de este escenario: tengo 100% de cubrimiento, con 1 solo caso de TEST y dio OK?

- <u>__respuesta 4__</u>:<br>
Esto nos dice que el __caso de Test__ tiene el comportamiento esperado, que se cubrieron todas los nodos, caminos, instancias etc. EN general es un buen caso de test.
Pero esto, no nos dice que el programa esta libre de errores, simplemente el Caso de test no los encontro.
