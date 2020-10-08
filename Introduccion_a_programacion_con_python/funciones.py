# Las funciones se crean a partir de la palabra reservada "'def'_nombreDeLaFuncion_(listaDeParametros)"

def cero(): # devuelve simplemente el numero 0
    return 0

def suma_uno(un_numero): 
    "Suma uno al número recibido como parámetro (esto es un docstring)"
    return un_numero + 1

def suma(a, b):
    "Realiza una suma entre a y b, devolviendo el resultado de la misma"
    resultado = a + b
    return resultado # resultado es una variable local, tal como a y b, no existen fuera de la funcion!!

def f(a, L=[]): #retorna el valor de a en una lista 'L' + los valores q tenga anteriormente cargados
    L.append(a)
    return L

def f(a, L = None): # retorna siempre una nueva lista con el valor de 'a'
    if L is None:
        L = []
    L.append(a)
    return L

