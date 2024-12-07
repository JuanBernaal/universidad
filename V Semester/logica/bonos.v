Section Bono1.
Variable sigma: Set.
Variable x y z : sigma.
Variable (P Q S T U: sigma-> Prop) (R V: sigma -> sigma -> Prop).

Hypothesis H0: forall l: sigma, (P l -> (exists c: sigma, (Q c /\ R l c ))).
Hypothesis H1: forall c: sigma, (Q(c) /\ S(c) -> T(c)).
Hypothesis H2: forall l c: sigma, (Q(c) /\ T(c)) -> (P(l)  /\ ~V l c).
Hypothesis H3: forall l c: sigma, (P(l) /\ Q(c) /\ R l c /\ ~V l c) -> U(l).
Lemma bono1: ( forall c: sigma, Q(c) /\ S(c) ) -> (forall l: sigma, P(l) -> U(l)).

Proof.

(* Obtener X0 *)
intros.
apply H0 in H4.
destruct H4.
destruct H4.

(* Reformular H3 *)
assert( H7 := H3 l ).
assert( H8 := H7 x0 ).

(* Probar P l *)
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


(* Probar Q x0 y R l x0 *)
exact H4.
split.
exact H5.


(* Probar ~ V l x0 *)
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


Section Bono2.
Variable sigma: Set.
Variable x y z : sigma.
Variable (P Q S T U V W: sigma-> Prop) (R: sigma -> sigma -> Prop).

Hypothesis H0: forall m: sigma, (P m) -> exists s, ((Q s) /\ (R m s)).
Hypothesis H1: forall a s: sigma, (((Q(s)) /\ R x s -> (forall r: sigma, (S(r) -> R x r)))).
Hypothesis H2: forall r: sigma, (S(r) /\ (V(r) /\ T(r))).
Hypothesis H3: forall r: sigma, (T(r) -> U(r)).
Hypothesis H4: forall s: sigma, (W(s) /\ forall r: sigma, (U(r)) -> (~R s r)).
Lemma bono2: forall s: sigma, (W(s) -> ~P(s)).

Proof.

intros.
unfold not.
intros.


(* Encontrar x0  *)
assert( H6 := H0 s ).
apply H6 in H5.
destruct H5.
destruct H5.


(* Reformular H4 en s y x0*)
assert( H8 := H4 s ).
destruct H8.
assert( H10 := H9 x0 ).
apply H10.


(* Probar U x0 *)
assert( H11 := H3 x0 ).
apply H11.


(* Probar T x0 y R s x0*)
assert( H12 := H2 x0 ).
destruct H12.
destruct H13.
exact H14.
exact H7.

Qed.

End Bono2.
