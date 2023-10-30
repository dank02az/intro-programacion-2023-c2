from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# archivo = open(file_name, "r")
# texto = archivo.read()
# primeraLinea = archivo.readline()
# lineas = archivo.readlines()
# palabras = "hola como estas".split()
# archivo.write("string")
# archivo.writelines()
# random.shuffle()
# random.sample()
# random.randint()

def contar_lineas(file_name: str) -> int:
    archivo = open(file_name, "r")
    texto = archivo.readlines()
    res: int = len(texto)
    archivo.close()
    return res

def existe_palabra(palabra: str, file_name: str) -> bool:
    archivo = open(file_name, "r")
    texto = archivo.readlines()
    res: bool = False
    for line in texto:
        for pal in line.split():
            if pal == palabra:
               res = True
               break
    return res      

def cantidad_apariciones( file_name: str, palabra: str) -> bool:
    archivo = open(file_name, "r")
    texto = archivo.readlines()
    res: int = 0
    for line in texto:
        for pal in line.split():
            if pal == palabra:
               res += 1
    return res  


def clonar_sin_comentarios(file_name: str): 
    archivo = open(file_name, "r")   
    res = open("sin_comentarios","w+")
    texto = archivo.readlines()
    
    for line in texto:
        if len(line) == 0 or not "#" == line.strip()[0]:
           res.writelines(line) 
           
    archivo.close()
    res.close()       

def eliminarChar(lista: list, char: str):
    nuevaLista = ""
    for elem in lista:
        if not elem == char:
           nuevaLista+= elem
    return nuevaLista           

def reverso(file_name: str) :
    archivo = open(file_name, "r")
    lineas = archivo.readlines()
    reverso = []
    res = open("reverso", "w")
    
    for i in range(len(lineas)-1,-1,-1):
        reverso.append(lineas[i])   
         
    for elem in reverso:
        if elem == reverso[0]:
           elem = f"{elem}\n"
        if elem == reverso[len(reverso)-1]:
           elem = eliminarChar(elem,"\n")    
        res.write(str(elem))       

    archivo.close()
    res.close()
 
def frase_al_final(file_name: str, frase: str):
    archivo = open(file_name, "r+") 
    lineas = archivo.readlines() + [f"\n{frase}"]
    
    archivo = open(file_name, "w")
    for line in lineas:
        archivo.write(line)

def frase_al_principio(file_name: str, frase: str):
    archivo = open(file_name, "r+")
    lineas = [f"{frase}\n"] + archivo.readlines()
    for line in lineas:
        archivo.write(line)


def leerBinario(file_name: str) -> [str]:
    archivo = open(file_name, "rb")
    lineas = archivo.readlines()

    numeros = [1,2,3,4,5,6,7,8,9,0]
    letras = "abcdefghijklmnñopqrstuvwxyz"
    chars = [" ","_"]
    
    char_legibles = list(letras) + list(letras.upper()) + chars + numeros

    res = []
    palabra = ""

    for char in lineas:
        if chr(char) in char_legibles:
           palabra+=chr(char)
           if len(palabra) > 5:
              res.append(palabra) 
              palabra = ""
        else:
           palabra = ""

    return res       


                    

def promedioNotas (file_name: str, alumno: str) -> int:
    archivo = open(file_name, "r")
    lineas = archivo.readlines()

    palabra, matriz, linea = '',[], []

    # convierto lineas en una matriz
    for line in lineas :
        for char in line:
            if not char == ',':
               palabra+=char 

               # ultimaPalabra
               if char == line[-1]:
                  linea.append(palabra)
                  matriz.append(linea)
                  palabra = ''
                  linea = [] 

            else:
              linea.append(palabra)
              palabra=''
    
    sumNotas, cantidadDeMaterias= 0, 0

    for line in matriz:
        if line[0] == alumno:
           sumNotas += float(line[-1]) 
           cantidadDeMaterias += 1 
           promedio = sumNotas / cantidadDeMaterias


    return round(promedio,2)    


# PARTE 2. PILA ::...            

# p = Pila ()
# p . put (1) # apilar
# elemento = p . get () # desapilar
# p . empty () # vacia ?                     
     

def generar_nros_al_azar(n: int, desde: int, hasta:int) -> Pila:
    p = Pila()
    nmroAlAzar = random.randint(desde, hasta)
    i=0
    while i <= n :
        p.put(nmroAlAzar)
        i+=1
    return p
      
def cantidadElementos(p: Pila) -> int:
    res: int = 0
    lista = []
    
    while not p.empty() :
          lista.apend(p.get())
          res+=1
          
    i=len(lista)-1   
    while i >= 0:
          p.put(lista(i))
          i-=1
    return res   

