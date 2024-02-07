Definition nor (a b : bool) : bool :=
    match a, b with 
    | false, false => true
    | -, - => false
    end.

Example testNor1 : nor false false = true.
Proof. simpl. reflexivity. Qed.