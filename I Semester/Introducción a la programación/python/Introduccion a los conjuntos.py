"""
Itroducción a los conjuntos
"""

### Crear conjuntos
s = set()
t = {0,1,2,3}
w = {0,5,6,7}
a = {6,32,53,0,-1}

### Operaciones con conjuntos

# Agregar elementos
t.add(4) 
t.update([100,200])

# Eliminar elementos
a.pop()
a.remove(0)  # Te da error si no encuentra el elemento en el conjunto. 
a.discard(-1) #Si no encuentra el elemento no devuelve error, simplemente continua.

# Unión
st = t | w 
t.union(w)
print(st)

# Intersección
d = t & w 
f = t.intersection(w)
t.intersection_update(w)   # El resultado de la intersección se va a guardar en la variabele t
print(d)

#Diferencia 
dif = t - w
t.difference(w)
t.difference_update(w)    # El resultado de la diferencia se va a guardar en la variabele t

# Diferencia simetrica
t.symmetric_difference(w)
t.symmetric_difference_update(w)   # El resultado de la diferencia simetrica se va a guardar en la variabele t

# Recorrer un conjunto
for elem in t:
    print("elemento %d" % (elem))


# Convertir un conjunto en una lista
list(w)

# Convertir una lista a un conjunto
lista = [1,1,2,2,3,3,4,5,6,6]
c = set(lista)
print(c)

# Tamaño de un conjunto
tam = len(c)

# Subconjunto y superconjunto
c1 = {2,4}
c2 = {2,4,6,8}
res = c1.issubset(c2)
ans = c2.issuperset(c1)
print(res)
print(ans)

# Subconjunto propio
c3 = {1,2,3,4,5}
c4 = {1,5}
ans1 = c3 > c4
print(ans1)
ans2 = c4 < c3
print(ans2)


### Ejercicio

def tieneRepetidos(l):
    s = set(l)
    ans = len(s) < len(l)
    return ans

print(tieneRepetidos([1,2,3,1]))

def convertirAConjunto(l):
    ans = set()
    for e in l:
        ans.add(e)
    return ans
print(convertirAConjunto([1,2,2,2,3,2,5,6,9,9]))

#El subconjunto propio contiene mas valores que el conjunto que se esta verificando. 
#En cambio el subconjunto, si puede tener los mismos valores. 
#El super conjunto es porque es igual al otro conjunto, pero tiene mas elementos. 