"""
Juan David Bernal Maldonado 
8977771 
5 de septiembre del 2022
Solución Parcial 1 
""" 
############################################# Punto 1. #############################################
"""
a. Componentes del sistema: 
    - Seguridad. 
    - Residencias. 
    - Salón Social.
    - Residentes. 
    - Administración.
    - Parqueaderos. 
b. Constantes: 
    - Cantidad de porteros cuidando la Unidad (Seguridad.)
    - Numero de residencias (Residencias)
    - Administración del conjunto residencial (Administración.)
    - Numero de parqueaderos. (Parqueaderos).
    - Ubicación del salón Social. (Salón Social). 
    - Ubicación de los parqueaderos. (Parqueaderos).
c. Variables: 
    - Cantidad de habitantes por casa. (Residentes).
    - Cantidad de Carros de residentes. (Parqueadero). 
    - Empresa de seguridad. (Seguridad).
    - Miembros de la administración. (Administración). 
    - Cantidad de Carros de los visitantes. (Parqueaderos).
    - Horarios para usar las zonas. (Salón Social, Administración.)
"""
############################################# Punto 3. #############################################

def sumarmayormenor(a, b, c, d, e): 
    ans = None 
    Mayor = None 
    Menor = None 
    if a >= b and a >= c and a >= d and a >= e: 
        Mayor = a 
    if b >= a and b >= c and b >= d and b >= e: 
        Mayor = b 
    if c >= a and c >= b and c >= d and c >= e: 
        Mayor = c 
    if d >= a and d >= b and d >= c and d >= e: 
        Mayor = d 
    if e >= a and e >= b and e >= c and e >= d: 
        Mayor = e 
    
    if a <= b and a <= c and a <= d and a <= e: 
        Menor = a 
    if b <= a and b <= c and b <= d and b <= e: 
        Menor = b 
    if c <= a and c <= b and c <= d and c <= e: 
        Menor = c 
    if d <= a and d <= b and d <= c and d <= e: 
        Menor = d 
    if e <= a and e <= b and e <= c and e <= d: 
        Menor = e 
    ans = (Mayor + Menor)
    return ans 
#print(sumarmayormenor(0, 0, 7, 0, 0))

############################################# Punto 4. #############################################

def calcularfuncion(x, y, z, w): 
    ans = None 
    if w < 1: 
        ans = ((x + 2 * z) ** y) + (x ** 2) 
    elif w == 1: 
        ans = (((3 * y) / (2 * x)) ** - 2) + ((y ** (x + 3)) - 4) 
    elif w > 1: 
        ans = (((x + y) ** 3) / ((5 * z) ** (1/2))) + 2 * y * (z ** (x + 1)) 
    return ans 
#print (calcularfuncion(1, 2, 3, 4))

############################################# Punto 5. #############################################

def escaleracartas(c1, c2, c3): 
    ans = None 
    if ((c1 + 1 == c2) or (c1 + 1 == c3)) and ((c1 + 2 == c3) or (c1 + 2 == c2)) or ((c1 - 1 == c2) or (c1 - 1 == c3)) and ((c1 - 2 == c2) or (c1 - 2 == c3)) or ((c1 - 1 == c2) or (c1 - 1 == c3)) and ((c1 + 1 == c3) or (c1 + 1 == c2)):  
        ans = True
    else: 
        ans = False 
    return ans 
#print (escaleracartas(6, 4, 5))  

############################################# punto 6. #############################################

def DeterminarCategoria(NivelEducativo, Vinculo, NumeroProyectosInvesParticipa, NumerodeAñosDespuesDR, NumArtInt, NumArtNa, NumArtconf, NTGPregrado, NTM, NTD): 
    ans = None 
    NumTotalPub = (NumArtInt + NumArtNa + NumArtconf)
    NumTesis = (NTD + NTM) 
    if Vinculo == False: 
        ans = "Sin Categoria"
    elif (NivelEducativo == "Doctorado") and ((NTGPregrado >= 5) or (NumTesis >= 5)) and (NumArtInt > 3) and (NumTotalPub > 6):
        ans = "Investigador Senior" 
    elif (NivelEducativo == "Doctorado") and (NumeroProyectosInvesParticipa >= 4) and (NumTotalPub > 8): 
        ans = "Investigador Senior" 
    elif (NivelEducativo == "Doctorado") and (NumeroProyectosInvesParticipa >= 2) and ((NumTesis >= 3) or (NTGPregrado >= 3)) and (NumTotalPub > 6): 
        ans = "Investigador Asociado"
    elif (NivelEducativo == "Doctorado") and (NumeroProyectosInvesParticipa >= 1) and (NumTotalPub > 4):
        ans = "Investigador Junior"
    elif (NivelEducativo == "Doctorado") and (NumerodeAñosDespuesDR <= 3): 
        ans = "Investigador con Doctorado"
    elif (NivelEducativo != "Doctorado"): 
        ans = "Investigador sin doctorado"
    return ans 
#print (DeterminarCategoria ("Doctorado", True, 3, 2, 7, 1, 6, 3, 5, 6)) 