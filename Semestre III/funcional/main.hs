factorial :: Integer -> Integer
factorial n = product [1 .. n]

multi :: Integer -> Integer -> Integer
multi x y = x * y

programa :: [Int] -> Int -> [[Int]]
programa lst n = [[x | x <- lst, x <= n], [x | x <- lst, x > n]]

dividir x [] = [[], []]
dividir x (a:r) | a <= x = [a:(head divs), (head(tail divs))]
                        where divs = (dividir x r)
dividir x (a:r) = [(head divs), a:(head(tail divs))]
                        where divs = (dividir x r)   

ordenada [] = True
ordenada [a] = True
ordenada (a:b:r) = (a <= b) && (ordenada (b:r))

-- zip l1 l2 = costruye parejas con elementos compartidos 
-- [3,9] [6, 7] = [[3,6] [9,7]]

posiciones x lst = aux 0 lst 
            where   aux k [] = []
                    aux k(a:r) | a == x = k: (aux (k + 1) r)
                    aux k(_:r) = (aux (k + 1) r )

posiciones2 x xs = [i | (y, i) <- zip xs [0..], x == y]


mapeo2 f [] y = []
mapeo2 f x [] = []
mapeo2 f (a:r1) (b:r2) = (f a b) : (mapeo2 f r1 r2)


---(**********                                                      **************)
---(********** Funciones como valores: Transformadores de funciones  *************)
---(***********                                                      *************)

-- un elemento divide a la suma:
fconsuma lst = any (\x -> (sum lst) `mod` x == 0) lst

---- Transformadores de funciones

mapeo f  [] = []
mapeo f (x : resto) = (f x) : (mapeo f resto)

mp1 = mapeo (\x -> 2*x) [3, 5, 7]

expo 0 = 1
expo x = 2* expo (x -1)


mpE1 = mapeo expo [3, 5, 7]

---(*** la función mapeo existe en lenguajes funcionales. Se llama map   *****)

mp3 = map expo  [3, 5, 7]


-----(********    filtrar  una lista   **************)


filtrar f  [] = []
filtrar f (x:r) |  (f x) =  x : (filtrar f r)
filtrar f (x:r) = (filtrar f r)

fil1 = filtrar (\x -> mod x  2 == 0) [3, 4, 5, 7, 16, 1]


-----(** filtrar también existe en funcionales  **)
fil2 = filter (\x -> mod x  2 == 0) [3, 4, 5, 7, 16, 1]

---(** map  y filter son polimórficas   ***)

fil3 = map (\x -> x ++ "OK") ["a", "b", "c"]

--------------- Para el examen -----------------------------
doblefilt l1 l2 = filter (\x -> (filter (\y -> y `mod`x == 0) l2) /= []) l1

doblefiltR l1 l2 = aux l1 l2 []
             where
                 aux [] ls acum = acum
                 aux (a:r) [] acum = aux r l2 acum
                 aux (a:r) (b:s) acum | b `mod`a == 0 = aux r (b:s) (a:acum)
                 aux (a:r) (b:s) acum = (aux (a:r) s acum)  

---------------------------------------------------------------------

----(********    Map doble   **************)

mapeo2 f [] [] = []
mapeo2 f [] y = []
mapeo2 f x [] = error "mapeo2, lista 2 vacia"
mapeo2 f (a:r1) (b:r2) = (f a b) : (mapeo2 f r1 r2)

m2p1=mapeo2 (+) [3,6] [7,2]

---(************   zip   unzip  **************)


parzip [] x = []
parzip y [] = []
parzip (a:x) (b:y) = (a,b):(parzip x y)

zz1 = parzip ["yo", "tu", "el"] [1, 2, 3]

----(******   ejercicio: unzip  ***********)




parunzip  [] = ([],[]) 
parunzip ((x,y) : r) = let (l1,l2) = parunzip r in (x:l1, y:l2) 

ll1 = let (lista1,lista2) = parunzip (zip ["yo", "tu", "el"] [1, 2, 3])  in lista1

parunzip2  [] = ([],[]) 
parunzip2 ((x,y) : r) =  (x:l1, y:l2) where (l1,l2) = parunzip2 r

