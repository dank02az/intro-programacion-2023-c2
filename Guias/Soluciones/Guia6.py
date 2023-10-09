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


def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    res: bool = 0
    if es_multiplo_de (numero,3):
        res: bool = 2 * numero
    if es_multiplo_de (numero, 9):
        res: bool = 3 * numero
    return res           

def lindo_nombre(nombre: str) -> str:  
    res: str = "Tu nombre tiene menos de 5 caracteres"
    if len(nombre) >= 5: 
        res = "Tu nombre tiene muchas letras!"
    return res

def elRango(numero: int) -> str:
    res :str = ''
    if numero < 5 :
       res = "Menor a 5"
    if numero >= 10 and numero <= 20:
       res = "Entre 10 y 20"
    if numero > 20:
       res = "Mayor a 20"         
    return res

def vacaciones(edad: int, sexo: str):
    sexo = sexo.upper()
    
    res: str = "Anda de vaciones"
    if edad >= 18:
       res = "Te toca trabajar"      
    if sexo == "F" and edad > 60:
       res = "Anda de vaciones" 
    if sexo == "F" and edad <= 60:
       res = "Te toca trabajar"  
    if sexo == "M" and edad <= 65: 
       res = "Te toca trabajar"      
    if sexo == "M" and edad > 65:
       res = "Anda de vacaciones"
    return res   
 
# Ejercicio 6::..

def uno_al_diez():
    i=1 
    while i <= 10 :
        print(i)
        i+=1


def pares_10_40 ():
    i=10
    while i <= 40:
        print(i)
        i+=2


def eco_10():
    i=10
    while i<=10:
      print("Eco")        
      i+=1

def cuenta_regresiva(n: int):
    i=n
    while i >= 0:
      print(i)
      i-=1
    return 'Despegue!'     


def viaje_al_pasado(partida: int, llegada: int) -> str : 
    año = partida
    while not año == llegada:
        print(f"Viajo 1 año al pasado, estamos en el año {año}")
        año-=1
    return ''

def monitoreoDeViaje(partida: int) -> str:
    año: int = partida
    llegada: int = -384
    while not año <= llegada:
          data = f"{año} d.C" 
          if año < 0 :
            data = f"{(-1)* año} a.C"            
          print(f"Viajo 20 años al pasado, estamos en el año {data}")
          año-= 20
    return ''      

# Ejercicio 7::..

def uno_al_diez_for():
    for i in range(0,11):
        print(i)


def pares_10_40_for():
    for i in range(10,41,2):
        print(i)

def eco_10_for():
    for i in range(0,11):
        print("eco")

def cuenta_regresiva_for(hasta: int) -> int:
    for i in range(hasta,-1,-1):
        print(i)
    return "Despegue!"    

def viaje_en_el_tiempo(partida: int, llegada: int) -> str:
    año: int = partida
    for i in range(partida,llegada-1,-1):
        print(f"Viajo un año al pasado, estamos en el año: {año}")
    return ""


def monitoreo_de_viaje_for(partida: int):
    año: int = partida
    llegada: int = -384
    for i in range(partida, llegada-1,-20):
          data = f"{año} d.C" 
          if año < 0 :
            data = f"{(-1)* año} a.C"            
          print(f"Viajo 20 años al pasado, estamos en el año {data}")
          año-= 20
    return ''    
