/* 
Author: Juan David Bernal Maldonado.
MM/DD/YY: 05/04/2024.
UVA: 10424 - Love Calculator.
*/

#include <iostream>
#include <algorithm>

using namespace std;

int sumarDigitos( int num ) {
    int originalNum = num;
    int copy = num;
    while( copy > 9) {
        int tmp = copy;
        copy = 0;
        while ( tmp != 0 ) { 
            copy += tmp % 10;
            tmp /= 10;
        }
    }
    return copy;
}

int main() { 
    string name1, name2;
    int sum;
    while (getline(cin, name1)) {
        int a, b;
        sum = 0; 
        getline(cin, name2);
        for (int i = 0; i < name1.size(); i++) {
            if (name1[i] >= 'A' && name1[i] <= 'Z') sum += name1[i] - 'A' + 1;
            else if (name1[i] >= 'a' && name1[i] <= 'z') sum += name1[i] - 'a' + 1;
        } 
        a = sumarDigitos(sum);
        sum = 0; 
        for (int i = 0; i < name2.size(); i++) {
            if (name2[i] >= 'A' && name2[i] <= 'Z') sum += name2[i] - 'A' + 1;
            else if (name2[i] >= 'a' && name2[i] <= 'z') sum += name2[i] - 'a' + 1;
        }
        b = sumarDigitos(sum);
        float ans = 0;
        if (a >= b) ans = (float) b / a;
        else if (a < b) ans = (float) a / b;
        ans *= 100;
        printf("%.2f", ans);
        cout << " %" << endl;
    }
    return 0;
}
