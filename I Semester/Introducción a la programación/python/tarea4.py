"""
Federico Terán Pascuas
Introducción a la programación
Código: 8977473

"""


###################################################################################
#### Punto 1 ####



def imprimirSucesion(n):

    for i in range(1, n+1):
        if i < n:
            print("%.4f, " % ((-1/i)**i),end="")

        else:
            print("%.4f" % (-1/n)**n)

#imprimirSucesion(5)
####################################################################################
#### Punto 2 ####
def lineaesp(n):
    esp1 = "  "
    esp = esp1
    i = 0
    while i < n:
        a = esp
        i += 1
        esp += esp1 
    return a 

def lineaast(n):
    ast1 = "*"
    ast = ast1
    i = 0 
    while i < n:
        b = ast 
        i += 1
        ast += ast1 + ast1
    return b 

def imprimirAsteriscos(n):
    for i in range(1,n,1):
        print(lineaesp(n-i)+lineaast(i))
    print(lineaast(n))
    for j in range(1,n):
        print(lineaesp(j)+lineaast(n-j))

imprimirAsteriscos(20)



#################################################################################
#### Punto 3 ####

def simpsonRule(a,b,n):
    h = (b-a)/n
    y = ((a) ** 3) + ((a+n*h) ** 3)

    i = 1

    while i < n:
        if i % 2 == 1: 
            yk4 = 4*((a+i*h) ** 3)
            y += yk4
            i += 1

        elif i % 2 == 0:
            yk2 = 2*((a+i*h) ** 3)
            y += yk2
            i += 1

    ans = h/3 * y

    return ans
    
#print(simpsonRule(1,5,8))


################################################################################
### Punto 4 ####


def euler(n):
    e = 1
    f = 1
    for i in range(1, n + 1):
        f *= i
        e += 1/f
    return e 

#print(euler(10))

################################################################################
### Punto 5 ###


def imprimirLineasNumeros (n):

    maxi = n
    mini = 0
    cont = 1
    cont2 = 0
    for j in range(n,0,-1):
        a = ""
        for i in range (maxi,mini,-1):

            a = a +"  " + str(i)
        print(a)


        maxi += n - cont
        mini += n - cont2
        cont2 += 1
        cont += 1




#imprimirLineasNumeros(5)



################################################################################
### Punto 6 ###
def filtrarValoresEnPosicion(v):
    a = []
    i = 0
    while i < len(v):
        if v[i] == i:
            a.append(i)
        i += 1
    return a 

#print(filtrarValoresEnPosicion([10, 1, 5, 3, 15, 6, 7, 7]))

################################################################################
### Punto 7 ### 

def reemplazar(l,v1,v2):
    i = 0
    ln = []
    while i < len(l):

        if l[i] == v1:
            ln.append(v2)
        else:
            ln.append(l[i])

        i += 1
    return ln

#print(reemplazar([4, 1, 11, 1, 8, 1, 1, 5, 6, 7, 17, 1], 1, 100))

####################################################################################
### Punto 8 ###

def perimetroFigura(x,y):
    
    ans = 0
    
    for i in range(0,(len(x)-1)):
        lx = ((x[i+1]) - x[i]) ** 2 
        ly = ((y[i+1]) - y[i]) ** 2 
        lado = (lx + ly) ** (1/2)
        ans += lado


    lx0 = ((x[0]) - x[len(x)-1]) ** 2 
    ly0 =  ((y[0]) - y[len(x)-1]) ** 2 
    lado0 = (lx0 + ly0) ** (1/2)
    ans += lado0
    
    
    

    return ans 

#print(perimetroFigura([2,2,4,4],[1,3,3,1]))
#print(perimetroFigura([1,3,5],[1,3,1]))
        

####################################################################################
### Punto 9 ###
def factAcumInv(N):
    f = 1
    listaFactorial = []
    listaFactorialInvertida = []
    for i in range(1, N + 1):
        
        f *= i
        listaFactorial.append(f)


    for j in range(N-1,-1,-1):
        listaFactorialInvertida.append(listaFactorial[j])

    
    return listaFactorialInvertida
        
##print(factAcumInv(7))

######################################################################################
### Punto 10  ###

def emoogleBalance(l):
    pos = 0
    neg = 0
    for i in range(0,len(l)):
        if l[i] > 0:
            pos += 1
        elif l[i] == 0:
            neg += 1

    ans = pos - neg

    return ans


def leerImprimir():
    casos = int(input())
    caso = 1
    while casos != 0:
        a = [] 
        for i in range(casos):
            
            b = (int(input()))
            a.append(b)
        print("Case %d: %d" % (caso,emoogleBalance(a)))
        caso += 1
        casos = int(input())



#leerImprimir()
######################################################################################
### Punto 11  ###

def ordenAscendente(l):
    i = 1 
    ans = True
    m = 1
    while i < len(l) and ans == True:
        if l[i] <= l[i-1]:
            ans = False
        i += 1
        m += 1
    return ans


def ordenDescendente(l):
    i = 1 
    ans = True
    m = 1
    while i < len(l) and ans == True:
        if l[i] >= l[i-1]:
            ans = False
        i += 1
        m += 1
    return ans

def lumberjackSequencing():
    
    casos = int(input())
    print("Lumberjacks:") 
    for i in range(casos):
        l = []
        for i in range(10):
            a = int(input())
            l.append(a)

        if ordenAscendente(l) == True or ordenDescendente(l) == True:
            print("Ordered")
        else:
            print("Unordered")

#lumberjackSequencing()