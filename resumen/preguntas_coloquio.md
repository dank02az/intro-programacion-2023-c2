# Preguntas para Coloquio

¿Qué diferencia hay entre testing de caja blanca y de caja negra? 

  - __Caja Blanca__ se hace sobre la __implementacion__, sin conocer la especificacion.<br>
*En la materia se usa CFG para hacer caja Blanca.<br>
  - __Caja Negra__ se hace sobre la __especificacion__, sin conocer la implementacion.<br>
*En la materia se hace Caja Negra con HUnit en Haskell.

#

¿Qué diferencia hay entre una 6-tupla y una lista de 6 elementos en Haskell?

En Haskell; 
  - Las __6-uplas__ pueden tener __diferente tipo de Dato__.<br>
  - Una __lista__ de 6 elementos siempre tiene el __mismo tipo de Dato_.

#

¿Qué es un estado de un programa en los lenguajes imperativos? ¿Qué relación hay entre una especificación y un programa?


  - Un __estado__ es un valor de una variable en __un punto de la ejecucion__ de un programa.<br>
  - Una __especificacion__ describe __cual es problema__ y que __propiedades__ debe tener su posibles soluciones.<br>
  - Un __programa__ es la implementacion de una especificacion en un lenguaje de programacion.<br>
  - Una especificacion ayuda a __construir__, a __entender mejor__ y a __encontrar errores__ en un programa.

#

¿Qué conclusiones sacás de este escenario: tengo __100% de cubrimiento__ , con __1 solo caso de TEST__ y dio OK?

- Esto nos dice que los casos de test tienen el comportamiento esperado, que se cubrieron todas los nodos, caminos, instancias etc. En general esto nos dice la suficiencia y eficacia de la prueba realizadas fueron buenas.
Pero esto, no nos dice que el programa esta libre de errores, simplemente el TestSuite no los encontro.




__Ejemplo (con dos Caso de Test)__

### menorQue1 

```haskell
   menorQue1 :: Integer -> [Char]
   menorQue1 n | n < 1 = "A"
               | otherwise = "B"
```

<p align="center">
  <img src="/resumen/ejemplo_cfg.svg" width="292">
</p>



TestSuite: # 100% de cobertura (cubre todos los nodos y arcos)

  | entrada | salida |
  |--|--| 
  | n = 0 | "A" |
  | n = 2 | "B" |  

Pero no encuntra el bug o error:

TestSuite:  # BUG
  |entrada| salida|
  |--|--|
  | n = 1 | indefinido |


<hr>

__Ejemplo (con un Caso de TEST, el la pregunta)__


### menorQue1 

```haskell
   menorQue1 :: Integer -> Bool
   menorQue1 n = n < 1  
```




<p align="center">
  <img src="/resumen/ejemplo_cfg2.svg" width="192">
</p>




TestSuite: # 100% de cobertura (con un solo caso de Test)

  | entrada | salida |
  |--|--| 
  | n = 0  | True | 

Pero no encuentra el bug o error:

TestSuite:  # BUG
  |entrada| salida|
  |--|--|
  | n = 1 | indefinido |


#

## Ejemplos de Sub-especificar y Sobre-especificar:


### Sub-especificar
<code> 
<b>problema</b> elSiguienteN (<b>n</b>:<i>int</i>): <b>res</b>:<i>int</i> {
      <b>requiere</b>: True
      <b>asegura</b>: res > n 
}
</code>

<br>


Me piden el siguiente a __n__, pero la especificacion me dice que la solucion es  cualquier numero mayor que __n__ pues _"res > n"_, dejando ambigua y poco clara la solucion, pues __el conjunto de salida es muy grande__, osea el __asegura es muy permisivo__. 

--------------------------------------------------------------------------------------------

### Sobre-especificar
<code> 
<b>problema</b> mayorQueN (<b>n</b>:<i>int</i>): <b>res</b>:<i>int</i> {
      <b>requiere</b>: True
      <b>asegura</b>: res = n+1
}
</code>

<br>



Me piden un numero mayor a __n__, pero la especificacion me restringe la solucion solo al siguiente pues _"res = n+1"_, Pero la solucion podria ser mas grande e incluir (n+1,n+2...n+m) a todos los mayores que __n__.
Entonces al ser el __asegura muy restrictivo se pierden soluciones__.


