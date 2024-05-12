"""
Juan David Bernal Maldonado
Carlos Ramirez Restrepo
Solución a la tarea 5 introducción a la programación 
30 de septiembre del 2022
"""

############################################################################# Punto 1. #############################################################################

def sumasAcumuladas(l1): 
    ans = [l1[0]] 
    for i in range (1, len(l1)):  
        ans.append(l1[i] + ans[i - 1])  
    return ans 

#print(sumasAcumuladas([3, 4, 1, 7, 11])) 

############################################################################# Punto 2. ############################################################################# 



############################################################################# Punto 3. #############################################################################

def matrizPorVector(matriz, vector):
    ans = 0
    listaMatrizVector = []
    matrizVector = []
    for i in range(len(matriz)):
        # El primer for selcciona cada lista de la matriz
        for j in range(len(matriz[i])):
            # Va a cada elemento de cada lista
            ans = matriz[i][j] * vector[j]
            # multiplico cada elemento de la lista por el elemento en la misma posición del vector
            matrizVector.append(ans)
        listaMatrizVector.append(matrizVector)
        matrizVector = []
    return listaMatrizVector 
#print(matrizPorVector([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [2, 3, 4, 5]))

############################################################################# Punto 4 #############################################################################

def crearDeListaDeConteo (lPar):
    lista = []
    for i in range(len(lPar)):
        # i significa cada lista en la lista grande
        for j in range(lPar[i][1]):
            # Este ciclo es para repetir r veces(punto de la tarea donde dice v, r) el valor v en la lista que se retorna
            lista.append(lPar[i][0])
    return lista

#print(crearDeListaDeConteo([(1, 3), (12, 4), (8, 2), (9, 0), (12, 1)]))

############################################################################# Punto 5. #############################################################################
def esSubcadena(cad1, cad2):
    if cad1 in cad2:
        return True
    return False    

#print(esSubcadena("fici", "tuveunproblemadedificilsolucion"))

############################################################################# Punto 6. #############################################################################
#############################################################################    A     #############################################################################
def zlatanCine(l1): 
    l2 = [] 
    for i in range(len(l1)): 
        if l1[i][4] > l1[i][5]: 
            l2.append(l1[i][0]) 
    return l2 
"""
print(zlatanCine([["Erase una vez en Hollywood", "Quentin Tarantino",
"Humor Negro", 2016, 90, 374,
["Leonardo Di Caprio", "Brad Pitt", "Margot Robbie"]],
["Avengers Endgame", "Hermanos Russo",
"Accion", 2019, 356, 2800,
["Mark Ruffalo", "Robert Downey Jr.", "Chris Evans",
"Chris Hemsworth", "Scarlett Johansson"]],
["The wolf of wall street", "Martin Scorsese",
"Humor Negro", 2013, 100, 392,
["Leonardo Di Caprio", "Margot Robbie", "Jonah Hill"]],
["The Ladykillers", "Alexander Mackendrick",
"Humor Negro", 1955, 2, 10,
["Alec Guinness", "Herbert Lom",
"Peter Sellers", "Cecil Parker"]],
["50 First Dates", "Peter Segal",
"Comedia Romantica", 2004, 75, 120,
["Adam Sandler", "Drew Barrymore", "Rob Schneider"]],
["Titanic", "James Cameron", "Drama", 1997, 200, 1843,
["Leonardo Di Caprio", "Kate Winslet", "Billy Zane",
"Gloria Stuart"]]])) 
"""
#############################################################################    B     #############################################################################

def conteoPeliculasActor(cine):
    listaActores = []
    nombreActores = []
    numeroParticipaciones = []
    listafinal = []
    ans = 0
    for i in range(len(cine)):
        for j in range(len(cine[i][6])):
            listaActores.append(cine[i][6][j])
    for b in range(len(listaActores)):
        if not listaActores[b] in nombreActores:
            nombreActores.append(listaActores[b])
    for l in range(len(nombreActores)):
        for n in range(len(listaActores)):
            if nombreActores[l] == listaActores[n]:
                ans += 1
        numeroParticipaciones.append(nombreActores[l])
        numeroParticipaciones.append(ans)
        listafinal.append(numeroParticipaciones)
        numeroParticipaciones = []
        ans = 0
    return listafinal

""" 
print(conteoPeliculasActor([["Erase una vez en Hollywood", "Quentin Tarantino",
"Humor Negro", 2016, 90454, 374,
["Leonardo Di Caprio", "Brad Pitt", "Margot Robbie"]],
["Avengers Endgame", "Hermanos Russo",
"Accion", 2019, 356, 2800,
["Mark Ruffalo", "Robert Downey Jr.", "Chris Evans",
"Chris Hemsworth", "Scarlett Johansson"]],
["The wolf of wall street", "Martin Scorsese",
"Humor Negro", 2013, 100, 392,
["Leonardo Di Caprio", "Margot Robbie", "Jonah Hill"]],
["The Ladykillers", "Alexander Mackendrick",
"Humor Negro", 1955, 2, 10,
["Alec Guinness", "Herbert Lom",
"Peter Sellers", "Cecil Parker"]],
["50 First Dates", "Peter Segal",
"Comedia Romantica", 2004, 75, 120,
["Adam Sandler", "Drew Barrymore", "Rob Schneider"]],
["Titanic", "James Cameron", "Drama", 1997, 200, 1843,
["Leonardo Di Caprio", "Kate Winslet", "Billy Zane",
"Gloria Stuart"]]])) 
"""