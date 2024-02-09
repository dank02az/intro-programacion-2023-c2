---
tags: [intro-resumen]
title: teorica6 validacion y varificacion
created: '2023-12-06T12:58:27.430Z'
modified: '2024-01-10T00:35:46.427Z'
---

_teorica6_ validacion y varificacion

# Validacion y Verificacion 

Un sofware tiene __calidad__ cuando <u>_cumple con la especificacion y con su proposito_</u>.
La __calidad de sofware__ no se puede inyectar al final del proceso de desarrollo si no que acompaña todo el desarrollo.

__Validacion y Verificacion__ es un proceso por el cual se __garantiza la calidad__ de software.



* ### Validacion
El software deberia hacer lo que el __usuario__ requiere de el

* ### Verificacion
El sofware deberia cumplir con la __especificacion__


### Nociones Basicas

* __Falla__: manifestacion de un *Defecto*
* __Defecto__: desperfecto en algun componente del sistema
* __Bug__ : Equivovacion humana, puede producir ninguno o varios __Defectos__, que manisfestaran o no __Fallas__.



### Proceso de V&V (Validacion y Verificacion)

Se deberia aplicar a cada instacion del desarrollo

* #### Objetivo:
     - Descubrir __defectos__ en el sistema 
     - Asegurar que el software respete su __especificacion__.
     - Determinar si safisface las __necesidades de sus usuarios__.
     - Garantiza __calidad de software__. 
* #### Metas:     
     - __NO garantiza__ que este libre de Defectos
     - Determina si es confiable para su uso.


#
# Testing

### ¿Que es hacer testing?

Es un proceso mediante...
* Se verifica que se cumpla con la **especificacion**
* Identificar diferencias entre el comportamiento __real__ y el comportamiento __esperado__ 

__Objetivo__: encontrar defectos en el software

__Importante__: El testing puede demostrar la presencia de errores nunca su ausencia

<br>

Ejemplo de TESTING :

```haskell
   sumar :: Int -> Int -> Int
   sumar a b = a - b
``` 


- Comportamiento Esperado : se espera que el programa sume valores.
- Comportamiento Real : el programa resta en lugar de sumar.

OBS: si el __Comportamiento Real = Comportamiento Esperado__ el testCase no encontro errores.

#TestCase: 
  | entrada | valor de salida | valor esperado |
  |-|-|-|
  |a=1 ,b=2| -1 | 3 |



### Tipos de testing

  * <u> __Test de Caja Negra__ </u>: 
  Los casos de test se generan analizando la **especificación** sin considerar la implementación.

  *En la materia se usa Test HUnit (Haskell) para hacer Caja Negra*

  * <u> __Test de Caja Blanca__ </u>: [✍](@note/teorica3 Caja Blanca.md)
  Los casos de test se generan analizando la **implementación** para determinar los casos de test.

  *En la materia se usa CFG (Pyhton) para hacer Caja Blanca*





