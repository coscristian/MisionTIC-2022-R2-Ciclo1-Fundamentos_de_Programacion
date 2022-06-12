"""
### Ejercicio 7
Con la lista `frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']`generar 
otra con las frutas que solo tengan exactamente 2 vocales: `['mango', 'kiwi', ...]`.
"""

frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']

def tiene_dos_vocales(fruta:str):
    vocales = "aeiou"
    cont=0
    for vocal in vocales:
        for letra in fruta:
            if vocal == letra:
                cont+=1
    if cont == 2:
        return True
    else:
        return False 

lista_2_vocales = [fruta for fruta in frutas if tiene_dos_vocales(fruta)]
print(lista_2_vocales)
