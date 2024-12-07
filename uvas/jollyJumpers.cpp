/* 
Author: Juan David Bernal Maldonado.
MM/DD/YY: 12/06/2024.
UVA: 10038 - Jolly Jumpers.
*/

#include <iostream>
#include <vector>
	
using namespace std;

int main() {

	int cases, N, res, last;

	while( cin >> cases ){	
		vector<int> v(cases - 1);

		for( int i = 0; i < cases; i++ ) {
			cin >> N;
			if( i > 0) {
				res = abs(last - N);
				if ( res < cases && res > 0 )
					v[res - 1] = 1;
			}
			last = N;
		}
		
		bool jollyJumper = true;

		for( int i = 0; i < cases - 1; i++ ) {
			if( v[i] != 1 )
				jollyJumper = false;
		}

		if ( jollyJumper == true ) 
			cout << "Jolly" << endl;
		else 
			cout << "Not jolly" << endl;
	}
	return 0;
}