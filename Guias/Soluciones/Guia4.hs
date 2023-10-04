module Guia4 where

fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2)


parteEntera :: Float -> Integer
parteEntera n |  0 <= n && n < 1 = 0 
              | -1 <= n && n < 0 = -1
              | n>=1  = parteEntera(n-1) + 1
              | n<=(-1) = parteEntera(n+1) - 1


esDivisible :: Integer -> Integer -> Bool
esDivisible 0 m = True
esDivisible n 1 = True
esDivisible n m | n < 0 = False
                | otherwise = esDivisible (n-m) m




sumaImpares :: Integer -> Integer 
sumaImpares 1 = 1
sumaImpares n = nesimoPar + sumaImpares(n-1)
              where nesimoPar = 2*n-1


medioFactorial :: Integer -> Integer
medioFactorial 0 = 1
medioFactorial 1 = 1
medioFactorial n = medioFactorial(n-2) * n


sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = sumaDigitos(div n 10)  + ultimoDigito
              where ultimoDigito = mod n 10
                    




todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True 
                      | otherwise =  (unidades == decenas) == todosDigitosIguales(div n 10)
                      where unidades = mod n 10
                            decenas = mod (div n 10) 10
                      

 
cantidadDigitos :: Integer -> Integer
cantidadDigitos n | n < 10 = 1 
cantidadDigitos n | otherwise = cantidadDigitos(div n 10) + 1

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10 ^(cantidadDigitos (n)-i ))) 10






primerosKDigitos :: Integer -> Integer -> Integer
primerosKDigitos n k = div n (10 ^(cantidadDigitos (n)-k )) 

ultimosKDigitos:: Integer -> Integer -> Integer
ultimosKDigitos n k = mod n (10^k)


espejarNumero :: Integer -> Integer
espejarNumero n | n < 10 = n
                | otherwise = espejarNumero(div n 10) + mod n 10 * (10^(cantidadDigitos(n)-1 ))
                
               

quitarPrimeryUltimoDigito :: Integer -> Integer
quitarPrimeryUltimoDigito n = div (n - (primerDigito*10^(cantidadDigitos(n)-1) )) 10 
                            where primerDigito = iesimoDigito n 1

                            
esCapicua :: Integer -> Bool
esCapicua n | n < 10 = True
esCapicua n | otherwise = (ultimoDigito == primerDigito) == esCapicua( quitarPrimeryUltimoDigito(n) ) 
            where primerDigito = iesimoDigito n 1
                  ultimoDigito = mod n 10 


esCapicua2 :: Integer -> Bool
esCapicua2 n = (primerosKDigitos n partirN) == espejarNumero ( ultimosKDigitos n partirN )
             where partirN = div (cantidadDigitos n ) 2
                                         


esPar :: (Integral a) => a -> Bool
esPar n = even n

--EJERCICIO 10 ::..

f1 :: Integer -> Integer
f1 0 = 0
f1 n = f1(n-1) + 2^n    


f2 :: Integer -> Integer -> Integer
f2 _ 0 = 0
f2 n q = f2(n-1) q + q^n

f3 :: Integer -> Integer -> Integer
f3 1 q  = q
f3 n q = f3 (n-1) q + q^(2*n-1) + q^(2*n)


--EJERCICIO 11::..

--fromIntegral :: Int -> Float

factorial  :: Integer -> Integer
factorial 0 = 1
factorial n = factorial (n-1) * n

eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n =  1 / fromIntegral(factorial n) + eAprox (n-1)

e :: Float
e = eAprox 10 
 


--EJERCICIO 12::..

raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 2
raizDe2Aprox n = 2 + 1 / raizDe2Aprox (n-1)


--EJERCICIO 13::..

sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna _ 0 = 0
sumatoriaInterna i j = sumatoriaInterna i (j-1) + i^j

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0
sumatoriaDoble i j = sumatoriaDoble (i-1) j + sumatoriaInterna i j


 
--EJERCICIO 14::..

sumaPotenciasInterna :: Integer -> Integer -> Integer -> Integer
sumaPotenciasInterna _ _ 0 = 0   
sumaPotenciasInterna q a b = sumaPotenciasInterna q a (b-1) + q^(a+b)

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q a b = sumaPotencias q (a-1) b + sumaPotenciasInterna q a b



--EJERCICIO 15::..

