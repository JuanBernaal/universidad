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