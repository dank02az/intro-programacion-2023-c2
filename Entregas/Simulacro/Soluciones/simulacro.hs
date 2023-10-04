relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((a,b):xs) = a /= b && not(pertenece (a,b) xs) && not(pertenece (b,a) xs) && relacionesValidas xs

         
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs                           

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:y:xs) | x == y = eliminarRepetidos (x:xs)
                           | otherwise = eliminarRepetidos (y:xs)


personas ::  [(String,String)] -> [String]
personas [] = []
personas ((a,b):xs) = eliminarRepetidos ( a:b:(personas xs) )                  
 
 
amigosDe :: String -> [(String,String)] -> [String] 
amigosDe _ [] = []
amigosDe n ((a,b):xs) | n == a = b : amigosDe n xs
                      | n == b = a : amigosDe n xs
                      | otherwise =  amigosDe n xs   
  
 
cantidadDeAmigos :: String -> [(String,String)] -> Integer
cantidadDeAmigos n (x:xs) = longitud (amigosDe n (x:xs)) 


longitud :: [String] -> Integer
longitud [] = 0
longitud (x:xs) = longitud xs + 1 

 
personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos (x:xs) = personaConMasAmigosAux (personas (x:xs)) (x:xs)

 
personaConMasAmigosAux :: [String] -> [(String,String)] -> String
personaConMasAmigosAux [x] _ = x
personaConMasAmigosAux (x:xs) (y:ys) | cantidadDeAmigos x (y:ys) >= cantidadDeAmigos (personaConMasAmigosAux xs ys) ys = x
                                     | otherwise = personaConMasAmigosAux xs ys
