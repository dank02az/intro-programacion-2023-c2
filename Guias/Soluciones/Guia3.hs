module Guia3 where

-- EJERCICIO 1::..

f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

-- EJERCICIO 2::..

absoluto :: Integer -> Integer
absoluto n | n<=0 = n*(-1)
           | n>=0 = n
           
absoluto' :: Float -> Float
absoluto' n  | n<=0 = n*(-1)
             | n>=0 = n
                       
           
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n m | absoluto m > absoluto n = absoluto m
                   | otherwise = absoluto n

maximo :: Integer -> Integer -> Integer
maximo n m | n > m = n
           | otherwise = m
           
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c  | maximo a b > c = maximo a b
               | maximo a c > b = maximo a c
               | maximo b c > a = maximo b c

               
algunoEs0 :: Integer -> Integer -> Bool
algunoEs0 n m = n * m == 0                                        

ambosSon0 :: Integer -> Integer -> Bool
ambosSon0 n m = n==0 && m==0


mismoIntervalo :: Integer -> Integer -> Integer
mismoIntervalo n m | n < 3 && m < 3 = 1
                   | (n > 3 && n <= 7) && (n > 3 && n <= 7) = 2
                   | n > 7 && m > 7  = 3

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe a b = mod a b == 0 

digitoUnidades :: Integer -> Integer 
digitoUnidades a = mod a 10 

digitoDecenas :: Integer -> Integer
digitoDecenas a = div (mod a 100) 10




-- EJERCICIO 3::..

estanRelacionados ::  Integer -> Integer -> Bool
estanRelacionados a b = a*a + a*b*k == 0
                      where k = (-1) * div a b 

--EJERCICIO 4::..

prodInt ::  (Int, Int) -> (Int,Int) -> (Int,Int)
prodInt a b = ( fst(a)*fst(b) , snd(a)*snd(b) )

prodIntAlt :: (Int,Int) -> (Int,Int) -> (Int,Int)
prodIntAlt (a,b) (c,d) = (a*c, b*d)


todoMenor :: (Int, Int) -> (Int, Int) -> Bool
todoMenor (x,y)(x2,y2) = x<x2 && y<y2

distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x1,y1)(x2,y2) = sqrt ( (x2-x1)^2 + (y2-y1)^2 )


sumarTerna :: (Int,Int,Int) -> (Int,Int,Int) -> (Int,Int,Int)
sumarTerna (x1,y1,z1) (x2,y2,z2) = (x1+x2, y1+y2, z1+z2)



soloMultiplosN :: Integer -> Integer -> Integer 
soloMultiplosN a n | mod a n == 0 = a
                   | otherwise = 0

sumarSoloMultiplos :: (Integer,Integer,Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n = soloMultiplosN a n + soloMultiplosN b n + soloMultiplosN c n 


posPrimerPar :: (Int,Int,Int) -> Integer 
posPrimerPar (a,b,c) | even a = 1
                     | not(even a) && even b = 2
                     | not(even a && even b) && even c = 3
                     | not(even a && even b && even c)  = 4
                     
crearPrimerPar :: a -> b -> (a,b)
crearPrimerPar a b  = (a,b) 

invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)


--EJERCICIO 5::..


f' :: Integer -> Integer
f' n | n <= 7 = n^2
     | otherwise = 2*n-1 

g' :: Integer -> Integer 
g' n | even n = div n 2
     | otherwise = 3*n+1
     

todoMenores :: (Integer, Integer, Integer) -> Bool
todoMenores (n1,n2,n3) = f' n1 > g' n1 && f' n2 > g' n2 && f' n3 > g' n3

--EJERCICIO 6::..

bisiesto ::  Integer -> Bool
bisiesto anio = (esMultiploDe anio 4 || esMultiploDe anio 100) && not(esMultiploDe anio 400)

--EJERCICIO 7::.. 


distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p0,p1,p2) (q0,q1,q2) = absoluto'(p0-q0) + absoluto'(p1-q1) + absoluto'(p2-q2)


--EJERCICIO 8::..

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = mod x 10 +  mod (div x 10) 10

comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b)  = 1
             | sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b)  = -1
             | sumaUltimosDosDigitos(a) == sumaUltimosDosDigitos(b) = 0
                    


sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna _ 0= 0
sumatoriaInterna i j = sumatoriaInterna (i-1) j + i^j

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble i j = sumatoriaDoble (j-1) i + sumatoriaInterna i j   
