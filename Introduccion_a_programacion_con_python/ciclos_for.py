for i in range(10): #imprime una lista de numeros del 0 al 9
    print(i)
    
for i in "Hola Mundo!": #imprime el string letra por letra
    print(i)
    
def contador(n): #contador con ciclo for
    c = 0
    for i in range(n):
        c += 1
    return c

contador(10) #devuelve 10

#--

def sumatoria(numeros): #sumatoria con ciclo for
    acum = 0
    for n in numeros:
        acum += n
    return acum

sumatoria([1,2,3,4,5]) #devuelve 15

#--

def tabla_multiplicar(numero): 
    "Imprime tabla de multiplicar del numero dado"
    for indice in [0,1,2,3,4,5,6,7,8,9,10]:
        print(numero, "*", indice, "=", numero*indice)
    
tabla_multiplicar(2)