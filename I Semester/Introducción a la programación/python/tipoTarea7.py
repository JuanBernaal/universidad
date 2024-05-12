### Punto 2. 

def obtnerEquipo(l): 
    ans = set() 
    for part in l: 
        eq1, eq2 = part[0], part[2] 
        ans.add(eq1) 
        ans.add(eq2) 
    ans = list(ans) 
    return ans 
print(obtnerEquipo([["America", 3, "Cali", 0],
["Junior", 2, "America", 3],
["Santafe", 2, "Junior", 1],
["Cali", 2, "Junior", 2],
["America", 1, "Santafe", 1]]))      