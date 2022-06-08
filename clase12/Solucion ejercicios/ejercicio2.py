"""Crea una nueva lista que a partir de otra lista de números que contenga solo los números positivos de la lista, como enteros.  
La lista es `numeros = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]`"""

numeros = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positivos = [int(num) for num in numeros if num > 0]
print(positivos)