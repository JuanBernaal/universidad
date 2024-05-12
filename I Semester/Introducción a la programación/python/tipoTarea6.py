"""
Juan David Bernal Maldonado.
Solución Ejercicios tipo tarea 6.
"""
#### Punto 5. 
def contarOcurrencias(cad): 
	ans = {} 
	for i in range(len(cad)):  #for i in cad.  
		if cad[i] in ans: 
			ans[cad[i]] += 1 
		else: 
			ans[cad[i]] = 1 
	return ans  

######### Punto 6. 

# Solución con While 
def obtenerCostoTextoWhile(cad, d): 
    ans, i = 0, 0
    while i < len(cad): 
        for j in d: 
            if j == cad[i]: 
                ans += d[j] 
        i += 1 
    return ans 
print(obtenerCostoTextoWhile ("Tuve un problema de dificil solucion",
{"i" : 3, "o" : 2, "x" : 8, " " : 1, "p" : 5}))

#Solución con for 

def obtenerCostosTexto(cad, d): 
    ans = 0 
    for i in range(len(cad)): 
        if cad[i] in d: 
            ans *= d[cad[i]] 
    return ans 
print(obtenerCostoTextoWhile ("Tuve un problema de dificil solucion",
{"i" : 3, "o" : 2, "x" : 8, " " : 1, "p" : 5})) 
######## Punto 7. 
def listaOcurrencias(cad): 
    ans = {} 
    for i in range(len(cad)): 
        if cad[i] in ans: 
            ans[cad[i]].append(i) 
        else: 
            ans[cad[i]] = [i] 
             
    return ans  
print(listaOcurrencias ("el cielo resplandece a mi alrededor")) 