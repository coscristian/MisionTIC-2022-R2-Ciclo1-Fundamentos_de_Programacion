"""
Funciones all y any
Ejercicio 10
Se recibe una lista de números enteros separados por espacios: Si todos los enteros son positivos, se debe revisar si algún entero es un número palíndromo como se muestra a continuación https://en.wikipedia.org/wiki/Palindromic_number. Se imprime la palabra ‘True’ si se cumplen las condiciones o ‘False’ de lo contrario. Ejemplos:

Para [10, 30, 50, 90, 100, 101] imprime True
Para [10, 20, 30, 400, 50, 100] imprime False
Para [1, 2, 3, 4, 5, 6, 7, 8, 9] imprime True
Para [151, 60, -5, 135, 18, 40] imprime False"""


#Solución 1
def verificar1(lista: list) -> str: #Verifica si todos los enteros son positivos, si todos son positivos verifica si hay palindromos
    cond = []
    cond.append(len(list(filter(lambda x: x > 0, lista))) == len(lista)) #Verifico si todos son positivos
    cond.append(len(list(filter(lambda num: str(num) == str(num)[::-1], lista))) > 0 if all(cond) else False) #Si todos son positivos, verifico si hay palindromos
    return "True" if all(cond) else "False"
print(verificar1([10, 30, 50, 90, 100, 101]))

#Solución 2
def verificar2(lista: list) -> str: #Verifica si todos los enteros son positivos, si todos son positivos verifica si hay palindromos
    positivos = (list(map(lambda x: x > 0, lista))) #Verifico si los elementos son positivos
    #print(f"Positivos --> {positivos}")
    palindromos = list(map(lambda x: str(x) == str(x)[::-1],lista)) if all(positivos) else [False] #Verifico si existen palindromos
    #print(f"Palindromos --> {palindromos}")
    return "True" if any(palindromos) else "False"
print(verificar2([10, 30, 50, 90, 100, 101]))