def buscarElMaximo(p: Pila) -> int:
    lista : list = []
    while not p.empty():
        lista.append(p.get())
        
    i=len(lista)-1   
    while  i >= 0:
          p.put(lista(i))
          i-=1
          
    res: int = max(lista)      
    return res     
          
               
          

def estaBienBalanceada(s:str) -> bool:
    p = Pila()
    
    res: bool = False 

    for char in s:
        if char == "(" :
           p.put(char)
        elif char == ")" :
            if p.qsize() > 0 :
               p.get()
            else : 
                res = False
                break       
        
    if p.qsize() == 0:
        res = True

    return res        



def notacionPolacaInversa (expresion: str) -> int:
    p = Pila()

    operadores = ["+","-","*","/"]

    for char in expresion.split():
        if char not in operadores:
            p.put(char)
        else:
            a = int(p.get()) 
            b = int(p.get())
            
            if char == "+":   
               p.put(b + a)
            if char == "-":
               p.put(b - a)    
            if char == "*":
               p.put(b * a)  
            if char == "/":
               p.put(b / a)

    return  p.get()       




# PARTE 3. COLA ::...    

# c = Cola ()
# c . put (1) # encolar
# elemento = c . get () # desencolar ()
# c . empty () # vacia ?

def generarColasAlAzar(n: int, desde: int, hasta:int):
    p = generar_nros_al_azar(n, desde, hasta)
    c = Cola()
    while not p.empty():
        c.put( p.get() )



def cantidad_elementos(c : Cola) -> int:
    res: int =0
    cola = []
    while not c.empy():
        cola.append(c.get())
        res+=1
    i=0    
    while i >= len(cola)-1:
        c.put(cola[i])
        i+=1
    return res

def buscar_el_maximo(c: Cola) -> int:
    
    cola = Cola()
    res: int = 0

    while not c.empty() :
        cola.put(c.get())
        res += 1

    while not cola.empty():
        c.put(cola.get())
   
    return res 

    
# genNrosAlAzar =  lambda n,desde,hasta : random.sample([x for x in range(desde,hasta+1)], n)

# 17.

def n_pacientes_urgentes(c : Cola[(int, str, str)])-> int:

    cantPacientes = 0
    caux = Cola()
    lista = []

    i=0
    while not c.empty():
        lista.append(c.get()) 
        caux.put(lista[i])
        i+=1

    while not caux.empty:
        c.put(caux.get())    

    for priodidad, paciente, especialidad in lista:
        if priodidad in range(1,3+1):
           cantPacientes += 1

    return cantPacientes


# 18.
def  a_clientes(c: Cola[(str,int,bool,bool)]) -> Cola[(str,int,bool,bool)]:
    res = Cola()
    lista = []

    while not c.empy:
        lista.append(c.get())
    
    for i in lista: c.put(i)

    prioridad, preferencial, resto = [],[],[]

    for nombre, dni, esPreferencial, tienePriodidad in lista:
        if tienePriodidad:
           prioridad.append((nombre,dni,esPreferencial,tienePriodidad))
        elif esPreferencial and not tienePriodidad:    
           preferencial.append((nombre,dni,esPreferencial,tienePriodidad))
        elif not tienePriodidad and not esPreferencial:  
           resto.append((nombre,dni,esPreferencial,tienePriodidad))
    lista = prioridad + preferencial + resto

    for i in lista:
        res.put(i)

    return res



# PARTE 4. Diccionarios::..



def cantidadDeAparicionesYLen(filename: str, palabra: str) -> (str,int):
    archivo = open(filename, "r")
    lineas = archivo.readlines()
    
    apariciones = 0 
    res = (apariciones, len(palabra))
    for line in lineas:
        for pal in line.split():
            if pal == palabra:
               apariciones += 1 
    return res           



def agruparPorLongitud(file_name: str) -> dict:
    archivo = open(file_name, "r")
    texto = archivo.read()
    
    dic: dict = {}
    palabra: str = ''

    for char in texto:
        if char == '\n':
           char = ' ' 
        if char != ' ':
           palabra += char
           
           #ultima Palabra
           if char = texto[-1]:
             if not len(palabra) in dic:    
                dic[len(palabra)] = 1 
             else :
                dic[len(palabra)] += 1    
               
        else:  
          if not len(palabra) in dic:    
             dic[len(palabra)] = 1 
          else :
             dic[len(palabra)] += 1    
          palabra = ''
    
    archivo.close() 
    return dic 


