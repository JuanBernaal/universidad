""" 
Juan David Bernal Maldonado, Codigo: 8977771. 
Solución a la entrega 2 introducción a la programación.
Octubre del 2022. 
"""
"""
def sumaLista(l):
    ans = 0
    for i in l: 
        ans += i 
    return ans   

def restarLista(l1, l2):
    cont1 = 0 
    cont2 = 0
    ans = 0
    for i in range(len(l1)): 
        cont1 += l1[i] 
    for j in range(len(l2)): 
        cont2 += l2[j] 
    ans = abs(cont1 - cont2)
    return ans 
     
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
            print("cargo weight: %d" % sumaLista(l2)) 
            print("Unused weight: %d" % restarLista(l1, l2)) 
            print("Unloaded weight: %d")  
            newInput = input() 

            if newInput == "":    
                flag = False 
            else: 
                cantidadContenedores = int(newInput) 
loadingACargoShip() 
"""
#unused weight es la lista del peso de los contenedores restandole el total de paquetes




d = {1 : [1, 5, 7], 7 : [3, 6]} 
    
for i in d: 
    if len(d) >= 1:  
        if len(d[i]) >= 1: 
            d[i].append('x')  
        else: 
            d[i] = [] 
print(d)




def pruebaInput():
    capacidadContenedores = [] 
    pesoPaquetes = [] 
     
    cases = int(input())
    
    for i in range(cases): 
        x = int(input())   
        capacidadContenedores.append(x)   
    print(capacidadContenedores)        
    input()     
    cont = int(input()) 
    for j in range(cont):
        k = int(input())  
        pesoPaquetes.append(k) 
    print(pesoPaquetes) 

        
"""  
#La idea es luego hacer dos ciclos, uno que recorra la capacidad de los contenedores para asignarle cuanto recibe cada/u
# y otro que recorra los paquetes
el cual entrara dentro de las condicionales de los paquetes 
"""
pruebaInput() 