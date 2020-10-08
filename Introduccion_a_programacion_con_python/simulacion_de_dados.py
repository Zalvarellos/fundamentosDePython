import random

def tirar_dados():
    a = int(random.randrange(1, 7))
    
    b = int(random.randrange(1, 7))

    print("Dado 1:", a)

    print("Dado 2:", b)

    print("Sumatoria de dados:", a + b)    

tirar_dados()

respuesta = input("Tirar los dados nuevamente (s/n)?")

while respuesta == "s" or respuesta == "S" or respuesta == "si" or respuesta == "Si" or respuesta == "SI" or respuesta == "n" or respuesta == "N" or respuesta == "no" or respuesta == "No" or respuesta == "NO":
    
    if respuesta == "s" or respuesta == "S" or respuesta == "si" or respuesta == "Si" or respuesta == "SI":
        
        tirar_dados()
        
        respuesta = input("Tirar los dados nuevamente (s/n)?")
    
    elif respuesta == "n" or respuesta == "N" or respuesta == "no" or respuesta == "No" or respuesta == "NO":
        
        print("Hasta Luego!")
        break
else:
    print("Respuesta incorrecta!!")       
    
    
    
    
