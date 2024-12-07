%prog4
hombre(juan).
hombre(pedro).

tiene(maria, gato):- tiene(juan, perro).
tiene(pedro,gato):-tiene(pedro,perro).
tiene(laura,perro):-tiene(juan,perro),tiene(pedro,gato).
tiene(juan,gato):-tiene(maria,Mascota),tiene(pedro,Mascota).
tiene(Mascota,perro):-hombre(Mascota).