/* 
Author: Juan David Bernal Maldonado.
MM/DD/YY: 12/15/2024.
UVA: 280 - Vertex.
*/

#include <bits/stdc++.h>

using namespace std;

void bfs ( int init, vector<vector<int>> &g, vector<bool> &visited ) {
    queue<int> q;

    q.push(init);
    //visited[init] = true;

    while( !q.empty() ) {
        int tmp = q.front();
        q.pop();
        
        for ( int i = 0; i < g[tmp].size(); i++ ) {
            int adj = g[tmp][i];
            if ( !visited[adj] ) {
                q.push(adj);
                visited[adj] = true;
            }
        }
    }
}

void dfs ( int actual, vector<vector<int>> &g, vector<bool> &visited ) {
    if ( !visited[actual] ) {
        visited[actual] = true;

        for ( int i = 0; i < g[actual].size(); i++ ){
            int adj = g[actual][i];
            dfs( adj, g, visited );
        }
    }
}

int main() {
    int n;
    string edge, search;

    while( cin >> n && n != 0 ){ 
        vector<vector<int>> g(n);
        cin.ignore();

        while ( getline( cin, edge ) && edge != "0" ) {
            int vertex = edge[0] - 49;                         // Starting Vertex.
            
            for ( int i = 2; i < edge.size(); i+=2 ){          // Edge directed from SV.
                if ( edge[i] != '0' ) 
                    g[vertex].push_back(edge[i] - 49);         // Creates the directed graph.
            }
        }
        getline( cin, search );   
        vector<vector<int>> ans;                             // Starting vertices;
        
        for ( int i = 2; i <= search.size(); i+=2 ) {
            int cont = 0;
            vector<bool> visited( n, false );
            vector<bool> ans;
            bfs( search[i] - 49, g, visited );

            for ( int j = 0; j < visited.size(); j++ ) {    
                if ( !visited[j] ) 
                    cont++;
            }
            cout << cont << ' ';

            for ( int j = 0; j < visited.size(); j++ ) {
                if ( !visited[j] ) {
                    cout << j + 1;  
                    if ( j < visited.size() ) {
                        cout << ' '; 
                    }
                }
            }
            cout << endl;
        }
    }
    return 0;
}