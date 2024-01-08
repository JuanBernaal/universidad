"""
Juan David Bernal Maldonado
8977771
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.   
"""

def listaSuma(l):                           #Sumar todos los elementos de una lista desde la segunda posición, ya que los dos primeros valores no se suman aquí.           
    ans = 0
    flag = True 
    for i in l[2:]:
        if flag: 
            if i == ":":
                flag = False 
            else:
                ans += i 
    return ans 

def listaSumaUnload(l):                     #Suma todos los elementos de una lista, menos los simbolos de ":"                   
    ans = 0
    for i in l:
        if i != ":":
            ans += i 
    return ans 

def listasMenorTamaño(l):           #Busca la lista de menor tamaño y devuelve su posición, si todas las listas son del mismo tamaño retorna falso. 
                                    #Si hay dos pequeñas del mismo tamaño y una grande, dentro de las pequeñas busca la que mas capacidad tenga o menor num tenga
    aux = l[0] 
    lista = []
    lista.append(aux) 
    cont = 0                        
    for i in range(len(l)):     
        if len(l[i]) < len(lista[0]):
            lista.remove(lista[0]) 
            lista.append(l[i]) 
        elif len(l[i]) == len(lista[0]) and l[i][1] > lista[0][1]: 
            lista.remove(lista[0])
            lista.append(l[i]) 
        elif len(l[i]) == len(aux):
            cont += 1 
    if cont == len(l): 
        return False 
    else:                                   #Evitar retornar dos valores distintos dentro de una función. 
        return lista

def obtenerPosición(l, l1):         #Recibe una lista de listas y una lista, busca la lista en la lista de listas 
    ans = None  
    for i in range(len(l)):
        if i != ":":
            if l[i] == l1[0]:
                ans = i 
    return ans 

def obtenerCapacidades(l):          #Mete en una lista las capacidades de todos los contenedores
    ans = []
    for i in range(len(l)): 
        ans.append(l[i][1]) 
    return ans 

def obtenerMayorCapacidad(l):       #Retorna la posición de los contenedores que mayor capacidad tienen. 
    l = obtenerCapacidades(l) 
    ans = 0 
    aux = 0 
    for i in range(len(l)):
        if i != ":":
            if l[i] > aux: 
                aux = l[i] 
                ans = i 
    return ans 

def ultimaCondicion(l, num):        #Recibe una lista y un numero, revisa si el numero puede entrar a la lista  
    flag = True 
    flag1 = True 
    for i in range(len(l)): 
        if flag1:
            if l[i] == ":":
                flag1 = False 
            if flag:
                if (listaSuma(l[i]) + num) < l[i][1]:                   #Si el peso de todo lo de la lista + el numero ingresado es menor a la capacidad disponible, entonces se puede añadir el valor 
                    flag = False 
                    l[i].append(num)
                    actualizarCapacidades(l, i)             
    return l 
#print(ultimaCondicion([[1, 342, 5], [2, 4, 3], [3, 456, 7]], 222))  
#print(ultimaCondicion([[1, 3, 5], [2, 4, 3], [3, 6, 7]], 222))  
def actualizarCapacidades(l, pos):                 #Actualiza los valores de las capacidades de cada contenedro cuando se les mete un valor. 
    if l[pos][1] - l[pos][-1] >= 0:
        l[pos][1] = l[pos][1] - l[pos][-1] 
    return l 
#print(actualizarCapacidades([[1, 45, 6], [2, 45, 6], [3, 45, 9, 0], [4, 45, 3, 7]], 3))
def generarMatrix(l):
    k = []
    for i in l:
        k.append(len(i))
    columnas = max(k) - 2     #Determina cuantos datos hacia arriba tendra el codigo 
    filas = l[len(l) - 1][0]  #Determina el tamaño de la matriz horizontal 

    lista1 = []
    fila = []
    for i in range(columnas):     #Genera una matriz con el simbolo de ":" y luego hay que reemplazar esos valores
        for j in range(filas): 
            fila.append(":")
        lista1.append(fila)
        fila = []
    return lista1
