""" 
Juan David Bernal Maldonado. 
8977771 
Introducción a la programación: Solución a la tarea 6. 
""" 
########################################################## Punto 3. ##########################################################

def bombearCadena(cad, d): 
    newString = "" 
    for i in cad: 
        if i in d: 
            for j in range(1, d[i] + 1):  
                newString += i  
    return newString 
#print(bombearCadena("abcagabcdf", {"a" : 3, "f" : 4, "c" : 2, "g" : 5}))  
#bombearCadena ("mmmnnpmnppqtr", {"r" : 10, "f" : 4, "c" : 2, "g" : 5})

########################################################## Punto 4. ##########################################################

def traducir(d, cad): 
    f = cad.split()
    newString = ""
    ans = None 
    for i in f[ : :1]:  
        if i in d:  
            if i == f[-1]: 
                ans = d[i] 
                newString += ans 
            else: 
                ans = d[i] 
                newString += ans 
                newString += " "
    return newString 
""" print(traducir({"ojo": "eye", "otro" : "another", "con" : "with",
"amigo" : "friend", "eso" : "that", "manito" : "little hand" }, "ojo con eso manito"))  """

########################################################## Punto 5. ##########################################################

def obtenerInversa(d): 
    ans = {} 
    for i in d: 
        for j in d[i]: 
            if j in ans: 
                ans[j].append(i) 
            else: 
                ans[j] = [i] 
    return ans 
#print(obtenerInversa({ 2 : [3, 4, 1], 4 : [5, 1, 7], 6 : [], 11 : [2, 4, 8, 10, 1] })) 

########################################################## Punto 6A. ##########################################################

def crearMatrizDispersa(mat): 
    ans = {} 
    flag = -1  
    for i in range(len(mat)): 
        ans[i] = [] 
        if i != flag: 
                t = -1  
        flag += 1 
        for j in mat[i]:
            t += 1 
            if j != 0:  
                ans[i].append((t, j)) 
        if ans[i] == []: 
            del ans[i] 
    return ans 
""" 
print(crearMatrizDispersa([[1, 0, 0, 0, 0, 4, 0, 5],
[0, 0, 0, 0, 0, 0, 4, 7],
[2, 2, 0, 0, 9, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 8, 1, 0, 7, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[3, 0, 0, 0, 0, 6, 0, 2],
[4, 4, 7, 0, 0, 0, 0, 0],
[0, 9, 0, 8, 0, 7, 0, 6]]))
""" 

########################################################## Punto 6B. ##########################################################

disp = {0 : [(0, 1), (5, 4), (7, 5)],
1 : [(6, 4), (7, 7)],
2 : [(0, 2), (1, 2), (4, 9), (6, 1)],
4 : [(2, 8), (3, 1), (5, 7)],
6 : [(0, 3), (5, 6), (7, 2)],
7 : [(0, 4), (1, 4), (2, 7)],
8 : [(1, 9), (3, 8), (5, 7), (7, 6)]} 

def obtenerValor(d, i, j): 
    l = d[i] 
    ans = 0 
    for k in range(len(l)):
        if l[k][0] == j: 
            ans = l[k][1] 
    return ans 
#print(obtenerValor(disp, 2, 4)) 

########################################################## Punto 7. ##########################################################

def organizarPalabras(cad): 
    ans = {} 
    f = cad.split() 
    for i in range (len(f)): 
        x = f[i][0] 
        ans[x] = [] 
        for j in f[i][0]: 
            for k in f[::1]: 
                if (j == x) and (k[0] == j): 
                    ans[x].append(k) 
    return ans 
#print(organizarPalabras ("mi corazón encantado vibra por el polvo de esperanza y magia del universo que ambicionan todos poseer"))