ll1_1 = let (lista1,lista2) = parunzip2 (zip ["yo", "tu", "el"] [1, 2, 3])  in lista1

----(*** zip unzip existen en lenguajes funcionales   ***)
---(** trunca, pero no da error con listas de diferente tamaño   ****)

ll2 = zip ["yo", "tu", "el"] [1, 2, 3]
lu2 = unzip (zip ["yo", "tu", "el"] [1, 2, 3])

--- La función zipWith aplica una función a cada par de elementos (mapeo 2)

ss1= zipWith (+) [2,4,6] [3,7,9]

--  producto escalar de dos vectores

escalar v1 v2 = sum (zipWith (*) v1 v2)

-- las posiciones de todas las ocurrencias de x en una lista
indices x ls = [i | (x',i) <- zip ls [0..], x == x']


---(*  Partir una lista en dos, alternando elementos   **)
---(**                                                ***)


partir  [] = ([],[])
partir (x:[]) = ([x],[])
partir (x:y:r) = (x:l1,y:l2)
           where (l1,l2)= partir r
pp1 = partir [1, 5, 2, 9 , 4]

---(********************           *****************************)
---(********************  reducir una lista a un valor  ****************************)
---(* la función map transforma cada elemento de la lista. Se puede  *)
---(* definir otra que acumule de distintas maneras los elementos *)

---(* definiciones:                                *)
---(* reducir_der f b [a1, a2,..an]= f a1 (f a2 (... (f an b) ...))   *)
---(* reducir_izq f a [b1; b2;..bn]= f (... (f (f a b1) b2) ...) bn    *)

reducir_der  f a [] = a
reducir_der  f a (x : r) = f x  (reducir_der  f a r)

red1 = reducir_der  (\b c -> 2*b+c) 0 [3, 5, 7]
red2 = reducir_der  (+) 0 [3, 5, 7]

---(********  ejercicio:  reducir izquierda   ***********)


reducir_izq  f a [] = a
reducir_izq f a (x : r) = (reducir_izq  f (f a x) r)

rei1 = reducir_izq  (\b c -> 2*b+c) 0 [6,3, 5, 7]

--(* esa función ya existe en lenguajes funcionales  *)
--(* definiciones:                                *)
--(* foldl: f (... (f (f a b1) b2) ...) bn    *)
--(* foldr: f a1 (f a2 (... (f an b) ...))   *)

rer2 = foldr  (\b c -> 2*b+c) 0 [6,3, 5, 7]
rel2 = foldl  (\b c -> 2*b+c) 0 [6,3, 5, 7]

max_con_fold (x:xs) = foldl  max x xs

--(**** ejercicio: definir la fución recalc con fold  **)


recal1 = foldr (\a b -> a + 10*b) 0 [3, 4, 9, 1]


---(*** ejercicio: cómo recalcularla si el arreglo está en orden??   ****)


recal2 = foldl (\a b -> a*10 + b) 0 [1, 9, 4, 3]


--(* Invertir un arreglo usando fold   *)

inv1 = foldl (\a b -> b : a) [] [3, 5, 7]


---(** qué retorna?  **)
incog1 = foldl (\a b -> if (length a) > (length b) then a else b) 
               "pera" 
               ["oscar", "papa", "tango"]

--(***   Usar Fold para aplanar en una sola lista una lista de listas ******)



apl1 = foldr (++) [] [["oscar", "papa", "tango"], ["juana", "rosa", "salsa"]]


---(***********                     ***********)
---(************   STREAMS: listas infinitas          ***********)
---(*************                  ************)

-- enteros infinitos a partir de n -------
-- funciona porque la evaluación en Haskell es 'perezosa'  -----

flujo n = n: (flujo (n + 1) )
nde = flujo 5

elCinco = head nde
los10 = take 10 nde

--- también:
flujo_alt n = nums where nums = n: map (+1) nums
flujo_alt10 = take 12 (flujo_alt 6)

infde3 = flujo 3    ---OJO: NO EVALUAR: imprime infinitamente ---


infde5 = take 10 (flujo 5)

--- OJO: No evaluar infde3 en el intérprete: pide imprimir todos los números!  -----------

primerosDiez= take 10 infde3

--- es equivalente al operador ..
infde3A = [3..]
infde3A10 = take 10 infde3A

----- Todos los numeros impares   ------
impares = filter (\x -> (mod x 2 /= 0)) (flujo 2)

impares_2 = filter even (flujo 2)
imps10 = take 10 impares
imps10_2 = take 10 impares_2

cuadrados = map (^2) impares
cuad10 = take 10 cuadrados

--- ejercicio potencias de pares: take 20 (map (^2) (filter even [0..]))

----(**** Los primos !!  usando la criba de Eratóstenes ****)

eratho flu = (head flu) : eratho (filter (\x ->  x `mod` (head flu) /= 0) flu)


--- los 10 primeros primos  -----
prim10 = take 10 (eratho [2..] )

--- el k-esimo primo ------
nesimo k = (eratho [2..])!! k    --- el operador !! obtiene el k-esimo de una lista



--- map de dos flujos  ---
sumfl2 = mapeo2 (+) impares infde3
--- también ---
sumfl2_2 = zipWith (+) impares infde3

sumaimp_inf = take 20 sumfl2_2

divfl n flu = map (\x  -> (div x n)) flu

realFlu :: (Fractional a) => a -> [a]
realFlu n = n: (realFlu (n + 1) )


divfl2 :: (Fractional a) => a -> [a] -> [a]

divfl2 n flu = map (/ n) flu

-- take 10 (divfl2 3.0 (realFlu 7))

halve                   :: (Fractional a) => a -> a
halve x                 =  x * 0.5


----- eliminar repetidos ---

norep [] = []
norep (x:xs) | (elem x xs) = norep xs
norep (x:xs) = x: norep xs

nr1 = norep [1,3,2,4,3,5,6,6,2,7,8,7]

-----(** Ejercicio: qué hacen estas funciones? ****)---
prefix [] l = True
prefix (x: xs) [] = False
prefix (x: xs) (y: ys) | (x == y) = prefix xs ys
prefix (x:xs) (y:ys) = False

isin [] l = True
isin (x:r) [] = False
isin (x:r) (y:s) | (x == y) && (prefix r s) = True
isin (x:r) (y:s)   = isin (x:r) s

isin2 [] l = True
isin2 (x:r) [] = False
isin2 (x:r) (y:s) | (x == y) && ((take (length r) s) == r) = True
isin2 (x:r) (y:s)   = isin2 (x:r) s

iin1 = isin [2,5,3,1,7] [1,2,5,4,8,4,2,5,3,1,7,9]

iin2 = isin2 [2,5,3,1,7] [1,2,5,4,8,4,2,5,3,1,7,9]



--- con fold

decide x l| (elem x l) = l
decide x l = x:l

norepf l = foldr decide [] l

nrf1 = norepf [1,2,5,4,8,4,2,5,3,1,7,9]

----(****   menor entero que no está en una lista )
splitCola2  l x  = aux l [] []
    where aux [] acum1 acum2  = (acum1,acum2)
          aux (a:r) acum1 acum2 | a <= x = aux r (a:acum1) acum2
          aux (a:r) acum1 acum2 = aux r acum1 (a:acum2)

lnn2 lst | (notElem 0 lst) = 0   -- si no tiene el cero, ese es
lnn2 lst = aux 1 lst          -- aux k l : menor entero >= k que no está en l
           where 
            aux k [] = k
            aux k [a] | k == a = k+1
            aux k [a]  = k
            aux k (x:xs)  = let (l1,l2) = splitCola2 (x:xs) x
                            in let k1 = aux k xs
                               in if k1 < x  then k1
                                  else 
                                      if k1 == x then aux (k1+1) l2
                                      else aux k1 l2

---- Varias ----
notes2int (a:r) = (a, aux r a)
              where aux [] acum = []
                    aux (b:r) acum =  (b-acum): aux r b
int2notes (a,l) = aux l 0
               where aux [] acum =[acum+a]
                     aux (b:r) acum = acum+a : aux r (acum+b)

despliegue p h t x | (p x) = []
                   | otherwise = h x : despliegue p h t (t x)

trs n = despliegue (==0) (`mod` 10) (`div` 10) n
