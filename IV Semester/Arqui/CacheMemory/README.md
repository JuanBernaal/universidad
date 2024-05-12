# CacheMemory
Memoria completamente asociativa, FIFO y WT

# Instrucciones  de uso

Desde la terminal de windows:

1. Ejecutar "g++ generator.cpp" para crear el .exe. Recomendacion: "g++ generator.cpp -o generator".
2. Ejecutar el "generator.exe" e ingresar la cantidad de Queries deseadas. 
Ejemplo de uso: "generator.exe > test.txt".
2.1. Una vez hecho esto se puede observar que el test.txt tendra 3074 datos y seguido se encuentran la cantidad de instrucciones especificadas en el generator.
3. Para hacer la prueba sobre este archivo se debe crear el test.exe. En este caso se puede utilizar "makeFIle.cmd" en la terminal para crear el ejecutable del "test.cpp".

    3.1. El ejecutable aparece como "main.exe".

4. Una vez se tiene el "main.exe" y el "test.txt" se puede ejecutar "main.exe < test.txt" en caso de querer imprimir el resultado en la terminal.

5. La ejecución del main hará que se utilice la caché, en caso de que se quiera usar la ram se puede usar "main -r < test.tx" y como parametro opcional en caso de querer escribir el resultado en un documento "main -r < test.tx > resultado.txt"
   
# Como leer los datos de salida

1. Los primeros datos en salir son los resultados de las Queries (Instrucciones).
2. En el caso de la Caché son dos niveles, el primer nivel representa a la caché y el segundo nivel a la memoria ram. No hay misses para la memoria ram.
3. En el caso de la memoria ram solo es un nivel. 

- **Nota**: En "reporte.docx" se puede encontrar el resultado de las pruebas realizadas y las maquinas de estado