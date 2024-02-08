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

(**)