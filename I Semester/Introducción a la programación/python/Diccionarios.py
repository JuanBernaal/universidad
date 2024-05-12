######## Diccionarios 
#Creación 
d = {} 
d2 = dict()

d = {1 : 100, "hola" : 67, (2, 3, 4) : 100, 8 : [3, 4, 667]} 

d3 = {0 : 1, 1 : 2, "nombre" : "Juan David", "Edad" : 17}  

#### Valores No mutables (por valor)
# Tuplas, número, booleanos, strings. 

lista = ["tom", 22, True, 65, "gato"] 
tupla = ("tom", 22, True, 65, "gato") 



def run():
    dictionary = {
        "str" : "Tom",              #Las key solo pueden tomar un valor.  
        "int" : 22, 
        "bool" : True, 
        "int" : 65, 
        "str" : "gato"              #Al haber dos llaves iguales, devuelve el ultimo valor asignado a esa key.
    }
    
    print(dictionary['str'])        #imprime el valor asigando a la key. 
run() 

dictionary = {
        "str" : "Tom",              #Las key solo pueden tomar un valor.  
        "int" : 22, 
        "bool" : True, 
        "int" : 65, 
        "animal" : "gato"           #Al haber dos llaves iguales, devuelve el ultimo valor asignado a esa key.
    } 

dictionary["n"] = "m"               # n es la key y m es el elemento de la key, las añade al diccionario.

del dictionary ["n"]                #n es la key que se quiere eliminar y su indice se retira también. 

dictionary.values()                 #Devuelve los indices de un diccionario.

dictionary.keys()                   #Devuelve las llaves de un diccionario. 

dictionary.items()                   #Devuelve el key y su indice en forma de tuplas. 

#print(dictionary) 
 
print(dictionary.items()) 

print(d.values()) 