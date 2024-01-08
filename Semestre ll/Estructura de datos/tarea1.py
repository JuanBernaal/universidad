""" 
Juan David Bernal Maldonado 8977771
Segundo semestre
Estructuras de datos, solucion a la tarea 1 
"""

################################################################## Punto 1. ##################################################################

mat = [[11, 23, 76, 34, 11],
[14, 30, 92, 30, 101],
[12, 45, 58, 92, 22],
[74, 56, 49, 56, 100],
[99, 5, 28, 47, 99]]  

def verificarDiagonales(matriz):
    ans = True 
    lista = [] 
    lista1 = [] 

    for i in range(len(matriz)): 
        lista.append(matriz[i][i]) 
        lista1.append(matriz[i][-i -1]) 

    if lista1 != lista:
        ans = False 
    
    return ans 

#print(verificarDiagonales(mat))  

################################################################## Punto 2. ################################################################## 

def esCapicua(lista):
    ans = True 
    lista1 = []
    
    for i in range(1, len(lista) + 1):
        lista1.append(lista[-i])  
    
    if lista1 != lista:
        ans = False

    return ans 

#print(esCapicua([42, 12, 90, 90, 12, 42]))
#print(esCapicua([42, 12, 90, 90, 12, 45]))  

################################################################## Punto 3A. ################################################################## 

def diferenciaListas(listaA, listaB): 
    lista = []

    for i in listaA:
        if i not in listaB:
            lista.append(i) 
        else:
            listaB.remove(i) 
    
    return lista 

#print(diferenciaListas([40, 10, 22, 12, 33, 33, 33], [41, 22, 31, 15, 13, 12, 33, 19]))  
#print(diferenciaListas([41, 22, 31, 15, 13, 12, 33, 19], [40, 10, 22, 12, 33, 33, 33]))

################################################################## Punto 3B. ##################################################################

def leerImprimir(lista1):
    for i in range(len(lista1)): 
        if lista1[i] == lista1[-1]:
            print(lista1[i]) 
        else:
            print(lista1[i], end = ", ") 
 
def main():
    lista = []
    for _ in range(int(input())): 
        v1 = input().split()
        v2 = input().split()
        for j in range(1, len(v1)): 
            if v1[j] not in v2:
                lista.append(v1[j])  
            else:
                v2.remove(v1[j])  
        leerImprimir(lista)
        lista = [] 
#main()  

################################################################## Punto 4. ##################################################################

def esPrimo(num):
    ans = True 
    for i in range(2, num):
        if num % i == 0:
            ans = False 
    return ans 

def sumaDigitos(num):
    ans = 0
    x = str(num) 
    if len(x) == 1:
        return num 
    else: 
        for i in x:
            ans += int(i)
        return ans 

def mostrarPrimos(numero):
    lista = [] 
    lista2 = [] 
    for i in range(2, numero):
        if esPrimo(i) == True:
            lista.append(i)
    #leerImprimir        
    print("Números primos entre 1 y %d:" % numero) 
    for j in range(len(lista)):
        if lista[j] != lista[-1]:
            print("--> %d," % lista[j])   
        else:
            print("--> %d" % lista[j])
        x = sumaDigitos(lista[j]) 
        if esPrimo(x) == True:
            lista2.append(lista[j])   
    print() 
    print("Números entre 1 y %d con suma de dígitos con valor primo:" % numero)
    for k in lista2:
        if k == lista2[-1]:
            print(k) 
        else:
            print(k, end = ", ") 
#mostrarPrimos(100) 

################################################################## Punto 5. ##################################################################

disp = {0 : [(0, 1), (5, 4), (7, 5)],
1 : [(6, 4), (7, 7)],
2 : [(0, 2), (1, 2), (4, 9), (6, 1)],
4 : [(2, 8), (3, 1), (5, 7)],
6 : [(0, 3), (5, 6), (7, 2)],
7 : [(0, 4), (1, 4), (2, 7)],
8 : [(1, 9), (3, 8), (5, 7), (7, 6)]} 

lista1 = [(0, 0), (8, 3), (3, 5), (7, 2), (4, 3), (4,6)]

def encontrarValor(lista, num): 
    for i in range(len(lista)):
        if lista[i][0] == num:
            return lista[i][1] 

def sumarValoresMat(disp, lista):
    ans = 0
    for i in lista:
        if i[0] in disp:
            lista1 = disp[i[0]] 
            x = encontrarValor(lista1, i[1])
            if x != None:
                ans += x 
    return ans 

#print(sumarValoresMat(disp, lista1)) 
