(*Definiciones Inductiva de lista de naturales*)
Inductive natlist: Type :=
  | nil
  | cons (n: nat) (l: natlist).



Definition mylist := cons 1 (cons 2 (cons 3 nil)).

(*Se puede definir una notacion para las listas para facilitar la lectura*)

Notation "x :: l" := (cons x l)
                     (at level 60, right associativity).
Notation "[ ]" := nil.
Notation "[ x ; .. ; y ]" := (cons x .. (cons y nil) ..).

Definition mylist1 := 1 :: (2 :: (3 :: nil)).
Definition mylist2 := 1 :: 2 :: 3 :: nil.
Definition mylist3 := [1;2;3].

(*Funciones inductivas sobre listas*)

(*longitud de una lista*)
Fixpoint length (l: natlist) : nat :=
  match l with
  | nil => O
  | h :: t => S (length t)
  end.

Compute length mylist.

(*concatenacion de listas*)
Fixpoint app (l1 l2 : natlist) : natlist :=
  match l1 with
  | nil => l2
  | h :: t => h :: (app t l2)
  end.

Definition mylist4 := 4::5::nil.

Compute app mylist mylist4.

(*Funcion que cuente la cantidad de ceros en una lista*)
Fixpoint ceros (l: natlist) : nat :=
  match l with
  |nil => 0
  |h :: t => match h with
             | 0 => 1 + ceros(t)
             | _ => ceros(t)
             end
  end.



Definition mylist5 := [1;2;3;0;0].

Compute ceros mylist5.

(*Funciones inductivas sobre naturales*)

(*Funcion que determina si es un numero par*)
Fixpoint even (n:nat) : bool :=
  match n with
  | O => true
  | S O => false
  | S (S n') => even n'
  end.

Compute even 4.
Compute even 7.

(*Funcion para un numero impar (recuerde que esta la libreria bool)*)
Search bool.

Definition odd (n: nat) : bool := negb(even n).


Compute odd 4.
Compute odd 7.



(*Funcion para sumar*)
Fixpoint plus (n m : nat) : nat :=
  match n with
  | O => m
  | S n' => S (plus n' m) 
  end.

Compute plus 3 4.

(*Definicion de LP*)
Inductive LP: Type := 
  | T (*Verdadero*)
  | F (*Falso*)
  | var (*variable proposicional: p,q,r*) 
  | neg (F1: LP) (*negacion: ~*)
  | dis (F1: LP) (F2: LP) (*disyuncion: \/*)
  | con (F1: LP) (F2: LP) (*Conjuncion: /\*)
  | imp (F1: LP) (F2: LP). (*Implicacion: ->*)

(*la formula ((~P) -> Q) se representaria en LP como : imp (neg var) (var) *)
