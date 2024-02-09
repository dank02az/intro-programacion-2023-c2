---
tags: [intro-resumen]
title: teorica5 Polimorfismo
created: '2023-12-06T12:31:46.447Z'
modified: '2024-01-04T00:37:23.118Z'
---

_teorica5_ Polimorfismo

# Polimorfismo

Se llama **polimorfismo** a una funcion que se le puede aplicar __distintos tipos de datos__.

Ejemplo de funcion polimorfica, es la **funcion identidad**

```haskell 

-- funcion identidad
identidad :: t -> t
identidad a = a

-- con polimorfismo
suma :: t -> t -> t
suma a b = a + b

-- sin polimorfismo 
resta :: Int -> Int -> Int
resta a b = a - b
```