cargo = [] 
def leerImprimir2(l):
    lista1 = generarMatrix(l)

    for i in l:
        if len(i) > 2:  #Sirve para saber si se tiene que reemplazar mas de un numero dentro de la "generar matriz" (Lista 1). 
            flag = True
            while flag == True:
                for j in range(1, len(l) + 1): 
                    if j + 1 < len(i):             # Este confirma que se pueda hacer lo que esta en la linea 117:[i[j + 1] ] para que no ocurra el error index out of range
                        filaMatriz = len(lista1) - j        #Valor de la fila que se tiene que cambiar
                        columnaMatriz = i[0] - 1            
                        lista1[filaMatriz][columnaMatriz] = i[j + 1] 

                else:
                    flag = False              
    formato = []
    indicadores = []

    for i in range(len(lista1[0])):             #Tamaño de formatos e idincadores, formato son los "=", indicadores(los numeros de los cont)
        indicadores.append(i + 1)

    for i in range(len(l) * 2 - 1):             #Imprimir los "="
        formato.append("=")

    for i in range(len(lista1)):
        for j in range(len(lista1[0])):           #Para imprimir la matriz
            print(lista1[i][j], end=" ")          #Los end se utlizan para los espacios entre caracteres
        print()

    for i in range(len(formato)):
        print(formato[i], end="")                 #Esto reconoce el final de la matriz para no imprimir un espacio de más 
    print()
    for i in range(len(indicadores)):             #Imprime los indicadores(numeros de contenedores)
        print(indicadores[i], end=" ")
    print() 
    print()
    #return 

def loadingACargoShip():
    flag = True
    cantidadContenedores = input()
    unloaded = []  
    cargo = [] 
    while cantidadContenedores != "":   
        cantidadContenedores = int(cantidadContenedores) 
        ans = [] 
        
        for lista in range(1, cantidadContenedores + 1): 
            ans.append([])                                                  #Lista que contiene cada contenedor en la posición 0. 
            ans[lista - 1].append(lista) 
        
        for i in range(1, cantidadContenedores + 1):
            pesoContenedores = int(input())                                 
            ans[i - 1].append(pesoContenedores)                             #Input que permite tener registro de la capacidad de los contenedores en la posición 1. 
            #print('contenedor %d:' % i) 
        input()

        cantidadPaquetes = int(input())  
       
        for j in range(1 ,cantidadPaquetes + 1):                            #Tener registro de los pesos de los paquetes. 
            pesoPaquetes = int(input())  
            cargo.append(pesoPaquetes)  
            aux = ans 
            if flag == True:
                primeraCondicion = listasMenorTamaño(ans) 
                segundaCondicion = obtenerMayorCapacidad(aux)                         
                if primeraCondicion != False:
                    x = obtenerPosición(ans, primeraCondicion)  
                    if ans[x][1] - pesoPaquetes >= 0: 
                        ans[x].append(pesoPaquetes) 
                        actualizarCapacidades(ans, x) 
                    else: 
                        ans[x].append(":") 
                        flag = False 
                        unloaded.append(pesoPaquetes)
                elif primeraCondicion == False:  
                    if ans[segundaCondicion][1] - pesoPaquetes >= 0:     
                        ans[segundaCondicion].append(pesoPaquetes)
                        actualizarCapacidades(ans, segundaCondicion)      
                    else:
                        ans[segundaCondicion].append(":")
                        flag = False
                        unloaded.append(pesoPaquetes) 
                else:
                    if ultimaCondicion(ans, pesoPaquetes) == True:
                        ans[0].append(":") 
                        flag = False 
                        unloaded.append(pesoPaquetes)                 
            else:
                unloaded.append(pesoPaquetes) 

        #listaSumaUnload(unloaded)          
        input() 
        leerImprimir2(ans) 
        print('cargo weight:', listaSumaUnload(cargo)) 
        print('unused weight:', listaSumaUnload(obtenerCapacidades(ans))) 
        print('unloaded weight:', listaSumaUnload(unloaded))  
        print()  
        #print(ans)      
        #print('Unloaded:', unloaded) 
        flag = True 
        unloaded = []  
        cargo = []   
        cantidadContenedores = input() 
loadingACargoShip() 