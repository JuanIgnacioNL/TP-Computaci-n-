import math                                      
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
         

import math                                      
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
    def costo_vuelo(dic,costo,tiempo):
        print(dic)
        costo_total=costo/(30+tiempo)
        print("El costo de vuelo en funcion del tiempo es:",costo_total,"millones de USD.")
    def riesgo(dic,capa_comb,masa,dist_opt,tiempo):
        k=capa_comb/(masa*dist_opt)
        riesgo=math.e**(tiempo*k)
        print("El riesgo en funcion del tiempo de vuelo es:",riesgo)
    def menu():
        dic={}
        lista=[]
        with open ("prototipos.csv","r") as archivo: 
            next(archivo)
            for linea in archivo:
                linea=linea.rstrip("\n")
                lista=linea.split(",")
                nombre=lista[0].lower()
                masa=int(lista[1].lower())
                capa_comb=int(lista[2].lower())
                costo=int(lista[3].lower())
                vel_max=int(lista[4].lower())
                dist_opt=int(lista[5].lower())
                dic={"nombre":nombre,"masa":masa,"capacidad de combustible":capa_comb,"constante de costo":costo,"velocidad maxima soportada":vel_max,"distancia optima":dist_opt}
                print(dic)
                tiempo=int(input("Ingrese el tiempo de vuelo:\n"))
                costo_vuelo(dic,costo,tiempo)
                riesgo(dic,capa_comb,masa,dist_opt,tiempo)
     
    
def dos():
    
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()  
    x = np.linspace(0, 2, 100) 
    ax.plot(x, x,"r", label='linea') 
    plt.xlabel("tiempo(dias)")
    plt.ylabel("costo(USD)")
    plt.title("Costo en base al tiempo")
    plt.legend(loc=2)


    fig, ax = plt.subplots()  
    x = np.linspace(0, 2, 100)
    ax.plot(x, x,"g", label='linea')  
    plt.xlabel("tiempo(dias)")
    plt.ylabel("riesgo(URA")
    plt.title("Riesgo en base al tiempo")
    plt.legend(loc=2)

    
def tres():
        archivo_binario = open("distancias.pickle", "w")
        distancia_actual = archivo_binario.tell()
        print("la distancia actual es", "distancia_actual")
        datos = archivo_binario.read(3)
        print("el contenido de los 3 bytes es:",(datos))
        print("el tipo de datos es:", type(datos))
        distancia_actual = archivo_binario.tell()
        print("la distancia")
        filas = int(input("introduce distancias:"))
        columnas = int(input("introduce lugar"))
        matriz = []
        for i in range(filas):
            matriz.append ([0] * columnas)
        for i in range(filas):
            for j in range (columnas):
                matriz [i][j] = float(input("Fila {}, columna {}:". format))
        archivo = "distancia.pickle"
        CAMPOS = ("Distancias","Lugar")
        def cargar_distancia(archivo):
            distancia = ()
            if os.path.exists(archivo):
                with open(archivo) as f:
                    datos_csv = csv.reader(f)
                    encabezado = next(datos_csv)
                    for item in datos_csv:
                        distancia.pickle.append(item)
        def guardar_distancia(distancia, archivo):
   

main()

    
    
