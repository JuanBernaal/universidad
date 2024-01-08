#include "lista.h"
#include <iostream>

/* 
  Juan David Bernal Maldonado.

  Complejidad de insertarEnListaOrdenada:
  Esta funcion tiene complejidad O(n) donde n es el peor caso.
  En esta funcion el peor caso sucede cuando la lista tiene a v
  al final entonces se debe recorrer la lista completamente.
*/

void insertarEnListaOrdenada(Lista& l, Elemento v){
  int i = 0;
  while(i < l.longLista()){
    if(l.infoLista(i) > v){
      l.insLista(v, i);
      return;
    }
    i++;
  }
  l.anxLista(v);
}

int main(){
  Lista l;
  l.anxLista(5);
  l.anxLista(10);
  l.anxLista(12);
  l.anxLista(15);

  insertarEnListaOrdenada(l, 13);

  cout << "Valor posición 0: " << l.infoLista(1) << endl;
  cout << "Valor posición 1: " << l.infoLista(2) << endl;
  cout << "Valor posición 2: " << l.infoLista(3) << endl;
  cout << "Tamaño: " << l.longLista() << endl;

  l.insLista(13, 2);

  cout << "Tamaño: " << l.longLista() << endl;
  cout << "Elementos Lista:" << endl;

  int i;
  for(i = 1; i <= l.longLista(); i++){
    cout << l.infoLista(i) << " ";
  }
  cout << endl;

  if(l.vaciaLista())
    cout << "Lista Vacía" << endl;
  else
    cout << "Lista No Vacía" << endl;

  l.elimLista(1);
  l.elimLista(3);

  cout << "Elementos Lista:" << endl;
  for(i = 1; i <= l.longLista(); i++){
    cout << l.infoLista(i) << " ";
  }
  cout << endl;

  return 0;
}
