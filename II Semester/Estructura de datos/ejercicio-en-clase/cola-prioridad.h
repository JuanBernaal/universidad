#ifndef  COLAPRIORIDAD_H
#define COLAPRIORIDAD_H

#include "lista.h"

typedef int Elemento;
typedef int Prioridad;

class ColaPrioridad{
   Lista l;

   public:
      ColaPrioridad(); // crearCola
      Elemento front();
      void deque();
      void enqueue(Elemento);
      void enqueuePrioridad(Elemento, Prioridad);
      bool vaciaCola();
};

#endif
