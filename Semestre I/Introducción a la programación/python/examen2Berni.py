"""
Federico Terán
Código: 8977473
"""


################### Punto 1 #####################

"""
El máximo de goles no es siempre 700. Esto solo aplica para el ejemplo que se dio en el enunciado.
"""

def determinarEquipo(golescr,eqs,goles):

    suma = 0
    ans = ""
    i = 0
    flag = True
    if  goles > 700:
        ans = "Proximamente"

    else:
        while i < (len(golescr)) and flag:
            if goles > suma and goles <= suma + golescr[i]:
                flag = False
            suma += golescr[i]
            i += 1

    if flag == False:
        ans = eqs[i-1]

    return ans

#print(determinarEquipo([5, 118, 450, 101, 26],["Sporting de Lisboa", "Manchester United", "Real Madrid","Juventus", "Manchester United"],200))

######################### Punto 2 #############################

def obtenerDivisores(n):
    ans = []
    for i in range(1,n+1):
        if n % i == 0:
            ans.append(i)
    return ans

#print(obtenerDivisores(100))


######################### Punto 3 #############################

"""
El nombre correcto era estaContenida. Está bien aunque puede ser más simple.
"""

def esSubCadena(cad1,cad2):
    cantidad = 0
    i = 0
    j = 0
    ans = False
    while i < len(cad1):
        flag = True
        while j < len(cad2) and flag:
            if cad1[i] == cad2[j]:
                flag = False
            j += 1
        if flag == False:
            cantidad += 1   
        i += 1

    if cantidad == len(cad1):
        ans = True

    return ans

#print(esSubCadena("vromeo", "tuveunproblemadedificilsolucion"))

######################### Punto 4 #############################

"""
Los elementos de l ya son cadenas por ende no hay necesidad de convertirlos.
"""

def unir(l,sep):
    ans = ""
    i = 0
    while i < len(l):
        ans += str(l[i])
        if i < len(l) -1:
            ans += sep

        i += 1

    return ans
print(unir(["America", "perdio,", "Cali", "gano.", "El", "profesor", "esta", "triste."], ","))

######################### Punto 5 #############################

"""
El ciclo for más interno no es para nada necesario. Para saber el nombre del archivo es suficiente con colocar:

archivo = l[i][4][j] después de la línea donde se asigna mayorNumero.
"""

def determinarArchivosPesados(l):
    ans = []
    
    for i in range(len(l)):

        imei = l[i][1]
        mayorNumero = 0
        archivo = ""
        for j in range(len(l[i][5])):
            if l[i][5][j] > mayorNumero :
                mayorNumero = l[i][5][j]
            for h in range (0,len(l[i][5])):
                if mayorNumero == l[i][5][h]:
                    archivo = l[i][4][h]

        t =(imei,archivo)
        ans.append(t)

    return ans
"""
print(determinarArchivosPesados([["Iphone 12", "455353243", 2020, 12800,
["foto1.png", "foto2.png", "contrato.pdf", "recuerdo.mp4"],[20, 300, 2000, 12500]],
["Galaxy S22", "1888123", 2019, 10000,
["fotico.png", "paseo.png", "recibo.pdf", "chiste.mp4","cumple.mp4"],[50, 2000, 1000, 5000, 1000]],
["Iphone 13", "111123455", 2022, 200000,
["arch1.png", "arch2.png", "arch3.png", "arch4.png","arch5.mp4", "arch6.exe"],[50000, 30000, 100000, 5000, 20000, 3000]],
["Nokia 1100", "99999", 2007, 5000,["conversacion.txt"], [4000]]]))

 """           

############################ Punto 6 ######################################

"""
Es mejor transformar la variable a a entero una sola vez.
"""

def leerNumeros():
    a = input()
    cantidad = 0
    impares = 0
    mult5 = 0
    num10_20 = 0

    while a != "Fin":

        cantidad += 1

        if int(a) % 2 == 1:
            impares += 1

        if int(a) % 5 == 0:
            mult5 += int(a)

        if int(a) > 10 and int(a) < 20:
            num10_20 += 1
        a = input()

    t = (cantidad,impares,mult5,num10_20)

    print(t)

#leerNumeros()
