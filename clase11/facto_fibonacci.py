#Haciendo el factorial de un numero usando lambda(Funcion anonima)
recursiva = lambda x: 1 if x == 0 else x * recursiva(x-1)
print(f"Factorial --> {recursiva(5)}")

#Fibonacci
recursiva = lambda x: 0 if x == 0 else 1 if x == 1 else recursiva(x-1) + recursiva(x-2)
fib = [recursiva(i) for i in range(10)]
print(f"Fibonnaci --> {fib}")