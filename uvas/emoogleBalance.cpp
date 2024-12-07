/*
Author: Juan David Bernal Maldonado.
MM/DD/YY: 05/11/2024.
UVA: 12279 - Emoogle Balance.
*/

#include <iostream>

using namespace std;

int main() { 
	int N , u = 0;
	while( cin >> N && N != 0) {
		int event, ans = 0;
		for( int i = 0; i < N; i++ ) {
			cin >> event;
			if ( event == 0 ) ans--;
			else if ( event > 0) ans++; 
		}
		u++;
		cout << "Case " << u << ": " << ans << endl; 
	}

	return 0;
}