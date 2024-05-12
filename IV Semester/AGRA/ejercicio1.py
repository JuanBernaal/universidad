import random
import time

# Función para generar una secuencia aleatoria de longitud n sin repetir
def generar_secuencia(n):
    return random.sample(range(1, 1000001), n)

# Implementación del algoritmo de merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Función para realizar una búsqueda binaria en una lista ordenada
def busqueda_binaria(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return True
    return False

# Generar una secuencia aleatoria de un millón de números sin repetir
secuencia = generar_secuencia(1000000)

# Ordenar la secuencia usando merge sort
start_time = time.time()
merge_sort(secuencia)
end_time = time.time()
print(f"Tiempo de ordenamiento usando merge sort: {end_time - start_time} segundos")

# Realizar 100 búsquedas en la secuencia y medir el tiempo de cada búsqueda
busquedas = random.sample(range(1, 1000001), 100)  # Generar 100 números para buscar
tiempos_busquedas = []

for numero in busquedas:
    start_time = time.time()
    encontrado = busqueda_binaria(secuencia, numero)
    end_time = time.time()
    tiempos_busquedas.append(end_time - start_time)
    if encontrado:
        print(f"El número {numero} está en la secuencia.")
    else:
        print(f"El número {numero} no está en la secuencia.")

# Calcular el tiempo promedio de búsqueda
tiempo_promedio = sum(tiempos_busquedas) / len(tiempos_busquedas)
print(f"Tiempo promedio de búsqueda: {tiempo_promedio} segundos")