def es_primo(numero):
    "Indica si es numero primo y cuantas veces se ejecuta el ciclo for"
    resultado = True
    cont = 0
    for divisor in range(2, numero):
        if(numero % divisor) == 0:
            resultado = False
            cont += 1
            break
        cont += 1
    return resultado, cont

es_primo(13)

s = 0
for n in range(1, 10):
   if n % 11 == 0:
        break
   s += n
else:
    s += 10
print(s)

s = 0
for n in range(1, 10):
   if n % 2 == 0:
        pass;
   s += n
print(s)

