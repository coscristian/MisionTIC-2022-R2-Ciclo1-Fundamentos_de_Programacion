"""
Ejercicio 5
Cual sería la expresión List Comprehension para generar la siguiente 
lista: `[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`
"""

lista = [n**3 for n in range(11)]
print(lista)