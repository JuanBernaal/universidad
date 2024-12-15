/* 
Author: Juan David Bernal Maldonado.
MM/DD/YY: 12/14/2024.
UVA: 459 - graph connectivity.
*/

#include <bits/stdc++.h>

using namespace std;

void bfs( int init, vector<vector<int>> &G, vector<bool> &v ) {
    queue<int> q;
    q.push( init );
    v[init] = true;

    while ( !q.empty() ) {
        int next = q.front();
        q.pop();

        for ( int i = 0; i < G[next].size(); i++ ) {
            int adj = G[next][i];
            if ( !v[adj] ) {
                q.push( adj );
                v[adj] = true;
            }
        }
    }
}

int main() {
    int cases;
    cin >> cases;
    string blank;

    while( cases-- ) {
        string s;

        cin >> s;
        cin.ignore();
        int n = s[0] - 64;
        //creamos el grafo de tamaño n.
        vector<vector<int>> g(n);
        //creamos el vector de visitados en false porque no hemos visitado ninguno.
        vector<bool> visited(n, false);

        while ( getline( cin, s ) && s != "" ) {
            int x = s[0] - 65;
            int y = s[1] - 65;
            g[x].push_back(y);
            g[y].push_back(x);
        }
        int cont = 0;
        for ( int i = 0; i < n; i++ ) {
            if ( !visited[i] ) {
                bfs( i, g, visited );
                cont++;
            }
        }
        cout << cont << endl;
        if ( cases > 0 )
            cout << endl;
    }

    return 0;
}