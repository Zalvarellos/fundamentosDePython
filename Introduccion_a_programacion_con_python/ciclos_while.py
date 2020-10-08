def suma_n(n):
    "Suma los números de 1 a n"
    result = 0
    x = 1
    while x <= n:
        result += x
        x += 1
    return result

suma_n(5)

def ciclo_infinito():
    "Imprime el número 1 infinitas veces!!"
    i = 1
    while i <= 10:
        print(i, end=" ")

ciclo_infinito() #Kill con "Ctrl+C"