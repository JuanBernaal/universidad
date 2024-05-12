"""
Juan David Bernal Maldonado. 
8977771 
Octubre-Noviembre del 2022 
"""

###################################################### punto 1. ###################################################### 

def obtenerElementos(l):
    conjunto = set() 
    for i in range(len(l)): 
        for j in l[i]: 
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

###################################################### Punto 2. ###################################################### 

def esPangrama(cad): 
    ans = False
    conjunto = set() 
    abecedarioSet = {'a', 'b', 'c', 'd', 'e', 
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'ñ',
    'o', 'p', 'q', 'r', 's', 
    't', 'u', 'v', 'w', 'x', 
    'y', 'z'} 
    cad = cad.lower()  
    for i in cad: 
        if i in abecedarioSet: 
            conjunto.add(i)  
        if len(conjunto) == 27:
            ans = True  
    return ans 
#print(esPangrama ("si tu lo deseas puedes volar solo tienes que confiar mucho en mi ..."))  
#print(esPangrama ("Un jugoso zumo de piña y kiwi bien frio es exquisito y no lleva alcohol."))
#print(esPangrama("El baño de wolframio de un equipo de rayos X es capaz de generar unas horas de kilovoltaje"))
#print(esPangrama("Beber whisky por la mañana afloja vergonzantemente al que se excede.")) 

###################################################### Punto 3(a). ###################################################### 

cursos = {"Introducción a la Programación" :
[["Pepito Perez", "892324", 4.0] ,
["Rivaldo Rodriguez", "434335", 4.3] ,
["Novita Caicedo", "442565", 3.4] ,
["Manuela Beltran", "2323232", 4.1]] ,
"Matemáticas" :
[["Pepito Perez", "892324", 4.0] ,
["Ruperto Gutierrez", "111335", 4.3] ,
["Lupita Gallego", "789232", 4.8] ,
["Novita Caicedo", "442565", 3.4]] ,
"Humanidades" :
[["Eric Cartman", "343422", 2.0] ,
["Stan Marsh", "22999", 3.3] ,
["Novita Caicedo", "442565", 3.4]]}

def obtenerEstudiantes(d): 
    ans = [] 
    conjunto = set() 
    for i in d:
        for j in range(len(d[i])): 
            conjunto.add(d[i][j][0]) 
            ans = list(conjunto) 
    return ans 

#print(obtenerEstudiantes(cursos)) 

###################################################### Punto 3(b). ######################################################

def estudiantesEnComun(d, curso1, curso2):
    aux = set()
    conjunto = set() 
    for i in range (len(d[curso1])):   
        aux.add(d[curso1][i][0]) 
    for j in range(len(d[curso2])):
        estudiante = d[curso2][j][0] 
        if estudiante in aux: 
               conjunto.add((estudiante, d[curso2][j][1]))  
    conjunto = list(conjunto)
    return conjunto  

#print(estudiantesEnComun(cursos, "Introducción a la Programación", "Matemáticas")) 

###################################################### Punto 4(a). ###################################################### 

profCursos = {"Maestro Roshi" : ["Introducción a la Programación",
"Matemáticas"],
"Maestro Kaiosama" : ["Introducción a la Programación",
"Estructuras de Datos",
"Árboles y Grafos"], 
"Bills" : ["Física Cuántica", "Análisis y Diseño de Algoritmos",
"Diseño e Implementación de Algoritmos"]} 

def cambiarDict(d):
    dic = {}  
    for i in d:  
        for j in d[i]:   
            if j in dic: 
                dic[j].append(i)
            else:
                dic[j] = []   
                dic[j].append(i)      
    return dic 
#print(cambiarDict(profCursos))  

def profesoresParaCurso(d, curso):
    dic = cambiarDict(d) 
    return dic[curso] 
#print(profesoresParaCurso (profCursos , "Física Cuántica")) 

###################################################### Punto 4(b). ######################################################

def estudiantesConProfesor(dEstudiantes, dProfes, profesor): 
    conjunto = set() 
    if profesor in dProfes:
        for i in dProfes[profesor]:
            if i in dEstudiantes:
                for j in range(len(dEstudiantes[i])): 
                    conjunto.add(dEstudiantes[i][j][0]) 
    conjunto = list(conjunto) 
    return conjunto
print(estudiantesConProfesor(cursos, profCursos ,"Bills"))    

###################################################### Punto 5. ######################################################

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
