#include <cstdio>
#include <queue>
#include <string>
#include "cola-prioridad.h"

class Estudiante{
   public:
      string nombre, codigo;
      double nota;

      Estudiante(){}
      Estudiante(string n, string c, double d){
	nombre = n;
	codigo = c;
	nota = d;
      }
};

void imprimirElementos(ColaPrioridad &c){
  while(!c.vaciaCola()){
     printf("%d\n",  c.front());
     c.deque();
  }
}

void imprimirElementos(queue<int> &que){
  while(!que.empty()){
      printf("%d\n",  que.front());
      que.pop();
  }
}

double promedioEstudiantes(queue<Estudiante> &q){
   double ans = 0;
   int tam = q.size();
   Estudiante est;
   while(!q.empty()){
      est = q.front();
      ans += est.nota;
      q.pop();
   }

   ans /= tam;
   return ans;
}

int main(){
   ColaPrioridad c;
   c.enqueue(1);
   c.enqueue(4);
   c.enqueue(6);
   c.enqueue(8);
   imprimirElementos(c);
   if(c.vaciaCola()){
      printf("El profesor dijo la verdad y la cola quedó vaciá\n");
   }
   else{
      printf("El profesor mintió y creo que no sabe de estructuras\n");
   }

   queue<int> q;
   q.push(4);
   q.push(10);
   q.push(8);
   q.push(7);
   q.push(9);
   imprimirElementos(q);

   queue<Estudiante> colaEst;
   colaEst.push(Estudiante("Cartman", "3323232", 1.5));
   colaEst.push(Estudiante("Butters", "4434343", 4.5));
   colaEst.push(Estudiante("Kyle", "111111", 3.5));
   colaEst.push(Estudiante("Kenny", "2221211", 2.5));

   double res = promedioEstudiantes(colaEst);
   printf("Promedio = %.3f\n", res);
   return 0;
}