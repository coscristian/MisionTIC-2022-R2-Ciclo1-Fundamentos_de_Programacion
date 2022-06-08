#Ejercicio 1
#Necesitamos crear una lista de enteros que contenga la longitud de cada palabra en una frase, pero solo si la palabra no es "el".  
#La frase es: `"el rápido zorro marrón salta sobre el perro perezoso"`

#Método clásico
frase = "el rápido zorro marrón salta sobre el perro perezoso"

lista_longitud_palabras = []
for palabra in frase.split():
    if palabra != "el":
        lista_longitud_palabras.append(len(palabra))
print(lista_longitud_palabras)

#Usando list comprehension
lista = [len(palabra) for palabra in frase.split() if palabra != "el"]
print(lista)
