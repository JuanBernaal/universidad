""" def inputPrueba(numCont, paquetes): 
    d = {} 
    
    for i in range(1, numCont + 1):  
        d[i] = ""  
        if d[i] == []:
            d[i].append(paquetes) 
        else:
            d[i] = []  
        d[i].append(paquetes) 
    print(d) 
inputPrueba() 
"""
def loadingACargoShip():
    d = {} 
    l1 = []
    l2 = []
    cantidadContenedores = input() 
    while cantidadContenedores != "":
        cantidadContenedores = int(cantidadContenedores)
        for i in range(1, cantidadContenedores + 1):
            pesoContenedores = int(input())
            l1.append(pesoContenedores)
            #print('contenedor %d:' % i) 
        input()

        cantidadPaquetes = int(input())

        for j in range(1 ,cantidadPaquetes + 1): 
            pesoPaquetes = int(input())
            l2.append(pesoPaquetes)
        input()

        if len(d) >= 1:  
            if len(d[i]) >= 1:  
                d[i].append(j) 
            else: 
                d[i] = []
            
        print() 
        cantidadContenedores = input() 
loadingACargoShip()