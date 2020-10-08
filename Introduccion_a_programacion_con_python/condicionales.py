# Escriba un programa que sume 1 a la variable x si es par o 2 si es impar:

x = 1 + 4 * 3 + 8 / 2 * 4 + 5 ** 2

if x % 2 == 0:
    x += 1
    print("Es par, el valor de X es:", x)
else:
    x += 2
    print("Es impar, el valor de X es:", x)

    
