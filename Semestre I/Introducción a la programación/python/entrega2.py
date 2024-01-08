"""
Juan David Bernal Maldonado, Codigo: 8977771. 
Solución a la entrega 2 introducción a la programación.
Octubre del 2022. 
"""

def loadingACargoShip(): 
    flag = True 
    flag2 = True  
    while flag == True: 
        l1 = [] 
        if flag2 == True:
            cantidadContenedores = int(input())
            flag2 = False  
        else:
            for pesoContenedores in range(cantidadContenedores): 
                pesoContenedores = int(input()) 
                l1.append(pesoContenedores)  
            pesoContenedores = input()  

            cantidadPaquetes = int(input())  
            l2 = []
        
            for pesoPaquetes in range(cantidadPaquetes): 
                pesoPaquetes = int(input())
                l2.append(pesoPaquetes) 
            pesoPaquetes = input()  

            print("Numero de contenedores: %d " % cantidadContenedores) 
            print("Capacidad de contenedores:", l1) 
            print("Cantidad de paquetes: %d " % cantidadPaquetes) 
            print("Peso de cada paquete:", l2)  
            print() 
            newInput = input() 

            if newInput == "":    
                flag = False 
            else: 
                cantidadContenedores = int(newInput) 
loadingACargoShip() 