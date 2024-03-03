Inductive LP: Type := 
  | T (*Verdadero*)
  | F (*Falso*)
  | var (*variable proposicional: p,q,r*) 
  | neg (F1: LP) (*negacion: ~*)
  | dis (F1: LP) (F2: LP) (*disyuncion: \/*)
  | con (F1: LP) (F2: LP) (*Conjuncion: /\*)
  | imp (F1: LP) (F2: LP). (*Implicacion: ->*)

(*########################## Punto 1 ##########################*)

Fixpoint countImp (F : LP) : nat :=
    match F with
    | T => 0
    | F => 0 
    | var => 0
    | neg X => countImp X 
    | dis F1 F2 => countImp F1 + countImp F2
    | con F1 F2 => countImp F1 + countImp F2
    | imp F1 F2 => 1 + countImp F1 + countImp F2
    end.

(*########################## Punto 2 ##########################*)

Fixpoint countSubF (F : LP) : nat :=
    match F with
    | T => 1
    | F => 1
    | var => 1
    | neg X => 1 + countSubF X
    | dis F1 F2 => 1 + countImp F1 + countImp F2
    | con F1 F2 => 1 + countImp F1 + countImp F2
    | imp F1 F2 => 1 + countImp F1 + countImp F2
    end.

(*########################## Punto 3 ##########################*)

Fixpoint countSimb (F : LP) : nat :=
    match F with 
    | T => 0
    | F => 0
    | var => 0 
    | neg X => countSimb X
    | dis F1 F2 => 1 + countSimb F1 + countSimb F2
    | con F1 F2 => 1 + countSimb F1 + countSimb F2
    | imp F1 F2 => countSimb F1 + countSimb F2
    end.

(*########################## Punto 4 ##########################*)

Inductive binaryTree : Type :=
    | Nodo : nat -> binaryTree -> binaryTree -> binaryTree
    | Hoja : binaryTree.

(*########################## Punto 5 ##########################*)

Fixpoint countHojas (arbol : binaryTree) : nat :=
    match arbol with
    | Hoja => 1
    | Nodo _ izq der => countHojas izq + countHojas der
    end.

(*########################## Punto 6 ##########################*)

Fixpoint sum5Hojas2Nodos (arbol : binaryTree) : nat :=
    match arbol with
    | Hoja => 5
    | Nodo n Hoja Hoja => n + 5 
    | Nodo n izq der => n + 2 + sum5Hojas2Nodos izq + sum5Hojas2Nodos der
    end.

(*########################## Punto 7 ##########################*)

Fixpoint sumNodos (arbol : binaryTree) : nat :=
    match arbol with
    | Hoja => 0
    | Nodo n izq der => n + sumNodos izq + sumNodos der
    end.

(*########################## Punto 8 ##########################*)

Fixpoint multiply (a b : nat) : nat :=
    match a with 
    | 0 => 0
    | S a' => b + multiply a' b
    end.

(*########################## Punto 9 ##########################*)

Fixpoint isUnequal (a b : nat) : bool :=
    match a, b with 
    | 0, 0 => false
    | 0, S _ => true 
    | S _, 0 => true
    | S a', S b' => isUnequal a' b'
    end.

(*########################## Punto 10 ##########################*)

Fixpoint isLessThan (a b : nat) : bool :=
    match a, b with 
    | 0 , _ => true 
    | S a', 0 => false 
    | S a', S b' => isLessThan a' b'
    end.

Fixpoint divide (a b : nat) : nat :=
  match isLessThan a b with
  | true => O 
  | false =>
      match a, b with
      | O, _ => O 
      | S a', S b' => S (divide (a' - b') b') 
      end
  end.