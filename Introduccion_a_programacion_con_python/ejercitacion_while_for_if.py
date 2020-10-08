# ¿Cuál es el resultado de sumar los primeros 50 números pares? 
# (Desde el 2 inclusive hasta el 100 inclusive)

def sumatoria_2_al_n_numeros_pares(n):
    "Suma los numeros del 2 al n inclusive si es par"
    x = 2
    result = 0
    for x in range(2, n+1, 2):
        result += x
    return result

sumatoria_2_al_n_numeros_pares(100)