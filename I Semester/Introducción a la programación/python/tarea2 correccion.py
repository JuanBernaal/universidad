"""
Juan David Bernal Maldonado. 
Codigo: 8977771
Tarea 2: Introducción a la programación.
"""
from math import pi 
############################################################ Punto 1: ################################################################
def funcion2 (x, y, z, w):
    a = (x - 2) ** (z + 1)
    b = (4 * y) ** (4 * z)
    c = (7 * x ** (y - 1))
    d = ((x + 3) ** (1/2)) / 4
    e = (z ** 4) * (w ** (y + x)) * (x ** 3)
    funcion = (a * b + c - d - e + 6)
    return funcion
#funcionprueba = funcion2 (1, 0, 2, 3)
#print (funcionprueba)
############################################################ Punto 2: ##################################################################
"""
Volumen de (V) un Cilindro: V = pi * (r ** 2) * h.
Volumen (V) de un Cono: V = (pi * (r ** 2) * h) / 3.
Volumen (V) de una Esfera: V = 4/3 * pi * r ** 3. 
"""
#r = Radio.
#h = Altura. 
#ci = Cilindro.
#co = Cono.
#es = Esfera. 
def volumencilindro(rci, hci):
    f = (pi * (rci ** 2) * hci)
    return f 

#print (volumencilindro(1.8, 4.1))
def volumencono(rco, hco):
    g = ((pi * (rco ** 2) * hco) / 3)
    return g 

#print (volumencono(3, 4)) 
def volumenesfera(res):
    h = (4/3 * pi * res ** 3)
    return h 

#print (volumenesfera(1)) 
############################################################ punto 3. ###################################################################
def sumarMayorMenor(a, b ,c, d, e): 
    menor = None 
    mayor = None
    if a <= b and a <= c and a <= d and a <= e: 
        menor = a 
    elif b <= a and b <= c and b <= d and b <= e: 
        menor = b
    elif c <= a and c <= b and c <= d and d <= e: 
        menor = c 
    elif d <= a and d <= b and d <= c and d <= e: 
        menor = d 
    elif e <= a and e <= b and e <= c and e <= d: 
        menor = e
    if a >= b and a >= c and a >= d and a >= e: 
        mayor = a 
    elif b >= a and b >= c and b >= d and b >= e:
        mayor = b 
    elif c >= a and c >= b and c >= d and c >= e:
        mayor = c 
    elif d >= a and d >= b and d >= c and d >= e: 
        mayor = d  
    elif e >= a and e >= b and e >= c and e >= d:   
        mayor = e  
    suma = (mayor + menor) 
    return suma 
#print (sumarMayorMenor(1, 2, 3, 6, 7))
############################################################ punto 4. ##################################################################
def cuadrante(x, y): 
    ans = 0
    if x > 0 and y > 0: 
        ans = 1
    elif x < 0 and y > 0:
        ans = 2 
    elif x < 0 and y < 0: 
        ans = 3 
    elif x > 0 and y < 0: 
        ans = 4 
    return ans 
print (cuadrante(-5,-2)) 
############################################################ punto 5. ############################################################
def cuantosencuadrante(x1, y1, x2, y2, x3, y3, x4, y4, c): 
    c1 = 0 
    c2 = 0
    c3 = 0
    c4 = 0
    if x1 > 0 and y1 > 0: 
        c1 += 1
    if x2 > 0 and y2 > 0: 
        c1 += 1 
    if x3 > 0 and y3 > 0: 
        c1 += 1 
    if x4 > 0 and y4 > 0: 
        c1 += 1 
    if x1 < 0 and y1 > 0: 
        c2 += 1
    if x2 < 0 and y2 > 0: 
        c2 += 1
    if x3 < 0 and y3 > 0: 
        c2 += 1
    if x4 < 0 and y4 > 0: 
        c2 += 1
    if x1 < 0 and y1 < 0: 
        c3 += 1 
    if x2 < 0 and y2 < 0:
        c3 += 1
    if x3 < 0 and y3 < 0: 
        c3 += 1 
    if x4 <0 and y4 < 0:
        c3 += 1
    if x1 > 0 and y1 < 0:
        c4 += 1
    if x2 > 0 and y2 < 0: 
        c4 += 1 
    if x3 > 0 and y3 < 0: 
        c4 += 1 
    if x4 > 0 and y4 < 0:
        c4 += 1
    if c == 1: 
        c = c1 
    elif c == 2:
        c = c2 
    elif c == 3: 
        c = c3
    elif c == 4: 
        c = c4
    return c

def cuantosEnCuadrante(x1, y1, x2, y2, x3, y3, x4, y4, c):
    ans = 0
    if cuadrante(x1, y1) == c:
        ans += 1
    if cuadrante(x2, y2) == c:
        ans += 1
    if cuadrante(x3, y3) == c:
        ans += 1
    if cuadrante(x4, y4) == c:
        ans += 1
    return ans

