def sumarLista(l): 
    ans = 0
    for i in l: 
        ans += i
    return ans  

def loadingACargoShip():
    l1 = []
    l2 = []
    cantidadContenedores = input() 
    while cantidadContenedores != "":   
        cantidadContenedores = int(cantidadContenedores) 
        ans = [] 
        for lista in range(1, cantidadContenedores + 1): 
            ans.append([])                                                  #Lista que contiene cada contenedor. 
            ans[lista - 1].append(lista) 
        
        for i in range(1, cantidadContenedores + 1):
            pesoContenedores = int(input())                                 
            ans[i - 1].append(pesoContenedores)                             #Input que permite tener registro de la capacidad de los contenedores. 
            #print('contenedor %d:' % i) 
        input()
        cantidadPaquetes = int(input())

        for j in range(1 ,cantidadPaquetes + 1):                            #Tener registro de los pesos de los paquetes. 
            pesoPaquetes = int(input())  
            l2.append(pesoPaquetes) 
        input() 


        """ print("Numero de contenedores: %d " % cantidadContenedores)
        print("Capacidad de contenedores:", l1)
        print("Cantidad de paquetes: %d " % cantidadPaquetes)
        print("Peso de cada paquete:", l2) """ 
            
        """ print('Capacidad contenedores:', l1)  
        print('Peso paquetes:', l2)    
        print()     """             
        """  
        #La idea es luego hacer dos ciclos, uno que recorra la capacidad de los contenedores 
        # para asignarle cuanto recibe cada/u
        # y otro que recorra los paquetes el cual entrara dentro de las condicionales de los paquetes 
        """ 
        cantidadContenedores = input() 
    print(ans)  
loadingACargoShip()