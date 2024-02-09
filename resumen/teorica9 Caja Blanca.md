---
attachments: [Captura desde 2023-12-05 12-07-50.png, CFG.svg, CFG2.svg]
tags: [intro, intro-resumen]
title: teorica9 Caja Blanca
created: '2023-12-05T14:13:09.102Z'
modified: '2023-12-14T15:08:46.992Z'
---

_teorica9_ Caja Blanca

# Test de Caja Blanca 

Se realiza sobre la **implementacion**, y sin necesidad de conocer la **especificacion**.
Se usa con el **CFG** para obtener __testCases__.

### CFG (Control Flow Graph)

<p align="center">
  <img src="@attachment/CFG2.svg" width="192">
</p>


### Criterio de Adecuación: 

Un criterio de adecuación de test es un predicado que toma un valor
de verdad para una tupla <programa, test suite>


Como sabemos si un **testSuite es Bueno**?
Cada nodo (sentencia) en el CFG debe ser ejecutado **al menos una vez** por algún test case.


<p style="display:none" align="center"><img src="@attachment/Captura desde 2023-12-05 12-07-50.png" min-width="100%"/></p>


### Resumen de Criterios de Adecuacion

* <u>**Sentencias**</u>: cubrir todas los nodos del CFG.
* <u>**Arcos**</u>: cubrir todos los arcos del CFG.
* <u>**Deciciones**</u> :Por cada if, while, for, etc.., la guarda fue evaluada a True y a False

* <u>**Condiciones Basicas**</u>: Por cada componente basico de una guarda, este fue evaluado a verdadero o ya falso.

* <u>**Caminos**</u>: cubrir todos los caminos del CFG. Como no esta acotado o es muy grande, se usa muy poco en la practica.



# Tipos Abstractos de Datos:

Un TAD es un modelo que **define valores** y las **operaciones** que se pueden realizar sobre ellos.

Se denomina **abstracto** ya que la intencion es que quien lo utiliza , no necesita conocer los detalles de la representacion interna o bien el como estan implementados sus operaciones.



