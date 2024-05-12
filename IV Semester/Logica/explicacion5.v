Section LPO1.
Variable A : Set. (*Conjunto de variables (Dominio del discurso)*)
Variable x y z: A. (*algunas variables pertenecientes a A *)
Variables P Q : A -> Prop. (*Predicados logicos*)

(*Cambio de lugar*)
Lemma ex0: Q x = P x .
Proof.
symmetry.
Admitted.

(* Escritura de cuantificadores universales y existenciales:
  (forall x y : P x /\ Q y) 
  (exists x y : P x /\ Q y) 
*)

(*cuando forall este en el objetivo utilizar intro o intro x 
Esto asume una variable arbitraria x0 y la remplaza en el objetivo*)
Lemma ex1: forall x, (( P x -> Q x) -> P x )-> P x .
Proof.
intro .
(*intro y0.*)
intro.
Admitted.

(*cuando forall P(x) este en el contexto y P(x) donde x puede ser
cualquier variable particular (x, y, z) se puede utilizar apply H*)
Hypothesis H0: forall x, P x /\ Q x.
Lemma ex2: P y /\ Q y.
Proof.
apply H0.
Qed.

(*cuando forall este en el contexto, tambien se puede utilizar assert (H2 := H1 x)
lo cual indica que el forall se va a instanciar con la variable x y se llamara a 
esta nueva hipotesis H1 *)
Lemma ex3: P y /\ Q y.
Proof.
assert (H1 := H0 y).
assumption.
Qed.

End LPO1. 

Section LPO2.
Variable A : Set. (*Conjunto de variables (Dominio del discurso)*)
Variable x y z: A. (*algunas variables pertenecientes a A *)
Variables P Q : A -> Prop. (*Predicados logicos*)

(*cuando exists P(x) este en el objetivo, utilizar exists x donde x puede
ser cualquier variable particular (x, y, z) *)
Lemma ex4: (P y) -> (exists x, P x).
Proof.
intro.
exists y.
assumption.
Qed.

(*cuando exists este en el contexto utilizar destruct H o destruct H as [x0 H]
el cual instancia el existencial para una variable arbitraria x0*)
Lemma ex5: (exists x, ~P x) -> ~(forall x, P x).
Proof.
intro.
intro.
(*destruct H.*)
destruct H as [y0 H].
apply H.
apply H0.
Qed.

End LPO2.

Section natProofs.
Variable a b c d: nat. (*variables de tipo nat*)

(*definicion de suma *)
Fixpoint sumar (a b: nat): nat := 
  match a with
    |O => b
    |S a' => S (sumar a' b)
  end.

(*definicion de multiplicacion*)

Fixpoint multiplicar (a b: nat): nat := 
  match a with
    |O => O
    |S a' => sumar (multiplicar a' b) b
  end.


(*utilizar indcution para hacer pruebas por induccion *)
(*rewrite sirve para reescribir una objetivo a partir de una hipotesis
o Lemma/Theorem previamente probado *)
Theorem ex6: forall a, sumar a 1 =  S a.
Proof.
intro.
induction a0.
simpl.
reflexivity.
simpl.
rewrite IHa0.
(*rewrite -> IHa0.*)
(*rewrite <- IHa0.*)
reflexivity.
Qed.

(*utilizar rewrite con un teorema previo*)
Theorem ex7: forall n m : nat, (sumar n 1) * m = (S n) * m.
Proof.
pose proof ex6 as T.
intros.
rewrite T.
(*rewrite ex6.*)
reflexivity.
Qed.


(*es necesario en ciertas ocaciones realizar pequeñas pruebas dentro de otras pruebas
para esto se puede utilizar assert *)
Hypothesis conmutativa: forall a b, a + b = b + a.
Theorem plus_rearrange : forall n m p q : nat,
  (n + m) + (p + q) = (m + n) + (p + q).
Proof.
intros.
assert (H: n + m = m + n).
rewrite conmutativa. 
reflexivity.
rewrite H. 
reflexivity. 
Qed.

Theorem ex11: forall a b: nat, a + (b +  0) = a + b.
Proof.
intros.
assert (H: b0 + 0 = b0).
simpl.
rewrite conmutativa.
simpl.
reflexivity.
rewrite H.
reflexivity.
Qed.


Theorem ex11': forall a b: nat, a + (b + 0) = a + b.
Proof.
intros.
induction a0.
simpl.
induction b0.
reflexivity.
simpl.
rewrite IHb0.
reflexivity.
simpl.
rewrite IHa0.
reflexivity.
Qed.

End natProofs.