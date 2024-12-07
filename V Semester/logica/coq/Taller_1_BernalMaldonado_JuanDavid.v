Module bools.
(***Punto 1***)
Inductive bool : Type :=
  | true
  | false.

Definition nor (b1 b2 : bool) : bool :=
  match b1, b2 with
  | true, _ => false
  | _, true => false
  | _, _ => true
  end.

Example testNor1: (nor true false) = false.
Proof. simpl. reflexivity. Qed.
Example testNor2: (nor false false) = true.
Proof. simpl. reflexivity. Qed.
Example testNor3: (nor true true) = false.
Proof. simpl. reflexivity. Qed.
Example testNor4: (nor false true) = false.
Proof. simpl. reflexivity. Qed.

(***Punto 2***)
Definition neg (b : bool) : bool :=
  match b with
  | true => false
  | false => true
  end.

Definition or (b1:bool) (b2:bool) : bool :=
  match b1 with
  | true => true
  | false => b2
  end.  

Definition nor2 (b1 b2 : bool) : bool :=
  neg (or b1 b2).

Example testNor12: (nor2 true false) = false.
Proof. simpl. reflexivity. Qed.
Example testNor22: (nor2 false false) = true.
Proof. simpl. reflexivity. Qed.
Example testNor32: (nor2 true true) = false.
Proof. simpl. reflexivity. Qed.
Example testNor42: (nor2 false true) = false.
Proof. simpl. reflexivity. Qed.

End bools.
(***Punto 3***)
Module punto3.
Inductive tiempo: Type :=
  | mañana
  | mediodía
  | tarde
  | noche
  | madrugada.

(***Punto 4***)
Definition siguienteTiempo (d: tiempo) : tiempo := 
  match d with
  | mañana => mediodía
  | mediodía => tarde
  | tarde => noche
  | noche => madrugada
  | madrugada => mañana
  end.
Example testTiempo: siguienteTiempo madrugada = mañana.
Proof. simpl. reflexivity. Qed.

End punto3.

Module Naturales.
(***Punto 5***)
Definition sumar3 (n:nat) : nat :=
  S (S(S n)).

Compute sumar3 0.
Compute sumar3 3.
(***Punto 6***)
Definition mult (t: (nat * nat)) : nat :=
  match t with
  | (n1, n2) => n1 * n2
  end.

Compute mult (3, 4).

(***Punto 7***)
Definition suma_funciones (f g : nat -> nat) : (nat -> nat) :=
  fun x => f x + g x.

Compute suma_funciones sumar3 sumar3 3.

(***Punto 8***)
Definition tuplas (t: (nat * nat) ) : (nat * nat) := 
  match t with
  | (n1, n2) => (n1 + n2 , n2 - n1)
  end.

Compute tuplas (2, 4).

Definition neg (b : bool) : bool :=
  match b with
  | true => false
  | false => true
  end.
(***Punto 9***)
Definition es_impar (n: nat) : bool :=
    neg (Nat.leb n (Nat.double (Nat.div2 n))).

(***Punto 10***)
Definition punto10 (n: nat) : nat :=
  match es_impar n with
  | true => n + 5
  | false => n * 3
  end.

Compute punto10 3.
Compute punto10 5.
Compute punto10 8.
Compute punto10 6.
(***Punto 11***)
Definition g (f g : nat -> nat) (t: nat * nat) : (nat * nat) :=
  match t with
  | (a, b) => (f (a + b), g(a * b))
  end.

Compute g sumar3 sumar3 (2,3).
(***Punto 12***)
Definition func12 (t: nat * nat) (f : nat -> nat): nat :=
  let (a, b) := t in 
  match Nat.leb b (Nat.double a) with
  | false => f (b - (2 * a))
  | true => f (a + 2)
  end.

Compute func12 (2,5) sumar3.


End Naturales.












