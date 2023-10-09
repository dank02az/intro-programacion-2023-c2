module Otras where

import Guia3
import Guia5
import Guia4


primerosKPrimos :: Integer -> [Integer]
primerosKPrimos 0 = []
primerosKPrimos k = (nEsimoPrimo k) : primerosKPrimos (k-1)


sumaDeKPrimos :: Integer -> Integer -> Bool
sumaDeKPrimos n p   | n > p = False
                    | sumarTerminos (primerosKPrimos n) == p = True
                    | otherwise = sumaDeKPrimos (n+1) p


esSumaInicialDeKPrimos :: Integer -> Bool
esSumaInicialDeKPrimos n = sumaDeKPrimos 1 n


productoTerminos :: [Integer] -> Integer
productoTerminos [] = 1
productoTerminos (x:xs) = productoTerminos xs * x

esDescomposicion :: [Integer] -> Integer -> Bool
esDescomposicion l n = productoTerminos l == n



pertenece' :: (Eq t) => t -> [t] -> Bool
pertenece' _ [] = False 
pertenece' e (x:xs) | e == x = True
                    | otherwise = pertenece' e xs


combinatorio :: Integer -> Integer -> Integer
combinatorio n k = div (factorial n) ( (factorial k) * factorial (n-k))



divisoresDe :: Integer -> [Integer]
divisoresDe n = divisoresDesde n 1 

divisoresDesde :: Integer -> Integer -> [Integer]
divisoresDesde n k | k > n = []
                   | k<=n && mod n k == 0 = (-k):k : divisoresDesde n (k+1)
                   | otherwise = divisoresDesde n (k+1)  
  
x :: (Num t) => t -> t -> t
x a b = a * b


porcentaje :: Integer -> Integer -> Float
porcentaje n m = fromInteger (m * n) / fromInteger 100



 




