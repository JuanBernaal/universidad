/* 
Author: Juan David Bernal Maldonado.
MM/DD/YY: 05/10/2024.
UVA: 12372 - Packing for Holiday.
*/

#include <iostream>

using namespace std;

int main() { 
	int cases, L, W, H;
	cin >> cases;
	for ( int i = 0; i < cases; ++i ) { 
		cin >> L >> W >> H;
		if ( L < 21 && W < 21 && H < 21 ) cout << "Case " << i + 1 << ": good" << endl;
		else cout << "Case " << i + 1 << ": bad"  << endl;
	}
	return 0;
}