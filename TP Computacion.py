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

    
    