sumaRacionalesInterna :: Integer -> Integer -> Float
sumaRacionalesInterna _ 0 = 0
sumaRacionalesInterna n m = sumaRacionalesInterna n (m-1) + fromIntegral n / fromIntegral m

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 0 _ = 0
sumaRacionales n m = sumaRacionales (n-1) m + sumaRacionalesInterna n m


--EJERCICIO 16::..

buscarMenordivisor :: Integer -> Integer -> Integer
buscarMenordivisor k n | k == n = n
                       | mod n k == 0 = k
                       | otherwise = buscarMenordivisor (k+1) n 


menorDivisor :: Integer -> Integer
menorDivisor n = buscarMenordivisor 2 n


esPrimo :: Integer -> Bool
esPrimo 1 = False
esPrimo n = cantidadDeDivisores n == 1


cantidadDeDivisoresDesdeHasta :: Integer -> Integer -> Integer
cantidadDeDivisoresDesdeHasta k n | k == n = 1 
                                  | mod n k == 0 = 1 + cantidadDeDivisoresDesdeHasta (k+1) n  
                                  | otherwise = cantidadDeDivisoresDesdeHasta (k+1) n    

cantidadDeDivisores :: Integer -> Integer 
cantidadDeDivisores n = cantidadDeDivisoresDesdeHasta 2 n 


sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = mcd n m == 1


nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = buscarnEsimoPrimo 1 1 n

       

buscarnEsimoPrimo :: Integer -> Integer -> Integer -> Integer
buscarnEsimoPrimo p posActual posFinal | esPrimo(p) && (posActual == posFinal) = p
                                       | esPrimo(p) && not(posActual == posFinal)  = buscarnEsimoPrimo (p+1) (posActual+1) posFinal
                                       | otherwise = buscarnEsimoPrimo (p+1) posActual posFinal


mcd :: Integer -> Integer -> Integer
mcd 0 m = m 
mcd n m | n >= m = mcd (mod n m) m
        | otherwise = mcd (mod m n) n

sonCoprimos' :: Integer -> Integer -> Bool
sonCoprimos' n m = mcd n m == 1




--EJERCICIO 17 ::..


esFibonacci :: Integer -> Bool
esFibonacci n = encontrarFibonaci 1 n == n

encontrarFibonaci :: Integer -> Integer -> Integer
encontrarFibonaci x n | fibonacci x >= n = fibonacci x
                      | otherwise = encontrarFibonaci (x+1) n 


--EJERCICIO 18 ::..

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | cantidadDigitos n == 1 && not(esPar(digito)) = -1
                 | cantidadDigitos n == 1 && esPar(digito) = digito
                 | esPar(digito) && (digito) >= mayorDigitoPar (div n 10) = digito
                 | otherwise = mayorDigitoPar (div n 10)
                 where digito = iesimoDigito n (cantidadDigitos n)
                      

--EJERCICIO 19 ::..


esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = sumaInicialDePrimos n 1 == n

sumaInicialDePrimos :: Integer -> Integer -> Integer
sumaInicialDePrimos n x | (sumaPrimosDesdeHasta 1 x) >= n  = (sumaPrimosDesdeHasta 1 x)
                        | otherwise = sumaInicialDePrimos n (x+1)

sumaPrimosDesdeHasta :: Integer -> Integer -> Integer
sumaPrimosDesdeHasta k x | k > x = 0
                         | otherwise = sumaPrimosDesdeHasta (k+1) x + (nEsimoPrimo k) 
               
               
--EJERCICIO 20 ::..


sumaDivisoresDesdeHasta :: Integer -> Integer -> Integer
sumaDivisoresDesdeHasta n m | n >= m = n 
                            | mod n m == 0 = sumaDivisoresDesdeHasta (n+1) m + n  
                            | otherwise = sumaDivisoresDesdeHasta (n+1) m 


sumaDivisores :: Integer -> Integer 
sumaDivisores m =  sumaDivisoresDesdeHasta 1 m 


maximo :: Integer -> Integer -> Integer
maximo n m | n >= m = n 
           | sumaDivisores(n) >= maximo(n+1) m = n
           | otherwise = maximo (n+1) m  

tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n m = maximo (sumaDivisores(n)) m

               
               
--EJERCICIO 21::..

--pitagoras :: Integer ->



