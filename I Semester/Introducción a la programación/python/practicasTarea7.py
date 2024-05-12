def obtenerElementos(l):
    conjunto = set() 
    for i in range(len(l)): 
        for j in l:  
            for k in l[i + 1:]:
                for p in k: 
                    if p == j: 
                        conjunto.add(p)   
    conjunto = list(conjunto) 
    return conjunto 
#print(obtenerElementos([[2, 1, 8, 4], [1, 5, 3], [2, 6, 7], [8, 9]])) 
#print(obtenerElementos([[4, 1, 8, 4], [1, 5, 3], [2, 6, 7], [4, 8, 9]]))
#print(obtenerElementos([[2, 1, 8, 4], [1, 5, 3], [2, 6, 7], [8, 9]]))
#print(obtenerElementos([[3], [4], [4], [3]]))  

def obtenerElementos3Listas(l1, l2, l3): 
    ansSet = set() 
    #Opción 1: 
    for i in l1: 
        for j in l2: 
            if i == j: 
                ansSet.add("Opción 1")   
    #Opción 2: 
    for i in l1: 
        for j in l3: 
            if i == j:            
                ansSet.add('Opción 2') 
    #Opción 3: 
    for i in l2: 
        for j in l3: 
            if i == j:
                ansSet.add('Opción 3') 
    return ansSet 
#print(obtenerElementos3Listas([2, 5], [4, 5], [5, 8]))

def convertirListaEnteros(l):  
    ans = [] 
    for i in range(len(l)): 
        f = int(l[i])  
        ans.append(f)  
    return ans 

def UVa13037():  
    cases = input() 
    lista = [] 
    while cases != "": 
        input()       
        cases = int(cases)   
        listaL = input() 
        listaL = listaL.split() 
        listaL = convertirListaEnteros(listaL)
        lista.append(listaL) 
        listaR = input() 
        listaR = listaR.split() 
        listaR = convertirListaEnteros(listaR) 
        lista.append(listaR)  
        listaS = input() 
        listaS = listaS.split() 
        listaS = convertirListaEnteros(listaS)
        lista.append(listaS)
        #print(listaL)
        #print(listaR)
        #print(listaS)   
        lista = obtenerElementos(lista) 
        print(lista)   
        for case in range(1, cases + 1):  
            print("Case #%d" % case) 
            print(obtenerElementos3Listas(listaL, listaR, listaS), obtenerElementos(lista))     
        cases = input()     
UVa13037()    