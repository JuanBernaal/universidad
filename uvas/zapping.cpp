/* 
Author: Juan David Bernal Maldonado.
MM/DD/YY: 01/08/2024.
UVA: 12468 - Zapping.
*/

#include <iostream>

using namespace std;

int main(){
    int current, next, ans, absolute;

    cin >> current >> next;
    while(current != -1 && next != -1){
        if(current == 0)
            current = 100;
        if(next == 0)
            next = 100;   
        absolute = abs(current - next); 
        if(absolute > 50){
            absolute = abs(absolute - 100);
        }
        cout << absolute << endl;
        cin >> current >> next;
    }

    return 0;
}