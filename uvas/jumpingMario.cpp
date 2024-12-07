/* 
Author: Juan David Bernal Maldonado.
MM/DD/YY: 05/10/2024.
UVA: 11764 - Jumping Mario.
*/

#include <iostream>

using namespace std;

int main() {
	int cases, walls, tmp, bef;
	string jump;
	cin >> cases;
	for( int i = 0; i < cases; i++ ) {
		int high = 0, low = 0;
		cin >> walls;
		for( int j = 0; j < walls; j++ ) {
			cin >> tmp;
			if ( j == 0 ) bef = tmp;
			else {
				if ( bef < tmp ) high++;
				else if (bef > tmp) low++;
			}
			bef = tmp;
		}
		cout << "Case " << i + 1 << ": " << high << " " << low << endl; 
	}

	return 0;
}