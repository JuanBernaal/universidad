"""
Ejemplos Operadores Lógicos.
"""

"""
Hay 3 operadores lógicos y condicionales.


"""
"""
Hay 3 operadores particulares oara la conjunción.
-   Conjuncón AND - & Lógico.

and ambos valores tienen que ser True para que el resultado sea verdadero.

Disyunción - or -

or: Uno o los dos valores deben ser True para que el resultado sea True

- - Negación - Not

not: El valor debe ser False para que el resultado sea True
"""

x1 = 5
y1 = -3
print ( "Valores booleanos: " + str(x1) + " " + str (y1))
f = x1 > 0 and y1 > 0

g = (x1 > 0 and y1 > 0) or (x1 > 0 and y1 < 0) 

##################################################33

### Condicionales : Son estructuras de control que permiten
###                 condiciar la ejecución de instrucciónes
###                 a la validez de alguna expresión.

### Forma 1.

"""
if condición :
Instrucciones a ejecutar si la condicion es True
"""

# Problema: Determinar si un Estudiante gana o no la materia
#           a partir de las 5 notas de evaluación.

p1 = 4.5
p2 = 2.3
p3 = 3.4
ts = 2.4
pr = 2.0

notaFinal1 = ( p1 + p2 + p3 + ts + pr) / 5
notaFinal2 = ( p1 * 0.2) + (p2 * 0.2) + (p3 * 0.2) + (ts * 0.2) + (pr * 0.2)

print (notaFinal1)
print (notaFinal2)

resultado = notaFinal1 >= 3.0
print (resultado)
## Doble == significa que es igual a porque si solo se pone un igual, se le está definiendo 
if resultado == True:
    print ("Siiiii")
    print ("Gane la materiaaaa")
else :
    print ("Toco veranear")
    print ("Moriremos")
print ("Después del condicional")
#Forma ":
"""
if condición:
    Instrucciones a ejecutar si la condicion es True
Else:
    instrucciones a ejecutar si la consición es False
"""

if p1 >= 3.0 or p2  >= 3.0 or p3 >= 3.0:
    print ("Me van a comprar el iphone 13")
else:
    print ("No vas a tener celular nuevo")

if notaFinal1 < 3:
    print ( "De malas papi no hay Iphone")
else:
    print (True)

#Forma 3: Evaluar múltiples condiciones
"""
if condición1:
    instrucciones que se deben ejecutar si condicion1 es True
elif condicion2:
    instrucciones que se deben ejecutar si condicion2 es True
elif condicion3:
    instrucciones que se deben ejecutar si condicion3 es True
...
else:
    instrucciones que se deben ejecutar si ninguna condición
    resultó True
"""


## problema:    Se quiere saber el nombre de un día a partir
#               del número que ocupa el día en la semana: 1, 2, 3, 4, 5, 6, 7.
dia = 3
nombre = None 
if dia == 1:
    nombre = "Lunes"
elif dia == 2:
    nombre = "Martes"
elif dia == 3:
    nombre = "Miércoles"
elif dia == 4:
    nombre = "Jueves"
elif dia == 5:
    nombre = "Viernes"
elif dia == 6:
    nombre = "Sábado"
elif dia == 7:
    nombre = "Domingo"
else:
    nombre = ("Petro aún no ha creado ese festivo") 
print (nombre) 

### problema:
#   Se quiere saber si una fecha dada es una fecha válida. La
#   fecha se va a representar como 3 números (día, mes, año).

día = 29
mes = 2
año = 2013
def divisible ( x, y ):
    bisiesto = None 
    if x % y == 0:
        bisiesto = True
        print ("Es año bisiesto")
    else:
        bisiesto = False 
        print ("No es año bisiesto")
    return bisiesto 
divisible (año , 4 )
bisiesto = None
if bisiesto == True:
    ans = True 
ans = None
if año <= 0:
    ans = False
elif mes < 1 or mes > 12:
    ans = False
elif día < 1 or día > 31:
    ans = False
elif (bisiesto == True and mes == 2):
    ans = True
elif (mes == 2 and día <= 29):
    ans = True 
elif (mes == 2 and día <= 29):
    ans = True
elif (mes == 2 and día == 29):
    ans = False
elif (mes == 2 and día >= 29):
    ans= False 
elif (mes == 4 and día >= 31):
    ans = False
elif (mes == 6 and día >= 31):
    ans = False
elif (mes == 9 and día >= 31):
    ans = False
elif (mes == 11 and día >= 31):
    ans = False 
else:
    ans = True
if ans == True:
    print ("La fecha es valida")
else :
    print ("La fecha no es valida") 


## Queremos saber si un año es bisiesto y que se le cambiaria al programa para que verifique si cierto año es bisiesto. 

""" 
Año = None
if Año % 4 == 0:
    Año = True
elif Año % 100 == 0:
    Año = True  
elif Año % 400 == 0:
    Año = True
if Año == True:
    print ("Es un año bisiesto")
else:
    print ("No es año bisiesto")
"""







                        




        
 
