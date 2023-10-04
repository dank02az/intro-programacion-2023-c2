import Test.HUnit
import Guia5
import Guia4
import Otras



main = runTestTT todosLosTest 
todosLosTest = test [guia5Test]


-- Test Guia5::..


testSuiteSumaAcumulada = test [
  "Caso Base 1: sumaAcumulada []" ~: ( sumaAcumulada [] ) ~?= [] ,
  "Caso recursivo 1: sumaAcumulada [1,2] " ~: ( sumaAcumulada [1,2] ) ~?= [1,3],
  "Caso recursivo 2: sumaAcumulada [1,2,3,4]" ~: ( sumaAcumulada [1,2,3,4] ) ~?= [1,3,6,10]
  ]


testSuiteDescomponerEnPrimostest = test [
  "Caso Base 1: descomponerEnPrimos []" ~: ( descomponerEnPrimos [] ) ~?= [] ,
  "Caso recursivo 1: descomponerEnPrimos [35,120]" ~: ( descomponerEnPrimos (lista_Int_1) ) ~?= factoresPrimos_lista_Int_1,
  "Caso recursivo 2: descomponerEnPrimos [10,21,90]" ~: ( descomponerEnPrimos (lista_Int_2) ) ~?= factoresPrimos_lista_Int_2
  ]

testSuiteSacarEspaciosRepetidos = test [
  "Caso Base 1: SacarEspaciosRepetidos []" ~: ( sacarEspaciosRepetidos [] ) ~?= [] ,
  "Caso recursivo 1: SacarEspaciosRepetidos 'hola  mundo'" ~:  ( sacarEspaciosRepetidos (holaMundoConEspaciosRep) ) ~?= holaMundoSinEspacioRep
  ]



runGuia5 = runTestTT guia5Test
guia5Test = test [ testSuiteSumaAcumulada, testSuiteSacarEspaciosRepetidos, testSuiteDescomponerEnPrimostest ]


--runTestName = runTestTT testSuiteName

expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- Casos De Test

holaMundoConEspaciosRep = ['h','o','l','a',' ',' ','m','u','n','d','o']
holaMundoSinEspacioRep = ['h','o','l','a',' ','m','u','n','d','o']


descomposicion35 = [5,7] 
descomposicion120 = [2,2,2,3,5]
descomposicion10  = [2,5]
descomposicion21 = [3,7]
descomposicion90 = [2,3,3,5]


lista_Int_1 = [35,120]
lista_Int_2 = [10,21,90]
factoresPrimos_lista_Int_1 = [descomposicion35,descomposicion120]
factoresPrimos_lista_Int_2 = [descomposicion10,descomposicion21,descomposicion90]




