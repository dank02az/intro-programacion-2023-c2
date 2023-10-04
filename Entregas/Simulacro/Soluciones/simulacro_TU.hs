module Simulacro_Test where 

import Test.HUnit
import Simulacro

--Casos de Test

run = runTestTT tests

tests = test [
  ”Caso Base 1: fib 0” ˜ : ( fib 0 ) ˜?= 0 ,
  ”Caso Base 2: fib 1” ˜ : ( fib 1 ) ˜?= 1 ,
  ”Caso recursivo 1” ˜ : ( fib 2 ) ˜?= 1
]