#print (cuantosencuadrante(2, 3.4, 3, 1, -2.1, -3, -4, 1, 1))   
############################################################ punto 6. ###################################################################
A = 1 
J = 11 
Q = 12 
K = 13 
def póquer (a, b, c, d, e): 
    poquer = True 
    comb = None 
    if (a == b) and (a == c) and (a == d):  
        comb = poquer 
    elif (a == b) and (a == c) and (a == e): 
        comb = poquer 
    elif (a == b) and (a == d) and (a == e): 
        comb = poquer 
    elif (a == c) and (a == d) and (a == e): 
        comb = poquer 
    elif (b == c) and (b == d) and (b == e): 
        comb = poquer       
    else: 
        comb = False 
    return comb 
#print (póquer(K, K, K, K, J)) 

############################################################ punto 7. #################################################################
def partdiotenis (name1, set1, set2, set3, set4, set5, name2, set6, set7, set8, set9, set10): 
    p1 = 0
    p2 = 0
    if (set1 == 6 or set1 == 7) and (set6 <= 4 or set6 == 5): 
        p1 += 1 
    else: 
        p2 += 1
    ####
    if (set2 == 6 or set2 == 7) and (set7 <= 4 or set7 == 5):
        p1 += 1 
    else: 
        p2 += 1
    ###
    if (set3 == 6 or set3 == 7) and (set8 <= 4 or set8 == 5):
        p1 += 1
    else: 
        p2 += 1
    ###
    if (set4 == 6 or set4 == 7) and (set9 <= 4 or set9 == 5):
        p1 += 1
    else: 
        p2 += 1
    ###
    if (set4 == 6 or set4 == 7) and (set9 <= 4 or set9 == 5):
        p1 += 1
    else: 
        p2 += 1
    ###
    if (set5 == 6 or set5 == 7) and (set10 <= 4 or set10 == 5):
        p1 += 1
    else: 
        p2 += 1
    
    if p1 >= 3:
        winner = name1
    elif p2 >= 3: 
        winner = name2
    
    return winner 
#print (partdiotenis("Juan", 6, 6, 2, 1, 4, "David", 2, 4, 6, 6, 6))

############################################################ punto 8. #################################################################
def dietaZlatan (entrada, pentrada, centrada, proteina, pproteina, cproteina, ensalada, pensalada, censalada, sopa, psopa, csopa):
    ans = None 
    totalcalorias = (centrada + cproteina + censalada + csopa)
    pesototal = (pentrada + pproteina + pensalada + psopa)
    porcentaje = pesototal * 0.6 
    if proteina == "carne desmechada": 
        ans = True 
    elif totalcalorias < 500: 
        ans = True 
    elif (totalcalorias >= 500 and totalcalorias < 700) and (pesototal < 325 and pensalada >= 100): 
        ans = True 
    elif porcentaje > pesototal * 0.4:  
        ans = True 
    else: 
        ans = False
    return ans 
#print (dietaZlatan("pastas", 50, 30, "carne desmechada", 40, 20,"Salad", 70, 45,"Sancocho", 60, 73)) 

############################################################ punto 9. #################################################################
def ajedrez (prx, pry, ppx, ppy): 
    ans = None  
    if (prx == ppx) or (pry == ppy):  
        ans = True
    elif (prx + 1 == ppx and pry + 1 == ppy) or (prx + 2 == ppx and pry + 2 == ppy) or (prx + 3 == ppx and pry + 3 == ppy) or (prx + 4 == ppx and pry + 4 == ppy) or (prx + 5 == ppx and pry + 5 == ppy) or (prx + 6 == ppx and pry + 6 == ppy) or (prx + 7 == ppx and pry + 7 == ppy):
        ans = True 
    elif (prx + 1 == ppx and pry - 1 == ppy) or (prx + 2 == ppx and pry - 2 == ppy) or (prx + 3 == ppx and pry - 3 == ppy) or (prx + 4 == ppx and pry - 4 == ppy) or (prx + 5 == ppx and pry - 5 == ppy) or (prx + 6 == ppx and pry - 6 == ppy) or (prx + 7 == ppx and pry - 7 == ppy):
        ans = True 
    elif (prx - 1 == ppx and pry - 1 == ppy) or (prx - 2 == ppx and pry - 2 == ppy) or (prx - 3 == ppx and pry - 3 == ppy) or (prx - 4 == ppx and pry - 4 == ppy) or (prx - 5 == ppx and pry - 5 == ppy) or (prx - 6 == ppx and pry - 6 == ppy) or (prx - 7 == ppx and pry - 7 == ppy):
        ans = True
    elif (prx - 1 == ppx and pry + 1 == ppy) or (prx - 2 == ppx and pry + 2 == ppy) or (prx - 3 == ppx and pry + 3 == ppy) or (prx - 4 == ppx and pry + 4 == ppy) or (prx - 5 == ppx and pry + 5 == ppy) or (prx - 6 == ppx and pry + 6 == ppy) or (prx - 7 == ppx and pry + 7 == ppy):
        ans = True
    else: 
        ans = False 
    return ans 
print (ajedrez(1, 2 , 6, 7)) 

############################################################ punto 10. ################################################################
def puedesalir (tipo, placa, dia, hora, minuto): 
    ans = None 
    if (tipo == "Particular") and dia == "Lunes" and (placa == 7 or placa == 8) and ((hora >= 6 and hora < 10) or (hora >= 16 and hora < 20)): 
        ans = False 
    elif tipo == "Particular" and dia == "Lunes" and (placa == 7 or placa == 8) and (hora == 10 or hora == 20) and minuto == 0: 
        ans = False 

