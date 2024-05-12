
################################################ Puntos Bonus ################################################

#####################################################
###################### Punto 1 ######################

def imprimirEsradisticas(l):
    print("Total Recaudado por genero:") 
    generos = ["Accion","Infantil","Humor Negro","Terror","Misterio","Comedia Romantica","Drama"]
    ans = []
    for j in range(len(generos)):
        i = 0
        rec = 0
        flag = True
        while i < len(l) and flag:   
                  
            if generos[j] == l[i][2]:              
                rec += l[i][5]
            i += 1

        ans.append(rec)
    for g in range(len(generos)):

        if ans[g] > 0:
            print("%s: %d millones de dolares" % (generos[g],ans[g]))

        else:
            print("%s: 0" % (generos[g]))
"""
imprimirEsradisticas([["Erase una vez en Hollywood", "Quentin Tarantino",
"Humor Negro", 2016, 90, 374,
["Leonardo Di Caprio", "Brad Pitt", "Margot Robbie"]],
["Avengers Endgame", "Hermanos Russo",
"Accion", 2019, 356, 2800,
["Mark Ruffalo", "Robert Downey Jr.", "Chris Evans",
"Chris Hemsworth", "Scarlett Johansson"]],
["The wolf of wall street", "Martin Scorsese",
"Humor Negro", 2013, 100, 392,
["Leonardo Di Caprio", "Margot Robbie", "Jonah Hill"]],
["The Ladykillers", "Alexander Mackendrick",
"Humor Negro", 1955, 2, 10,
["Alec Guinness", "Herbert Lom",
"Peter Sellers", "Cecil Parker"]],
["50 First Dates", "Peter Segal",
"Comedia Romantica", 2004, 75, 120,
["Adam Sandler", "Drew Barrymore", "Rob Schneider"]],
["Titanic", "James Cameron", "Drama", 1997, 200, 1843,
["Leonardo Di Caprio", "Kate Winslet", "Billy Zane",
"Gloria Stuart"]]])
"""
#####################################################
###################### Punto 2 ######################

def picosNamek (l):
    picos = 0
    for i in range(1,len(l)):
        if l[i-1] < l[i] and l[i] > l[i+1]:
            picos += 1

    return picos

#print(picosNamek([3, 5, 7, 5, 4, 6, 7, 5, 3, 4, 3, 5, 4]))

#####################################################
###################### Punto 3 ######################

def invertirSublista(l,m,r):

    ans = []
    for i in range(m):
        ans.append(l[i])

    for j in range (r,m-1,-1):
        ans.append(l[j])
    
    for k in range (r+1, len(l)):
        ans.append(l[k])
    
    return ans

#print(invertirSublista([3, 4, 1, 2, 5, 6, 8, 9, 11, 3, 7, 6], 4, 7))

#####################################################
###################### Punto 4 ######################

def ProblemaUva12503():

    casos = int(input())
    for i in range(casos):
        mem = []
        num = 0
        veces = int(input())
        ins = input()
        for j in range(veces):

            
            if ins == "LEFT":
                mem.append(-1)
                num -= 1

            elif ins == "RIGHT":
                mem.append(1)
                num += 1

            else:
                num += mem[(int(ins[8])-1)]
                mem.append(mem[(int(ins[8])-1)])
            
            if j < veces -1 :
                ins = input()
        print(num)
    if i < casos -1:
        veces = int(input())

ProblemaUva12503()
                           
#####################################################
###################### Punto 5 ######################

def ProblemaUva10050():
    casos = int(input())
    for i in range(casos):
        dias = int(input())
        l = []
        veces = int(input())
        for g in range(veces):
            h = int(input())
            flag = True          
            for j in range(1,dias+1):
                k = 0
                dia = h * j
                if (dia % 7 != 0) and (dia % 7 != 6) and dia <= dias:
                    while k < len(l) and flag:
                        if dia == l[k]:
                            flag = False
                        k += 1
                    if flag:
                        l.append(dia)
        print((len(l)))

#ProblemaUva10050()
            
