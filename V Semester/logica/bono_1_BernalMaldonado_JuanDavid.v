Section Bono1.

(*H0: Todo lobo persigue algun conejo.
  H1: Todo conejo que es cafe es astuto.
  H2: Ningun lobo es capaz de atrapar a un conejo astuto.
  H3: Cualquier lobo que persigue a un conejo pero no logra atraparlo, esta
      enojado.
  Prueba: Por lo tanto, si todos los conejos son cafes, entonces,
  todos los lobos estan enojados.*)

(*P: Es lobo.
  Q: Es conejo.
  R: persigue a.
  S: es cafe.
  T: Es astuto.
  V: Atrapa a.
  U: Esta enojado.*)

Variable domain: Set.
Variable x y z : domain.
Variable (P Q S T U: domain-> Prop) (R V: domain -> domain -> Prop).


(*** Hipotesis fundamentales para el razonamiento: ***)
Hypothesis H0: forall l: domain, (P l -> (exists c: domain, (Q c /\ R l c ))).
Hypothesis H1: forall c: domain, (Q(c) /\ S(c) -> T(c)).
Hypothesis H2: forall l c: domain, (Q(c) /\ T(c)) -> (P(l)  /\ ~V l c).
Hypothesis H3: forall l c: domain, (P(l) /\ Q(c) /\ R l c /\ ~V l c) -> U(l).
Lemma bono1: ( forall c: domain, Q(c) /\ S(c) ) -> (forall l: domain, P(l) -> U(l)).

Proof.

intros.
apply H0 in H4.
destruct H4.
destruct H4.
assert( H7 := H3 l ).
assert( H8 := H7 x0 ).
apply H8.
split.
assert( H9 := H2 l ).
assert( H10 := H9 x0 ).
apply H10.
split.
exact H4.
assert( H11 := H1 x0 ).
apply H11.
assert( H12 := H x0 ).
exact H12.
split.
exact H4.
split.
exact H5.
assert( H9 := H2 l ).
assert( H10 := H9 x0 ).
apply H10.
split.
exact H4.
assert( H11 := H1 x0 ).
apply H11.
assert( H12 := H x0 ).
exact H12.
Qed.

End Bono1.
