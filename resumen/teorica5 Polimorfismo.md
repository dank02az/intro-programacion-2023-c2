
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
