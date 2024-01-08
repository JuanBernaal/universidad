#Recursión. 
def factorial(N): 
    ans = None 
    if N == 0: ans = 1 
    else: 
        ans = N * factorial(N - 1) 
    return ans 
n = 5
a = factorial(n) 
print(f'El factorial de {n} es {a}') 

# forma de escribir 
def mayor(a,b):
    ans = a if a > b else b 
    return ans 
 