/* 
  Juan David Bernal Maldonado.
  Solucion al punto 1 y 2 de la tarea 5.
  
  Complejidades:
  - contarOcurrencias:
  Esta funcion tiene complejidad de O(n), donde n es el tamaño de la lista, 
  ya que se necesita recorrer siempre completa para contar la cantidad de 
  veces que aparece v. Y las complejidades de longLista e infolista
  no afectan el calculo del valor final ya que no son mayores que O(n).

  - obtenerMenores:
  Esta funcion tiene complejidad O(n), donde n es el tamaño de la lista que 
  se recorre completa para encontrar valores menores que v. Las funciones 
  utilizadas tampoco afectan el calculo final.
*/

#include "lista.h"
#include <iostream>

int contarOcurrencias(Lista l, int v){
  int cont = 0;
  for(int i = 0; i < l.longLista(); i++){
    if(l.infoLista(i) == v){
      cont++;
    }
  }
  return cont;
}

Lista obtenerMenores(Lista l, int v) {
  Lista list;
  for(int i = 0; i < l.longLista(); i++){
    if(l.infoLista(i) < v){
      list.anxLista(l.infoLista(i));
    }
  }
  return list;
}

int main(){
  Lista l;
  l.anxLista(5);
  l.anxLista(10);
  l.anxLista(12);
  l.anxLista(15);

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

  int ocurrencias = contarOcurrencias(l, 5); 
  Lista menores = obtenerMenores(l, 6);
  
  cout << "El valor aparece: " << ocurrencias << "veces en la lista." << endl;
  cout << "Elementos menores a v:";
  for(i = 1; i <= menores.longLista(); i++){
    cout << menores.infoLista(i) << " ";
  }

  return 0;
}
