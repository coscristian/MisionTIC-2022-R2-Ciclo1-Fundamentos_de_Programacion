"""
### Ejercicio 6
Con la lista `frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']`generar 
otra con la cantidad de caracteres que tiene cada fruta: `[5, 4, 5, ...]`.
"""

frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']
cant_caracteres = [len(palab) for palab in frutas]
print(cant_caracteres)