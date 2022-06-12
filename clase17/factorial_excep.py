class NegativeNumberException(Exception):
    pass

def factorial(num: int):
    if not isinstance(num, int):
        raise TypeError("Solo se puede calcular el error de enteros")
    if num < 0:
        raise NegativeNumberException("No existe factorial de numeros negativos")
    resultado = 1 / 0
    while num > 1:
        resultado*=num
    return resultado

try:
    valor= 2
    result = 25 + factorial(valor)
    print(result)
except Exception as e:
    print(e)
"""except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)"""

