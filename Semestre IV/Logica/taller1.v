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

Example testNor21 : nor false false = true.
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

Example testMultPar : multPar 3 4 = 12.
Proof. simpl. reflexivity. Qed.

(*########################## Punto 7 ##########################*)

Definition componerFunciones {A B C : Type} (f : A -> B) (g : C -> A) : C -> B :=
    fun x => f (g x).

(*########################## Punto 8 ##########################*)

Definition parejas (t : nat * nat) : nat * nat :=
  match t with
  | (a, b) => (a + b, b - a)
  end.

(*########################## Punto 9 ##########################*)

Definition esImpar (n :nat) : bool :=
    (Nat.leb(Nat.double(Nat.div2 n) + 1)n).  

Example odd1 : esImpar 2 = false.
Proof. simpl. reflexivity. Qed.
Example odd2 : esImpar 5 = true.
Proof. simpl. reflexivity. Qed.
Compute esImpar 5.
Compute esImpar 17.
Compute esImpar 16.

(*########################## Punto 10 ##########################*)

Definition punto10 (n: nat) : nat := 
    match esImpar n with
    | true => n + 5
    | false => n * 3
    end.

(*########################## Punto 11 ##########################*)

Definition punto11 (g: nat -> nat) (f: nat -> nat) (t: nat * nat) : (nat * nat) :=
    match t with
    | (a,b) => (f(a + b), g(a * b))
    end.

(*########################## Punto 12 ##########################*)

Definition punto12 (t : nat*nat) (f: nat -> nat) : nat :=
    match t with
    | (a, b) => 
        match Nat.leb b (2*a) with
        |true => f (b - (2 * a))
        |false => f (a + 2)
        end
    end. 