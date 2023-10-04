import math

# Ejercicio 1 ::..

def imprimir_hola_mundo() -> str:
    print("Hola mundo!")

def imprimir_un_verso(algo: str) -> str: 
    print(algo)

def raizDe2(n :int) -> float:
    res = round (math.sqrt(n),4)
    return res


def factorial(n :int) -> int:
    res :int = 1
    for i in range(0,n):
        res *= i
    return res     

def factorial_de_dos() -> int:
    res = factorial(2)
    return res 

def perimetro() -> float: 
    res :float = 2 * math.pi
    return res


# Ejercicio 2 ::..


def imprimir_saludo(nombre: str) -> str:
    print(f"hola {nombre}")

def raiz_cuadrada_de(numero: float) -> float:
    res :float = math.sqrt(numero) 
    return res


def fanrenheit_a_celcius(t :float) -> float:
    res :float = ( t - 32 ) * 5 / 9
    return res


def imprimir_dos_veces(estribillo: str) -> str:
    for i in range(0,2):
        print(estribillo)


def es_multiplo_de (n :int, m: int) -> bool:
    res :bool = n % m == 0
    return res    

def es_par(numero :int) -> bool:
    res :bool = es_multiplo_de (numero, 2)    
    return res


def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int :
    res = math.ceil(comensales*min_cant_de_porciones / 8)


def devolver_el_doble_si_par(n : int) -> int:
    res :int = n
    if es_par(n) :
       res = 2 * n
    return res


# Ejercicio 3 ::..

def alguno_es_0 (numero1 :float,numero2: float) -> float :
    res: bool = numero1 == 0 or numero2 == 0 
    return res

def ambos_son_0 (numero1 :float,numero2: float) -> float:
    res: bool = numero1 == 0 and numero2 == 0
    return res

def es_nombre_largo(nombre: str) -> bool:
    res :bool = len(nombre) >= 3 and len(nombre) <= 8  
    return res

def es_bisiesto (año: str) -> bool:
    res :bool = es_multiplo_de (año, 4) and not es_multiplo_de (año, 100)
    return res


# Ejercicio 4 ::..

def peso_pino(altura: int) -> float:

    peso = altura * 100 / 3

    if max(altura, 3) == altura :
       alturaExtra = altura - 3
       peso = altura + alturaExtra * 100 / 2  

    return peso


def altura_pino (peso: int) -> int:

    altura = (peso / 3)
    pesoExtra = peso - 3
    alturaExtra = (pesoExtra / 2) 

    if max(altura, 3) == altura :
        altura = altura + alturaExtra

    return altura


def es_peso_util (peso: int) -> bool:
    res: bool = min(peso, 400) == 400 and max(peso, 1000)
    return res


def sirve_pino (altura: int) -> bool:
    res: bool = es_peso_util (peso_pino(altura))    
    return res


# Ejercicio 5 ::..

def devolver_el_doble_si_es_par(numero: int) -> int:
    res: int= numero
    if not es_par(numero):
        res = 2*numero
    return res

def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    res: int = numero
    if not es_par(numero):
       res = numero + 1 
    return res


def ordenados (lista: list) -> bool:
    res: bool = True
    i=1
    for elem in lista:
        ultimoElem = lista[len(lista)-1] 
        if elem != ultimoElem :
           siguienteElem = lista[i]
           if not elem <= siguienteElem:
              res = False
              break
        if elem == ultimoElem :
           break
        i+=1
    return res      

print(imprimir_dos_veces("Hola, mundo!"))





