# en este ejemplo de modulo se importa el archivo 'fibo.py' 
# con funciones para crear secuencias fibonacci

import fibo # se importa el archivo completo 

fibo.fib(1000)
fibo.fib2(1000)

from fibo import fib,fib2 # se importan las funciones correspondientes

fib(2000)
fib2(2000)

#--------------
import fibo

dir(fibo) # la funcion dir() se usa opara encontrar los nombres que define el modulo

#Impirme -> ['__builtins__', '__cached__', '__doc__',
#'__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']