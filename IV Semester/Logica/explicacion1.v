Module dias.
(*Definicion de tipos nuevos*)
Inductive dia: Type :=
  | lunes
  | martes
  | miercoles
  | jueves
  | viernes
  | sabado
  | domingo.

(*Funcion sobre dato dia*)
Definition siguienteDia (d: dia) : dia := 
  match d with
  | lunes => martes
  | martes => miercoles
  | miercoles => jueves
  | jueves => viernes
  | viernes => sabado
  | sabado => domingo
  | domingo => lunes
  end.

(*El comando Compute permite computar el valor de una funcion dado unos parametros*)
Compute siguienteDia lunes.
Compute siguienteDia (siguienteDia martes).

(*El comando Example, permite probar si una afirmacion es cierta*)
(*simpl simplifica la expresion: siguienteDia lunes -> martes*)
(*reflexivity indica que tengo el mismo resultado a ambos lados de una igualdad*)
Example testDias: siguienteDia sabado = domingo.
Proof. simpl. reflexivity. Qed.

End dias.

(*Compute siguienteDia sabado.*)

Module booleanos.

(*definicion de booleanos*)
Inductive bool : Type :=
  | true
  | false.

(*definicion de negacion*)
Definition neg (b:bool) : bool :=
  match b with
  | true => false
  | false => true
  end.

(*definicion de conjuncion*)
Definition and (b1:bool) (b2:bool) : bool :=
  match b1 with
  | true => b2
  | false => false
  end.

Definition and2 (b1:bool) (b2:bool) : bool :=
  match b1, b2 with
  | _, false => false
  | false, _ => false
  | true, true  => true
  end.

(*definicion de disyuncion*)
Definition or (b1:bool) (b2:bool) : bool :=
  match b1 with
  | true => true
  | false => b2
  end.

Example testOr1: (or true false) = true.
Proof. simpl. reflexivity. Qed.
Example testOr2: (or false false) = false.
Proof. simpl. reflexivity. Qed.

End booleanos.

Module naturales.
(*Definicion de numeros naturales*)
Inductive nat : Type :=
  | O
  | S (n : nat).

(*Funcion predecesor*)
Definition pred (n : nat) : nat :=
  match n with
  | O => O
  | S n' => n'
  end.


End naturales.

(*Coq tiene por defecto implementado los numeros natures*)
Check S ( S ( S O) ).
Compute 3 + 4.

(*Comandos adicionales*)
(*El comando Check permite verificar el tipo de un dato/funcion *)
Check S.
Check O.
(*el comando Search permite ver las funciones definidas de librerias*)
Search nat.
(*Con print es posible ver la definicion de la funcion*)
Check Nat.div2.
Print Nat.div2.

(*estas funciones se pueden utilizar*)
Check Nat.pow.
(*esta funcion eleva el cubo*)
Definition cubo (base:nat) : nat:= (Nat.pow base) 3. 


(*otras funciones de Nat*)
(*esta funcion recibe un numero natural n y devuelve el numero natural n + n o 2*n *)
Print Nat.double.
(*esta funcion recibe un numero natural n y devuelve el numero natural floor(n/2) o division entera de n entre 2 *)
Print Nat.div2.
(*esta funcion recibe dos numeros naturales n1 y n2 y devuelve un valor booleano resultado de la comparacion n1 <= n2 *)
Print Nat.leb.


(*Coq tambien tiene a los booleanos*)
Search bool.

(*Las funciones pueden recibir funciones o tuplas*)

Definition ejemplo1 (f: nat -> nat) (n: nat) : nat := f n.

Definition ejemplo2 (t: (nat * nat * nat) ) : nat := 
  match t with
  | (n1, n2, n3) => cubo(n1) + cubo(n2) + cubo(n3)
  end.

Check ejemplo1.
Check ejemplo2.
Compute ejemplo1 Nat.div2 6.
Compute ejemplo2 (1,2,3).

(*Las funciones tambien pueden devolver funciones por medio de funciones anonimas
o funciones en linea*)
Definition ejemplo3 (n: nat) : nat -> nat := fun (x: nat) => n + x.

Check ejemplo3.
Check ejemplo3 3.
Check (ejemplo3 3) 2.
Compute ejemplo3 3 2.
Compute ejemplo3 6 7.

Definition ejemplo4 (n: nat): nat := ejemplo3 3 n.
Check ejemplo4.
Compute ejemplo4 7.
























