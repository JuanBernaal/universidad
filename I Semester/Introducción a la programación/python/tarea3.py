"""
Juan David Bernal   Código 8977771 
9 de septiembre del 2022
Solución a la tarea 3 
"""  
################################################################# Punto 1. #################################################################
def imprimirNumerosWhile(n, m): 
    i = n
    while i <= m:
        if (i % 900 == 0) or (i % 13 == 0): 
            print(i)
        i += 1
#imprimirNumerosWhile(1, 1000)


def imprimirNumerosFor(n, m): 
    for i in range(n, m + 1): 
        if i % 900 == 0 or i % 13 == 0: 
            print(i) 
#imprimirNumerosFor(1, 1000) 

################################################################# Punto 2. #################################################################

def leerNumeros(): 
    cantidadDatosLeidos = 0
    cantidadNumerosImpares = 0
    sumaNumerosMultiplos5 = 0
    cantidadnumerosentre10y20 = 0
    a = input()
    while a != "Fin": 
        b = int(a) 
        cantidadDatosLeidos += 1 
        if b % 2 != 0:   
            cantidadNumerosImpares += 1 
        if b % 5 == 0: 
            sumaNumerosMultiplos5 += b 
        if (b > 10) and (b < 20): 
            cantidadnumerosentre10y20 += 1 
        a = input()
    tupla = (cantidadDatosLeidos, cantidadNumerosImpares, sumaNumerosMultiplos5, cantidadnumerosentre10y20)
    print(tupla) 
#leerNumeros() 

################################################################# Punto 3. #################################################################

def imprimirPotencias(n, m): 
    i = 0
    while (n ** i) < m: 
            print (n ** i)
            i += 1 
#imprimirPotencias(3, 90) 

################################################################# punto 4. #################################################################
"""
def sumarDigitos(n): 
    ans = 0 
    while n > 0: 
        ans += (n % 10) 
        n //= 10 
    return ans 

def zlatanSueldo(sal, e, n): 
    
    x = 0 
    y = None 
    while x <= n - 1: 
        x += 1
        x1 = print(x, end = "")
    total = sal + (e * 10000) + (sumarDigitos(x1)) * 5000  
    print(total) 
zlatanSueldo(950000, 30, 5) 
"""
################################################################# punto 5. #################################################################

def UVa12577(): 
    a = input() 
    while a != "*":
        if a == "Hajj": 
            print("Hajj-e-Akbar") 
        if a == "Umrah": 
            print("Hajj-e-Asghar") 
        a = input()
#UVa12577() 
