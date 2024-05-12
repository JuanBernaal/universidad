""" 
Solución ejercicios tipo tarea 5
3, 5 de Octubre
"""
### Punto 1.

### pre-condición: l1 y l2 están ordenadas ascendentemente.
def mezclar(l1, l2): 
    i, j = 0, 0 
    ans = [] 
    
    while i < len(l1) and j < len(l2): 
        if l1[i] < l2[j]: 
            ans.append(l1[i])
            i += 1 
        else: 
            ans.append(l2[j])
            j += 1 
        
        
        #if i < len(l1): 
        while i < len(l1): 
            ans.append(l1[i])
            i += 1 
        #else: 
        while j < len(l2): 
            ans.append(l2[j])
            j += 1 
        
        return ans 
### Punto 2. 
def mayorMatriz(mat): 
    i, may = 0, float("-inf") 
    
    while i < len(mat):
        j = 0
        while j < len(mat[i]): 
            if mat [i][j] > may: 
                may = mat[i][j]
            j += 1 
        i += 1
    return may 

### Punto 3. 
def encontrarRobot(tab): 
    i = 0
    ans = None 
    while i < len(tab) and ans == None: 
        j = 0 
        while j < len(tab[i]) and ans == None: 
            if tab[i][j] == 1: 
                ans = (i, j)
            j += 1 
        i += 1 
    return ans 

def moverRobot(tab, vert, hor):
    fini, cini = encontrarRobot(tab)
    
    if vert < 0: 
        mult = -1 
    else: 
        mult = 1 
    
    k, flag = 0, True 
    while k < abs(vert) and flag: 
        r = fini + mult 
        if r >= 0 and r < len(tab) and tab[r][cini] != -1: 
            if tab[r][cini] == 0: 
                tab[r][cini] = 1 
            tab[fini][cini] = 0
            fini = r
        else: 
            flag = False 
        k += 1 
        
    if hor < 0: 
        mult = -1 
    else: 
        mult = 1 
        
    k, flag = 0, True 
    while k < abs(hor) and flag: 
        c = cini + mult 
        if c >= 0 and c < len(tab[0]) and tab[fini][c] != -1: 
            if tab[fini][c] == 0: 
                tab[fini][c] = 1 
            tab[fini][cini] = 0
            cini = c 
            
        else: 
            flag = False
        k += 1 
        
### Punto 8. 
""" 
def golesPartidos(lf, eq, ev): 
    ans = 0 
    
    for i in range(len(lf)): 
        part = lf[i] 
    if part[0] == ev and (part[1] == eq or part[2] == eq): 
        if ganadorPartido(part[1], part[2], part[3], part[4]) == eq: 
            if part[1] == eq: 
                lgoles = part[3] 
            else: 
                lgoles = part[4] 
            for j in range(len(lgoles)):
                ans += lgoles[j] 
    return ans 
""" 