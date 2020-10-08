from math import hypot
from math import sqrt

c1 = int(input("indique cateto1: "))
c2 = int(input("indique cateto2: "))

h1 = sqrt(c1 ** 2 + c2 ** 2)

h2 = hypot(c1, c2)

print(h1)

print(h2)