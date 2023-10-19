import random

def pertenece(lista: list, e: int) -> bool:
    res: bool = False
    for elem in lista:
        if elem == e :
            res= True
            break
    return res        

def pertenece_alt (lista: list, e: int) -> bool:
    res: bool = False
    i=0
    while i <= len(lista) and not res == True:
        if lista[i] == e :
            res= True
        i+=1
    return res   

def divideATodos(lista: list, e: int) -> bool:
    res: bool= True
    for elem in lista:
        if elem % e != 0:
            res= False
            break
    return res   

def sumaTotal(lista: list)-> int:
    res: int = 0
    for elem in lista:
        res+=elem
    return res    

def ordenados (lista: list) -> bool:
    i=1
    res= False
    for elem in lista:
        ultimoElem = lista[len(lista)-1] 
        if elem == ultimoElem :
           if elem == lista[i-1]:
               res=True 
        if not elem <= lista[i]:
           res = False
           break
    return res   

def pass_check(contraseña: str) -> str:
    
    res: str = "Amarilla"
    longitud = len( contraseña )
    digitos = [0,1,2,3,4,5,6,7,8,9]
    
    tieneDigitos, tieneMayusculas, tieneMayusculas, tieneDigitos = False,False,False,False 

    for char in contraseña:
        if char == char.uper():
           tieneMayusculas = True
        if char == char.lower():
           tieneMinusculas = True
        if char in digitos:
            tieneDigitos = True

    if longitud > 8 and tieneMayusculas and tieneMinusculas and tieneDigitos:
        res = "Verde"
    if longitud < 5:
        res = "Roja"

def fortalezaContraseña(contraseña: str) -> str:
    
    res: str = "Amarilla"

    longitud: int = len( contraseña )
    tieneMinusculas: bool = False
    tieneMayusculas: bool = False
    tieneDigitos: bool = False
   
    for char in contraseña:
        
        if char >= "0" and char <= "9" and not tieneDigitos: 
           tieneDigitos = True  
        if char >= "A" and char <= "Z" and not tieneMayusculas:
           tieneMayusculas = True
        if char >= "a" and char <= "z" and not tieneMinusculas:
           tieneMinusculas = True

    if longitud > 8 and tieneMayusculas and tieneMinusculas and tieneDigitos:
        res = "Verde"
    if longitud < 5:
        res = "Roja"

    return res

def movimientosBancarios(movimientos: list) -> int:
    saldo: int = 0
    for (operacion,monto) in movimientos:
        if operacion == "I" :
            saldo+= monto
        if operacion == "R" :
            saldo-= monto
    return saldo

def tiene3VocalesDistintas(lista: str) -> bool:

    vocalesIncluidas = []
    cantVocales = 0
    vocales = "aeiou"
    res: bool = len(vocalesIncluidas) >= 3
    
    for char in lista.lower():
        if char in vocales and char not in vocalesIncluidas and cantVocales <= 3:
           vocalesIncluidas.append(char)
           cantVocales +=1
    return res       



# Ejercicio 2 ::..



def borraPosicionesParesInout(lista: int) -> int:
    i=0
    while i <= ( len(lista)-1 ):
        if not i % 2 == 0 :
           lista[i] = 0
        i+=1
    return lista         


def borraPosicionesParIn(lista: int) -> int :
    i=0
    nuevaLista = []
    for num in lista:    
        if i % 2 == 0 :
           nuevaLista.append(num)
        else:
           nuevaLista.append(0)    
        i+=1
    return lista


def borraVocales(lista: list)-> list:
    vocales = "aeiou"
    res: list = []
    for char in lista:
        if not char.lower() in vocales:
           res.append(char)
    return res       


def reemplazaVocales(lista: list) -> list:
    nueva_lista = []
    vocales = "aeiou"
    for char in lista:
        if char in vocales:
           nueva_lista.append(' ')
        if not char in vocales:
            nueva_lista.append(char)
    return nueva_lista  

def reemplazaVocalesStr(string: str) -> str:
    nueva_string = ''
    vocales = "aeiou"
    for char in string:
        if char in vocales:
           nueva_string += ' '
        if not char in vocales:
            nueva_string += char
    return nueva_string  
        

def daVueltaStr(lista: list) -> list:
    nueva_lista = []
    i=len(lista)-1
    while i >= 0:
        nueva_lista.append(lista[i]) 
        i-=1
    return nueva_lista        


def daVueltaStrAlt(string: str) -> str:
    nueva_string = ''
    i=len(string)-1
    while i >= 0:
        nueva_string += string[i] 
        i-=1
    return nueva_string        


def elimnarReptidos(lista: list) -> list:
    res: list = []
    for char in lista:
        if char not in res:
            res.append(char)
    return res       


def aprobado(notas:list ) -> list:

    cantidadNotas = len(notas)
    sumaNotas = sumaTotal(notas)
    promedio = cantidadNotas / sumaNotas
    
    res = 0
    
    for nota in notas :
        if nota >= 4 and promedio >= 7:
           res = 1  
        if nota >= 4 and promedio >= 4 and promedio < 7:
           res = 2   
        if nota < 4 or promedio < 4 :
           res = 3   

    return res           


def listaDeEstudiantes() :

    listaDeNombres = []

    while 'listo' not in listaDeNombres:
           listaDeNombres.append(input()) 
    listaDeNombres.remove('listo')
           
    return listaDeNombres 


def monederoElectronico():

    mensaje = "-------------------- \n Operaciones: \n C = Cargar credito \n D = Descontar creditos \n X = Finalizar la simulacion \n --------------------" 
    historial = []
    operaciones = []
    
    def creditoValido() -> str :
        credito = [input()]
        while not credito[0].isdigit():
            print("*valor no valido")
            credito=[input()]
        return credito[0]    

    while "X" not in operaciones:
        print(mensaje)
        operaciones = [input().upper()]
        if "C" in operaciones:
           print("--------------------") 
           print("Cargar credito \n Ingresa un valor: ")
           historial.append( ("C",creditoValido()) )
           print("--------------------") 
        if "D" in operaciones:
           print("--------------------") 
           print("Descontar credito \n Ingresa un valor: ")
           historial.append( ("D",creditoValido()) ) 
           print("--------------------")     
    return historial       




def sieteYMedio() -> list:

    historial: int = []
    puntos: int = 0
    repartir = True

    carta: int = random.randint(1,12)
    cartasInValidas = [8,9]
    figuras = [10,11,12]
    
    while repartir and puntos <= 7.5:
        
        if carta not in cartasInValidas:  

           if carta in figuras :
              historial.append(0.5)
           else:
              historial.append(carta)  

           carta = random.randint(1,12)
           repartir = random.choice(["carta","plantarse"]) != "plantarse"
           puntos: int = sumaTotal(historial)      

           if puntos > 7.5:
              print("Perdiste!")    

    return historial


# Ejercicio 5::..

    


def pertenceACadaUno (listaDeListas: [[int]], e: int) -> [int]:
    i=0
    res: list = [] 
    for lista in listaDeListas:
        res.append(pertenece (lista, e))       
    return res            

def esMatriz(listaDeListas: [[int]]) -> bool:
    
    longitud = len(listaDeListas[0]) 
    res: bool = longitud > 0
    
   
    for lista in listaDeListas:
        if not res:
           break 
        res = longitud == len(lista)

    return res


def filasOrdenadas(Matriz: list)-> bool :
    res: bool = True
    for lista in Matriz:
        res = ordenados(lista)
        if not res:
           break  
    return res      

print(sieteYMedio())       


















