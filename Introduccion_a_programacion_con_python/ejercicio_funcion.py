def fib(n):
    "Devuelve el valor de 'n' en la escala de fibonacci"
    a = 0
    b = 1
    
    for k in range(n):
        c = a + b
        a = b
        b = c
    return b

print(fib(34))