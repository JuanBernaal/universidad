/* 
Author: Juan David Bernal Maldonado.
MM/DD/YY: 05/06/2024.
UVA: 11614 - Etruscan Warriors Never Play Chess.
*/

#include <iostream>

using namespace std;

int main() {
    long long a, cases, warriors, ans;
    cin >> cases;
    for ( int i = 0; i < cases; i++ ) {
        cin >> warriors;
        a = 0, ans = 0;
        for ( int j = 1; a <= warriors; j++ ) {
            a += j;
            ++ans;
        }
        cout << ans - 1 << endl;
    }
    
    return 0;
}