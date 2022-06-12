"""Extraiga en un conjunto los dígitos que existen en una frase. La frase es `"Hello 12345 World 5602"`"""

frase = "Hello 12345 World 5602"
#Si el caracter no es un espacio y no es una letra, entonces tome el caracter(Sería un digito)
digitos = {char for char in frase if char != " " and not char.isalpha()}
print(digitos)