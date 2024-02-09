---
tags: [intro-resumen]
title: teorica7 Programacion Imperativa
created: '2023-12-07T11:34:15.487Z'
modified: '2024-01-04T00:45:24.705Z'
---

_teorica7_ Programacion Imperativa

# Programacion Imperativa

* Los programas no necesariamente son funciones, ahora pueden devolver mas de un valor
* Pueden cambiar de __estado__
  * Perdida de __transparencia Referencial__
    * Hay __variables__, las cuales pueden mutar
* Las funciones no pertenecen a un **tipo de dato**

## Transformacion de Estados

Llamamos __estados__ de un programa a los valores de todas las variables en su punto de ejecucion.
Entonces vemos a la ejecuccion de un programa como una __sucession de estados__.

#### Pasaje de argumentos:

* <u>__Pasaje por valor__</u>: crea un copia local de la variable  __dentro de la funcion__.

* <u>__Pasaje por referencia__</u>: se maneja directamente la variable, los cambios realizados adentro de la funcion **afectaran tambien afuera**.

