#include <stack>
#include <iostream>
#include <list>
#include <queue>
#include <map>

using namespace std;

/* ======================================= Punto 1 ======================================= */

/*  
    La complejidad de esta operacion es de O(n), donde n es la cantidad de datos que tenga
    la pila inicial. Esto es porque el primer ciclo lo que hace es vaciar la cola, mientras
    que el segundo ciclo se encarga de devolver los elementos que no fueron eliminados a la 
    pila original.
*/

void eliminarPosicionesPila(stack<int>& pil, list<int>& l){
    stack<int> tmp;
    while(!pil.empty()){
        tmp.push(pil.top());
        pil.pop();
    }
    int i = 0;
    while(!tmp.empty()){
        if(i != l.front()){
            pil.push(tmp.top());
        }else{
            l.pop_front();
        }
        tmp.pop();
        i++;
    }
}

/* ======================================= Punto 2 ======================================= */

/* 
    La complejidad de esta funcion es O(n log n) por las funciones pop_heap y push_heap.
*/

void ordenarConMonticulo(vector<int>& vec){
    make_heap(vec.begin(), vec.end());
    for(int i = vec.size() - 1; i >= 0; i--){
        pop_heap(vec.begin(), vec.begin() + i + 1);
        push_heap(vec.begin(), vec.begin() + i);
    }
}

/* ======================================= Punto 3 ======================================= */

/*  
    La complejidad de esta operacion es de O(n) donde n es la cantidad de datos que tenga la cola
    ya que el ciclo itera mientras la cola no este vacia.
    
*/

bool verificarOrdenadoCola(queue<int> q){
    bool ans = false, ascending = true, descending = true;
    int prev = q.front();
    q.pop();
    while(!q.empty()){
        int current = q.front();
        if(prev < current)
            descending = false;
        if(prev > current)
            ascending = false;
        q.pop();
        prev = current;
    }
    if(ascending || descending)
        ans = true;
    return ans;
}

/* ======================================= Punto 4 ======================================= */

/* 
    La complejidad de esta operacion es O(n) donde n representa la longitud de la lista l, 
    todo lo que esta anidado al ciclo while, se ejecutara n veces. Pero el uso del sort
    hace la complejidad sea O(n log n). 
*/

int obtenerMenorCosto(list<int> l){
    l.sort();
    list<int>::iterator it = l.begin();
    int sum, ans = 0, prev = *it;
    while(it != l.end()){
        it++;
        sum = prev + *it;
        prev = sum;
        ans += sum;
    }
    return ans;
}

/* ======================================= Punto 6 ======================================= */

/* 
    La complejidad de esta operacion es O(n), esto es porque el primer ciclo se itera n veces,
    siendo n el numero de datos que hay en cola. El segundo ciclo se itera n veces pero n es 
    el tamaño del mapa.
*/

int verificarRepetidos(queue<int> col){
    int ans;
    map<int, int> mapa;
    
    while(!col.empty()){
        int tmp = col.front();
        col.pop();
        mapa[tmp]++;
    }
    for(map<int, int>::iterator it = mapa.begin(); it != mapa.end(); it++){
        if(it->second > 1){
            ans++;
        }
    }
    return ans;
}

/* ======================================= Punto 7 ======================================= */

/*  
    La complejidad de esta operacion es O(n), donde n es el tamaño de la cadena.
*/

map<char, list<int>> obtenerPosicionesOcurrencias(string &cad){
    map<char, list<int>> mapita;
    for(int i = 0; i < cad.size(); i++){
        mapita[cad[i]].push_back(i);
    }
    return mapita;
}

/* ======================================= Punto 8 ======================================= */

/*  
    La complejidad de esta operacion es O(n^2), la complejidad del primer ciclo es n, donde n
    es el tamaño la matriz. El segundo ciclo tambien es n, donde n es el tamaño de cada lista
    interna de la matriz. Como j esta anidado al ciclo de i, entonces la complejidad se vuelve 
    O(n*n) = O(n^2);
*/

vector<list<pair<int, int>>> crearMatrizDispersa(vector<vector<int>> mat){
    vector<list<pair<int, int>>> ans;
    for(int i = 0; i < mat.size(); i++){
        ans.push_back({});
        for(int j = 0; j < mat[i].size(); j++){
            if(mat[i][j] != 0){
                ans[i].push_back(make_pair(j, mat[i][j]));
            }
        }
    }
    return ans;
}

/* ======================================= Punto 9 ======================================= */

/*  
    La complejidad de esta operacion es O(n), en el primer ciclo n depende de la cantidad de datos
    que tenga la cola y el segundo ciclo se itera n veces en el peor caso si no se encuentra
    que ans es verdadera.
*/

bool verificarRepetidosCola(queue<int> q){
    bool ans = false;
    map<int, int> mapa;
    
    while(!q.empty()){
        int tmp = q.front();
        q.pop();
        mapa[tmp]++;
    }
    for(map<int, int>::iterator it = mapa.begin(); it != mapa.end() && !ans; it++){
        if(it->second > 1){
            ans = true;
        }
    }
    return ans;
}   

/* ======================================= Punto 10 ======================================= */

/*  
    La complejidad de este codigo es O(n), donde n puede ser la cantidad de datos en la cola 
    o el entero N que recibe la funcion.
*/ 

stack<int> filtrarNParesCola(queue<int> col, int N){
    stack<int> ans;
    int cont = 0;
    while(!col.empty() && cont <= N){
        if(col.front() % 2 == 0){
            if(cont < N){
                ans.push(col.front());
                cont++;
            }
        }
        col.pop();
    }
    return ans;
}