def cantidadDeAparicionesDic(file_name: str) -> dict:
    archivo = open(file_name, "r")
    texto = archivo.read()
    
    dic = {}
    palabra: str =''

    for char in texto:
        if char == '\n':
           char = ' ' 
        if char != ' ':
           palabra += char
           #veo la utlima palabra 
           if char == texto[-1]:
              if not palabra in dic:
                 dic[palabra] = 1
              else:
                 dic[palabra] += 1  
              palabra = ''   
        else:  
          if not palabra in dic:    
             dic[palabra] = 1 
          else :
             dic[palabra] += 1    
          palabra = ''
     
    return dic 

def laPalabraMasFrecuenteDic(file_name: str):
    
    dic = cantidadDeAparicionesDic(file_name)
    
    palabraMasFrecuente:str
    maximo = 0
    for key, value in dic.items():
        if value >= maximo and key != '' :
           maximo = value
           palabraMasFrecuente = key 

    return palabraMasFrecuente    
    



def promedioDeNotasDic(file_name:str)->int:
    archivo = open(file_name,'r')
    lineas = archivo.readlines()
   
    #inicializo todas las variables
    matrizLineas, linea, listaAlumnos, palabra = [], [], [],''
    sumNotas, cantMate = 0, 0  
    dic = {}

    #convierto el texto en una matriz
    for line in lineas:
        for char in line:
            if char != ',':
               palabra+=char
               if char == line[-1]:
                    # agrego ultima palabra y armo lista de palabras    
                    linea.append(palabra)
                    matrizLineas.append(linea) 
                    # limpio las var para armar una nueva linea      
                    linea, palabra = [], ''
            else:
               linea.append(palabra)    
               palabra = ''

    # armo lista de alumnos (sin repetidos)
    for line in matrizLineas:
        if line[0] not in listaAlumnos:
           listaAlumnos.append(line[0])

    # saco promedios y agrego a dic
    for alumno in listaAlumnos:
        for line in matrizLineas:
            for char in line:
                if char == alumno:
                   sumNotas += float(line[-1])
                   cantMate +=1 

        promedio = sumNotas / cantMate
        dic[alumno]= round(promedio,2) 
        # limpio variables para un nuevo Alumno
        sumNotas,cantMate,promedio = 0,0,0

    return dic    



# Navegacion de Sitio web

historiales, operaciones = {}, {}

def visitar_sitio(historiales: dict,usuario: str,url: str):  
    if usuario not in historiales :
      historiales[usuario] = Pila()
      historiales[usuario].put(url)  
    # inicializo operaciones:
    #     que guarda las operaciones de navegacion
      operaciones[usuario] = Cola()
    else:
      historiales[usuario].put(url)  

def navegar_atras(historiales:dict, usuario:str):
    if usuario in historiales :
    #  quito elem de historiales y agrego a operaciones 
       operaciones[usuario].put(historiales[usuario].get())   

def navegar_adelante(historiales: dict, usuario: str):
    if usuario in historiales :
    #  agrego elem en historiales y quito de operaciones   
       historiales[usuario].put(operaciones[usuario].get()) 


def sitio_web_runTest():
    visitar_sitio(historiales, "Usuario1", "google.com")
    visitar_sitio(historiales, "Usuario1", "facebook.com")   
    navegar_atras(historiales, "Usuario1")
    visitar_sitio(historiales, "Usuario2", "youtube.com")
    print(historiales.keys())
    print(historiales.values())



# Iventario de tienda de ropa


inventario = {}

def agregar_producto(inventario: dict, nombre: str, precio: str, cantidad: int): 
    if nombre not in inventario:
       inventario[nombre]={'precio': precio,'cantidad': cantidad}

def actualizar_stock(inventario: dict, nombre: str, cantidad: int):
    inventario[nombre]['cantidad']=cantidad 

def actualizar_precios(inventario: dict, nombre: str, precio: int):
    inventario[nombre]['precio']=precio 

def calcular_valor_inventario(inventario):
    valor_inventario = 0
    for producto, precio_stock in inventario.items():
        valor_inventario += precio_stock['precio'] * precio_stock['cantidad']   
    return valor_inventario


def inventario_runTest():
    agregar_producto(inventario, "Camisa", 20.0, 50)
    agregar_producto(inventario, "Pantalón", 30.0, 30)
    actualizar_stock(inventario, "Camisa", 10)
    valor_total = calcular_valor_inventario(inventario)
    print("Valor total del inventario:", valor_total) # Deberı́a imprimir 1300.00
 

print(inventario_runTest())
