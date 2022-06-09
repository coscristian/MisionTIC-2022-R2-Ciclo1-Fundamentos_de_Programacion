from functools import reduce 

# Utilice map() para imprimir el cuadrado de cada número redondeado
# a tres lugares decimales
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
map_result = list(map(lambda x: round(x**2, 3), my_floats)) 
print(f"Cuadrado de cada numero redondeado a 3 decimales --> {map_result}")

# Utilice filter() para imprimir solo los nombres que sean menores
# o iguales a siete letras
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filter_result = list(filter(lambda name: len(name) <= 7, my_names)) 
print(f"Nombres con longitud de caracteres menor o igual a 7 letras --> {filter_result}")


# Utilice reduce() para imprimir el producto de estos números
my_numbers = [4, 6, 9, 23, 5]
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers) 
print(reduce_result)