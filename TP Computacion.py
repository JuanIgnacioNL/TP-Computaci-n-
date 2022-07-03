# TP-Punto 1- Crear un menú que nos permita acceder a las siguientes opciones:
# a) Calcular los valores.
# b) Graficar.
# c) Obtener binario.                                           

def main() :
    print('Bienvenido al menú de simulación de SpaceX')
    print('------------------------------------------')
    print('Por favor, seleccione que acción desea llevar a cabo')
    print('1. Calcular valores')
    print('2. Graficar valores')
    print('3. Obtener datos en binario')
    print('4. Salir')
    print('------------------------------------------')
    opc = int(input('Ingrese un numero : '))
    if opc ==1:
        uno()
        

    elif opc ==2:
        dos()
 import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  #seria el 2A
x = np.linspace(0, 2, 100) 
ax.plot(x, x,"r", label='linea') 
plt.xlabel("tiempo(dias)")
plt.ylabel("costo(USD)")
plt.title("Costo en base al tiempo")
plt.legend(loc=2)


fig, ax = plt.subplots()  #seria el 2B.
x = np.linspace(0, 2, 100)
ax.plot(x, x,"g", label='linea')  
plt.xlabel("tiempo(dias)")
plt.ylabel("riesgo(URA")
plt.title("Riesgo en base al tiempo")
plt.legend(loc=2)


fig, ax = plt.subplots()  #seria el 2C
x = np.linspace(0, 2, 100)
ax.plot(x, x,"k", label='linea')  
plt.xlabel("tiempo(dias)")
plt.ylabel("riesgo y costo")
plt.title("Velocidad")
plt.legend(loc=2)


np.random.seed(3)
x = 3 + np.arange(2)
y = np.random.uniform(2, 7, len(x))

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
        

    elif opc ==3:
        tres()    
        

    elif opc ==4:  
        exit

    else:
        print('------------------------------------------')
        print('Opción no válida, ingrese un valor entre 1 y 3.')
        print('------------------------------------------')
        main()                           #Si lo saco, no me queda un loop 
         

def uno():
    
    print('uno')#Acá se deberia unir con las funciones 
    
def dos():
    
    print('dos')#gráficos con mathplotlib
    
def tres():
    
    print('tres')#archivos pickle

main()

    
    
