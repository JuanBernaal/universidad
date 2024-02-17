(*########################## Punto 1 ##########################*)
Definition nor (a b : bool) : bool :=
    match a, b with 
    | false, false => true
    | false, true => false
    | true, true => false
    | true, false => false
    end.

Example testNor1 : nor false false = true.
Proof. simpl. reflexivity. Qed.

Example testNor2 : nor true false = false.
Proof. simpl. reflexivity. Qed. 

Example testNor3 : nor false true = false.
Proof. simpl. reflexivity. Qed.

Example testNor4 : nor true true = false.
Proof. simpl. reflexivity. Qed. 

(*########################## Punto 2 ##########################*)

Definition neg (b:bool) : bool :=
  match b with
  | true => false
  | false => true
  end.

Definition nor2 (a  b : bool) : bool :=
    neg (orb a b).

Example testNor2.1 : nor false false = true.
Proof. simpl. reflexivity. Qed.

(*########################## Punto 3 ##########################*)
Module tiempo.
Inductive tiempo : Type := 
    | mañana
    | mediodía
    | tarde
    | noche
    | madrugada.

(*########################## Punto 4 ##########################*)

Definition nextTime (t : tiempo) : tiempo :=
    match t with 
    | madrugada => mañana
    | mañana => mediodía
    | mediodía => tarde
    | tarde => noche
    | noche => madrugada
    end. 

Example testNextTime1 : nextTime madrugada = mañana.
Proof. simpl. reflexivity. Qed.

(*########################## Punto 5 ##########################*)

Definition sucesor (n: nat) : nat :=
    match n with 
    | 0 => S 0 
    | S m => S(S m)
    end. 

Definition masTres (n: nat) : nat := 
    S (S (S n)). 

Example testMasTres : masTres 1 = 4.
Proof. simpl. reflexivity. Qed.

(*########################## Punto 6 ##########################*)

Definition multPar (a b : nat) : nat :=
    a * b.

Example testMultPar : multPar 3, 4 = 12.
Proof. simpl. reflexivity. Qed.

(*########################## Punto 7 ##########################*)

Definition componerFunciones {A B C : Type} (f : A -> B) (g : C -> A) : C -> B :=
    fun x => f (g x).

(*########################## Punto 8 ##########################*)

Definition parejas (t: (nat*nat)) : (nat*nat) :=
    (a, b) => (a+b, b-a).

(*########################## Punto 9 ##########################*)

Definition esImpar (n :nat) : bool :=
    negb(Nat.leb(Nat.double(Nat.div n))n).
