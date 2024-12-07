Section Taller6.
Variable sigma: Set.
Variable x y z: sigma.
Variable (P1 P2: sigma-> Prop) (P3: sigma -> sigma -> Prop).
(*1*)
Theorem punto1: (forall a: sigma, P2 a -> ~exists b: sigma, P1 b) /\ (forall b: sigma, P1 b) -> forall a: sigma, ~ P2 a.
Proof.
intros H x0 H1.
destruct H.
apply H in H1.
destruct H1.
exists x0.
apply H0.
Qed.

(*2*)
Theorem punto2: ~(forall a: sigma, P1 a) -> ~ forall a: sigma, P1 a /\ P2 a.
Proof.
intros H H1.
apply H.
destruct H.
intros.
apply H1.
Qed.


(*3*)

Theorem punto3: (forall a: sigma, ~P2 a) -> ~exists a: sigma, P2 a.
Proof.
intros H H1.
destruct H1.
apply H in H0.
apply H0.
Qed.

(*4*)
Theorem punto4: ~(forall a: sigma, P1 a /\ P2 a) /\ (forall a: sigma, P2 a) -> ~forall a: sigma, P1 a.
Proof.

intros.
destruct H.
intros c.
destruct H.
split.
apply c.
apply H0.
Qed.

(*5*)
Theorem punto5: (exists a: sigma, P1 a \/ P2 a) -> (forall a: sigma, ~ P1 a) -> exists a: sigma, P2 a.
Proof.
intros.
destruct H.
exists x0.
destruct H.
apply H0 in H.
contradiction.
exact H.
Qed.

(*6*)
Lemma punto6: (exists a: sigma, P1 a \/ P2 a) <-> (exists a: sigma, P1 a) \/ (exists a: sigma, P2 a).
Proof.
split.
intros.
destruct H.
destruct H.
left.
exists x0.
exact H.
right.
exists x0.
exact H.
intros.
destruct H.
destruct H.
exists x0.
left.
exact H.
destruct H.
exists x0.
right.
exact H.
Qed.

(*7*)
Lemma punto7: forall b: sigma, (forall a: sigma, P2 a) -> exists a: sigma, P2 a.
Proof.
intros.
exists b.
apply H.
Qed.

(*8*)
Lemma punto8: (forall a b: sigma, P3 a b) -> forall b a: sigma, P3 a b.
Proof.
intros.
apply H.
Qed.

(*9*)
Lemma punto9: (exists a: sigma, P1 a -> P2 a) -> (forall a: sigma, P1 a) -> exists a: sigma, P2 a.
Proof.
intros.
destruct H.
exists x0.
apply H in H0.
exact H0.
Qed.

(*10*)
Lemma punto10: ~(exists a: sigma, P2 a) <-> forall a: sigma, ~P2 a.
Proof.
split.
intros H x0 H1.
destruct H.
exists x0.
exact H1.
intros H H1.
destruct H1.
apply H in H0.
exact H0.
Qed.



(*11*)
Lemma punto11: (forall a: sigma, P2 a -> P1 a) -> (forall a: sigma, P2 a) -> forall a: sigma, P1 a.
Proof.
intros.
apply H.
apply H0.
Qed.

(*12*)
Lemma punto12: (forall b a: sigma, P3 b a) -> (forall a: sigma, P3 a a).
Proof.
intros.
apply H.
Qed.


End Taller6.