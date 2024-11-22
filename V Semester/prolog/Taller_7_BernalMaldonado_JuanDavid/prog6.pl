%punto6
rightTo(X, Y) :- X is Y + 1.
leftTo(X, Y) :- rightTo(Y, X).

riddle(Houses, FishOwner) :-
Houses = [
house(1, Nationality1, Color1, Cigar1, Beverage1, Pet1),
house(2, Nationality2, Color2, Cigar2, Beverage2, Pet2),
house(3, Nationality3, Color3, Cigar3, Beverage3, Pet3),
house(4, Nationality4, Color4, Cigar4, Beverage4, Pet4),
house(5, Nationality5, Color5, Cigar5, Beverage5, Pet5)
],
 
member( house(_, britanico, rojo, _, _, _), Houses),
member( house(_, sueco, _, _, _, perro), Houses),
member(	house(_, danes, _, _, te, _), Houses),
member(	house(_, _, verde, _, cafe, _), Houses),
member( house(_, _, _, pallMall, _, pajaro), Houses),
member( house(_, _, amarillo, dunhill, _, _), Houses),
member( house(3, _, _, _, leche, _), Houses),
member( house(1, noruego, _, _, _, _), Houses),
member( house(_, _, _, bluemasters, cerveza, _), Houses),
member( house(_, aleman, _, prince, _, _), Houses),
member( house(A, _, verde, _, _, _), Houses),
member( house(B, _, blanco, _, _, _), Houses),
(leftTo(A, B)),
member( house(C, _, _, brends, _, _), Houses),
member( house(D, _, _, _, _, gato), Houses),
(rightTo(C, D) ; leftTo(C, D)),
member( house(E, _, _, _, _, caballo), Houses),
member( house(F, _, _, dunhill, _, _), Houses),
(rightTo(E, F) ; leftTo(E, F)),
member( house(G, noruego, _, _, _, _), Houses),
member( house(H, _, azul, _, _, _), Houses),
(rightTo(G, H) ; leftTo(G, H)),
member( house(I, _, _, brends, _, _), Houses),
member( house(J, _, _, _, agua, _), Houses),
(rightTo(I, J) ; leftTo(I, J)),
    
member( house(_, FishOwner, _, _, _, fish), Houses).