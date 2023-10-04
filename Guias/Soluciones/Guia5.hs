module Guia5 where
import Guia4 



longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = longitud xs + 1


ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs


reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = e==x || pertenece e xs 

todoIguales :: (Eq t) => [t] -> Bool
todoIguales [] = True
todoIguales (x:y:xs) = x == y && todoIguales xs


todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:y:xs) = x /= y && todosDistintos xs


hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs
                    

quitar :: (Eq t) => t -> [t] -> [t]
quitar n [] = []
quitar n (x:xs) | n == x = xs 
                | otherwise = quitar n xs
                    
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos n [] = []
quitarTodos n (x:xs) | n /= x = x : quitarTodos n xs 
                     | otherwise = quitarTodos n xs


eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = [] 
eliminarRepetidos (x:xs) | pertenece x xs = x : quitarTodos x (eliminarRepetidos xs)                     
                         | otherwise = x : eliminarRepetidos xs


incluido :: (Eq t) => [t] -> [t] -> Bool
incluido [] _ = True
incluido (y:ys) (x:xs)| pertenece y (x:xs) = incluido ys (x:xs)
                      | otherwise = False


mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos (x:xs) (y:ys) = incluido (eliminarRepetidos(x:xs)) (eliminarRepetidos(y:ys)) && incluido (eliminarRepetidos(y:ys))(eliminarRepetidos(x:xs)) 


esPermutacion :: (Eq t) => [t] -> [t] -> Bool
esPermutacion x y = mismosElementos x y


sonIguales :: (Eq t) => [t] -> [t] -> Bool
sonIguales [][] = True
sonIguales (x:xs) (y:ys) | longitud (x:xs) /= longitud(y:ys) = False
                         | x /= y = False
                         | otherwise = sonIguales xs ys

capicua :: (Eq t) => [t] -> Bool 
capicua (x:xs) =  sonIguales (x:xs) (reverso(x:xs))


sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = sumatoria xs + 1


productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = productoria xs * 1


maximo' :: [Integer] -> Integer
maximo' [x] = x 
maximo' (x:y:xs) | x >= y = maximo'(x:xs)
                 | otherwise = maximo'(y:xs) 

sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = x+n : sumarN n xs 

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo(x:xs)) (x:xs)


pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs)  | even x = x : pares xs
              | otherwise = pares xs

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)  | mod x n == 0 = x : multiplosDeN n xs
                       | otherwise = multiplosDeN n xs
                       

ordenar :: [Integer] -> [Integer]
ordenar [x] = [x]
ordenar (x:xs)  = ordenar ( quitarTodos(maximo'(x:xs)) (x:xs)) ++ [maximo'(x:xs)]


--EJERCICIO 5::..

--5.1

sumarTerminos :: (Num t) => [t] -> t
sumarTerminos [] = 0
sumarTerminos (x:xs) = sumarTerminos xs + x



sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada (x:xs) =  sumaAcumulada (principio(x:xs)) ++ [sumarTerminos (x:xs)]


--5.2


descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (factoresPrimos 1 x) : descomponerEnPrimos xs

factoresPrimos :: Integer  -> Integer -> [Integer]
factoresPrimos _ 1 = []
factoresPrimos p n | mod n (nEsimoPrimo p) == 0 = (nEsimoPrimo p) : factoresPrimos p (div n (nEsimoPrimo p))
                   | otherwise = factoresPrimos (p+1) n



--EJERCICIO 4::..


sacarEspaciosRepetidos :: [Char] -> [Char]
sacarEspaciosRepetidos [] = []
sacarEspaciosRepetidos (x:[]) = [x]
sacarEspaciosRepetidos (x:y:xs) | x==y && x==' '= sacarEspaciosRepetidos (y:xs)
                                | otherwise = x:(sacarEspaciosRepetidos (y:xs))





quitarEspaciosExtremos :: [Char] -> [Char]
quitarEspaciosExtremos [] = []
quitarEspaciosExtremos (x:y:xs)  | x == ' ' && ultimo(x:y:xs) == ' ' = principio(y:xs) 
                                 | x == ' ' && ultimo(x:y:xs) /= ' ' = (y:xs)
                                 | x /= ' ' && ultimo(x:y:xs) == ' ' = principio(x:y:xs)
                                 | otherwise = (x:y:xs)



contarPalabras :: [Char] -> Integer
contarPalabras (x:xs) = contarPalabrasAux (quitarEspaciosExtremos( sacarEspaciosRepetidos (x:xs) ))


contarPalabrasAux :: [Char] -> Integer
contarPalabrasAux [] = 0
contarPalabrasAux [x] = 1
contarPalabrasAux (x:xs) | x ==' ' = contarPalabrasAux(xs) + 1
                         | otherwise = contarPalabrasAux xs 


palabra :: [Char] -> [[Char]]
palabra [] = []
palabra (x:xs) = primeraPalabra (x:xs) :   palabra (quitarPalabra(primeraPalabra (x:xs)) (x:xs))

 
quitarPalabra :: [Char] -> [Char] -> [Char]
quitarPalabra _ [] = []
quitarPalabra [] l = l
quitarPalabra (x:xs) (y:ys)  | not(incluido(x:xs)(y:ys)) = [] 
                             | otherwise = quitarEspaciosExtremos (quitarPalabra  xs (quitar x (y:ys)))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x == ' ' =  []
                      | otherwise = x : primeraPalabra xs

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga p = palabraMasLargaAux (palabra p) 
 
palabraMasLargaAux :: [[Char]] -> [Char]
palabraMasLargaAux [x] = x
palabraMasLargaAux (x:xs) | longitud(x) >= longitud(palabraMasLargaAux xs) = x
                          | otherwise = palabraMasLargaAux xs
                          
                          
                          
