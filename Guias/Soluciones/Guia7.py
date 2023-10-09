def pertenece(lista: list, e: int) -> bool:
    res: bool = False
    for i in lista:
        if i == e:
            res = True
    return res 
       
def perteneceAlt(lista: list, e: int) -> bool:
    res: bool = False
    i=0
    while i <= len(lista):
        if lista[i] == e:
           res = True
        i+=1
    return res           


def divideATodos(lista: list, e: int) -> bool:
    res: bool = True
    for elem in lista:
        if elem % e != 0:
            res =  False 
            break
    return res        