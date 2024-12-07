%punto5
mujer(maria).
hombre(john).
sano(john).
sano(maria).
adinerado(john).
viajero(Persona) :- sano(Persona), adinerado(Persona).
viajar(X) :- viajero(X).