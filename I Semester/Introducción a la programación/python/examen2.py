""" 
Juan David Bernal Maldonado.
Solución al Parcial 2: Introducción a la programación. 
profesor: Carlos Ramirez Restrepo. 
10 de Octubre del 2022.
""" 
######################################################## Punto 1. ########################################################

def obtenerDivisores(n): 
    l1 = [] 
    for i in range(1, n + 1):
        if n % i == 0: 
            l1.append(i) 
    return l1 
#print(obtenerDivisores(100)) 

######################################################## Punto 2. ########################################################

""" def unir(cad1): 
    cad1 = []
    for i in range(len(cad1)):  
        print(cad1[i])       
    return cad1 
"""
def unir(cad1):  
    newString = cad1.split() 
    i = 0
    ans = 0 
    while i < len(cad1):  
        ans = (cad1[i])  
        i += 1       
    return ans 

print(unir(["America", "perdio ,", "Cali", "gano.", "El", "profesor", "esta", " triste."])) 

""" 
a = ["America", "perdio ,", "Cali", "gano.", "El", "profesor", "esta", " triste."] 
print(a[0]) and print(a[]) 
"""

######################################################## Punto 3. ######################################################## 

""" def estaContenido(cad1, cad2):
    cad1 = "vromeo"
    result = cad1.split()
    return result """
"""     
def estaContenido(cad1, cad2):
    cont = 0
    flag = None 
    newString = cad1.split()
    for i in range(len(cad1)):
        newString = cad1[i] 
        for j in range(len(cad2)): 
            if newString == cad2 
"""
"""             
        if newString in cad2: 
            cont += 1 
        if cont == len(cad1): 
            flag = True 
        if cont > len(cad1): 
            flag = False 
        else: 
            flag = False 
    return flag  
"""
#print(estaContenido("vromeo", "tuveunproblemadedificilsolucion")) 

""" 
cad1 = "Profe por qué tiro tan duro con el parcial"
result = cad1.split()
#print(result)  
"""


""" def estaContenida(cad1, cad2):
    if cad1 in cad2: 
        return True
    return False  
#print(estaContenida("vromeo", "tuveunproblemadedificilsolucion"))  """
        
######################################################## Punto 4. ########################################################


######################################################## Punto 6. ########################################################
""" 
def leerNumeros(): 
    num = input() 
    cantidadImpares = 0
    sumMultiplos5 = 0
    numEntre10y20 = 0
    cantidadDatos = (cantidadImpares + sumMultiplos5 + numEntre10y20)
    tupla = (cantidadDatos, cantidadImpares, sumMultiplos5, numEntre10y20)  
    while num != "Fin": 
        if num % 3 == 0:   
            cantidadImpares += 1 
        if num % 5 == 0: 
            sumMultiplos5 += num 
        if num > 10 and num < 20: 
            numEntre10y20 += 1 
    return tupla 
leerNumeros() 
"""
