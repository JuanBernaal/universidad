/*
Juan David Bernal Maldonado
05/10/2024
Solution to UVa 12372.
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