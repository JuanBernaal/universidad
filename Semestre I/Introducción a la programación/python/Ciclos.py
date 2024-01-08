"""
Ciclos python
Juan Bernal
Intro programacion
""" 

"""
preguntar puede avanzar, if true entonces avanzar, if false girar y 
Siempre que "puedeavanzar" sea igual a verdadero repetir avanzar 
Siempre que "puedeavanzar" sea igual a falso repetir girar hasta que "puedeavanzar" sea igual a verdadero
"""
#######################################################################################################################
############################################### Tipos de Ciclos #######################################################
#######################################################################################################################

##### Ciclo "while"
# Repetir mientras algo sea cierto. 
"""
while cond:
    ...
Todo lo que necesitemos ejecutar si se cumple la condicion 


while not encontrar muro(): 
    avanzar()
"""
"""
n = 10 
i = 0

while i < n: 
    print("Valor i = " + str (i))
    i += 1

print ("Después del while")
"""
"""
from tkinter import N


def factorial(n): 
    ans = 1 
    i = 1
    while i <= n: 
        ans *= i 
        i += 1 
    return ans 
#print (factorial(3)) 

n = 9
i = n 
while i >= 0: 
    #print(i)
    i //= 2

i = n 
j = 4
n = 10
while j >= 0: 
    #print (i)
    i -= 1 

i = n 
while i < n: 
    #print(i)
    i += 1
#El ciclo no inicia, ya que al i ser igual a n hace que cuando llegue al while pregunte que si n es menor que n, lo cual es falso, 
#por eso el ciclo no funciona
""" 
#Un programa que imprima las filas de multiplicar
"""
def tablasdemultiplicar(n, m):
    i = 1 
    while not (i == m + 1): 
        res = i * n 
        print("%d x %d = %d" % (i, n, res)) #%d = es para un entero, %s = es para una cadena, %f = numeros flotantes (con decimales).
        i += 1
"""

#tablasdemultiplicar(5, 20)

##### Ciclos "for"#####
"""
n = 10
for i in range(4, n): 
    print(i) 
Este for, imprime los numeros que hay en el rango partiendo desde el 4 hasta el 9, porque el range agarra uno antes
"""
"""
n = 10 
for i in range (n, 0, -2):
    print(i)
Empieza en n y le resta de dos numeros 
El primer numero es desde donde se quiere empezar, el segundo es para ponerle limite de hasta donde llegar y el tercero es cuanto 
se le quiere sumar o restar
por eso este ciclo empieza en 10 y le emmpieza a restar - 2 hasta que llega a 0
"""
"""
n = 10 
for i in range (1, n + 1, 3): 
    print(i)
"""
"""
n = 10 
i = 1
while i < n + 1: 
    print(i)
    i += 3
"""
#Escribir la definicion de la operacion ImprimirNumeros que reciba dos numeros "n" y "m" e imprima todos los numeros 
#entre n y m que no son multiplos de 3 ni de 4. Escriba este procedimiento utilizando ciclos for y utilizando ciclos while.
"""
def ImprimirNumeros(n, m): 
    i = n #debe empezar en n porque es el primer valor porque se examina cada valor de n para saber si se debe imprimir o no 
    while i <= m: 
        if i % 3 != 0 and i % 4 != 0:
            print(i)
        i += 1
ImprimirNumeros(10, 40)
"""
"""
def ImprimirNumerosFor(n, m):
    for i in range(n, m + 1): 
        if i % 3 != 0 and i % 4 != 0: 
            print(i)
""" 
## Punto 2. 
"""
def leerNumeros(): 
    
    datosleidos = 0
    suma = 0
    mayor = float("-inf") 
    menor = float("inf")
    a = input()
    while a != "END": 
        b = int(a)
        datosleidos += 1
        suma += b  
        if b > mayor: 
            mayor = b
        if b < menor:
            menor = b
        a = input()
    t = (datosleidos, suma, mayor, menor) 
    print(t) 
leerNumeros()
"""
"""
def determinarRelacion(): 
    ans = None 
    if a < b: 

def leerimpriir11172(): 
    casos = int(input>()) 
    for i in range (casos): 
        x = int(input())
        y = int(input())
        r = determinarRelacion
        print(r)
"""
# punto 3.  
def esPotencia(v, n): 
    ans = False 
    p = 0
    ac = n ** p 
    
    while ac <= v: 
        if ac == v: 
            ans = True 
        ac *= n 
        p += 1 
        
    return ans 

#tarea 
def imprimirPotencias(n, m): 
    i = 0
    while (n ** i) < m: 
            print (n ** i)
            i += 1 
#imprimirPotencias(3, 90) 

#el end sirve para dos cosas, la primera es que te permite agregar al final de una cadena cualquier cosa
#la segunda funcion es que el siguiente print, se imprimira pegado a la cadena anterior del print. Ejemplo: 
#print("instagram: ", end = "@")
#print("bernaljuandaviid")

#punto 6.
def sumarDigitos(n): 
    ans = 0 
    while n > 0: 
        ans += (n % 10) 
        n //= 10 
    return ans 
#print(sumarDigitos(200302212))

#Solucion problema uva judge online 10055: 

def resolver(a, b): 
    ans = b - a 
    return ans 

def leerImprimir10055(): 
    line = input() 
    while line != "": 
        a = int(line) 
        b = int(input()) 
        r = resolver(a, b) 
        print(r) 
        line = input() 
#leerImprimir10055()

def sumarDigitos(x): 
    ans = 0 
    while x > 0: 
        ans += (x % 10) 
        x //= 10 
    return ans 

#leerImprimir()

###Ejercicio 2. 

def imprimirLineasNumeros(n): 
    
    for i in range(1, n + 1): 
        
        suma = i 
        
        for m in range(1, n + 1): 
            
            if m < n: 
                
                print("%d " % (suma), end = "") 
                
            else: 
                
                print(suma) 
                
            suma += n  
            
### mientras sea distinto a - 1 y -10 o menor a - 200

def leerImprimirLineasNumeros(): 
    
    a = int(input())
    
    while (a != -10 and a != 10) or a < -200: 
        
        imprimirLineasNumeros(a)  
        
        a = int(input()) 
leerImprimirLineasNumeros()


