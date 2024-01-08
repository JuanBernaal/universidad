#include "lista.h"
#include "cola-prioridad.h"

ColaPrioridad::ColaPrioridad(){
}

Elemento ColaPrioridad::front(){
   Elemento ans = l.infoLista(1);
   return ans;
}

void ColaPrioridad::enqueue(Elemento e){
   l.anxLista(e);
}

void ColaPrioridad::enqueuePrioridad(Elemento e, Prioridad p){
    int pos = 1;
    while(pos <= l.longLista() && p <= l.infoLista(pos)){ 
         pos++;
    }
    l.insLista(e, pos);
}

void ColaPrioridad::deque(){
   l.elimLista(1);
}

bool ColaPrioridad::vaciaCola(){
  bool ans;
  if(l.vaciaLista())
     ans = true;
  else
     ans = false;
  return ans;
}
