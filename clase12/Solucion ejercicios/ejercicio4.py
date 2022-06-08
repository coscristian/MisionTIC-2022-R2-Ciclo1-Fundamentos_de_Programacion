"""
Ejercicio 4
Que valores generan las siguientes List Comprehensions
* [x**2 for x in range(10)]
* [2**i for i in range(13)]

*La primera list comprehension genera 
el cuadrado de los numeros de los numeros del cero al nueve

*La segunda lista genera la serie de numeros 1 2 4 8 16 32 64 128.... 
"""

cuadrados = [x**2 for x in range(10)]
serie = [2**i for i in range(13)]

print(cuadrados, serie, sep="\n")

