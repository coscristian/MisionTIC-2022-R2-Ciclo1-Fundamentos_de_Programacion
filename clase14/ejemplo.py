import matplotlib.pyplot as plt


x1=[2,5,6,14]
y1= [11,22,33,44]

x2=[2,5,6,15]
y2=[4,12,18,45]

x3=list(range(16))
y3=list(map(lambda x: x**2+2*x-1, x3))

plt.plot(x1,y1,'o-', color="blue", linewidth = 3, label = 'Linea 1')
plt.plot(x2,y2, color="red", linewidth = 3, label = 'Linea 2')
#plt.plot(x3,y3,'.-', color="yellow", linewidth = 1, label = 'Linea 3')

plt.title('Dos Graficas juntas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid()
print("Hola")
plt.show()