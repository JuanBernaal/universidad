"""
Juan David Bernal
septiembre 19 del 2022

Generalidades listas
"""

#crear listas

#listas vacias
lista = [] 
lista2 = list() 

#Listas con elementos
lista3 = [3, 4, 1, "Hola", True, 30]

#para agregar elementos a la lista desde la terminal se usa lista.append("lo que se quiere agregar en la lista")
#para eliminar elementos de la lista: lista.remove(#Lo que se quiere quitar) o lista.pop(#posicion que se quiere eliminar)
#len se utiliza para saber cuantos elementos tiene una lista len(lista)

def problemaNotas(): 
    listaNotas = [] 
    suma = 0 
    
    nota = input() 
    while nota != "Fin": 
        nota = float(nota) 
        listaNotas.append(nota)
        suma += nota 
        nota = input() 
        
    promedio = suma / len(listaNotas) 
    print("El promedio de las notas es %f" % (promedio)) 
    
    i = 0 
    while i < len(listaNotas): 
        dif = listaNotas[i] - promedio 
        print("Diferencia estudiante %d: %f" % (i, dif))
        i += 1
#problemaNotas() 

def mayorElemento(lista): 
    i = 0 
    mayor = float("-inf") 
    while i < len(lista): 
        if lista[i] > mayor: 
            mayor = lista[i] 
        i += 1 
    return mayor

#print(mayorElemento([10, 8, 2, 11, 4, 7]))
#cuenta la cantidad de elementos de un dato "e" dentro de una lista
def contarOcurrencias(l, e): 
    i = 0 
    cnt = 0
    while i < len (l): 
        if l[i] == e: 
            cnt += 1
        i += 1
    return cnt 
#print(contarOcurrencias([2, 1, 4, 3, 8, 1, 4], 4))

def estaElementoposicion(l): 
    i = 0 
    ans = False 
    
    while i < len(l): 
        if l[i] == i: 
            ans = True 
        i += 1 
    return ans 

#### Tuplas
t = (3, 4, 5) 
print(len(t))   #para saber el tamaño de la tupla
#print(t{[1]}) 
#### NO se pueden agregar elementos. 
t.append(8)
#### NO se pueden cambiar los valores. 
t[0] = 10 

######## Indices negativos 
l1 = [34, 56, 89, 222, 822] 
l2 = [923, 48, 394934, 949540592, 3483439, 23223]
print(l1[-1]) 

#### Slices. 

print(l1[1:4]) #se pone entre corchetes para imprimir lo que esta entre la posicion 1 y 4 sin incluir el 4, es decir de la posicion 1 a la 3
print(l1[:3])  #Aqui si se omite el primero, python asume que empieza desde la posición(0)
print(l1[2:])  #Aqui se omite el segundo dato, por lo tanto es desde la posicion 2 hasta que la lista termina. 
print(l1[::2]) #Aqui salta la lista de 2 en dos y la imprime. 

#### Funciones sobre listas 

l1.extend([9, 11, 23]) #Se usa para añadir elementos al final de una lista  
l1.insert(3, "Tom")    #Se usa para añadir elementos a una lista, en una posicion determinada
l2.sort()              #Se usa para organizar elementos de una lista de menor a mayor 
print (l1)
print(l2)  