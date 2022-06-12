#Closures (Funciones que generan otras funciones)

def construir_multiplos(factor):
    return lambda valor: valor * factor


#Tabla de multiplicación del 37
multiplos_37 = construir_multiplos(37)

lista_tabla = [multiplos_37(i) for i in range(1,11)]
print(lista_tabla)

#Forma clásica
for i in range(1,11):
  print(f"37 x {i} = {37*i}")