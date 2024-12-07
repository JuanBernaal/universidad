/* 
Author: Juan David Bernal Maldonado
MM/DD/YY: 05/10/2024
UVA: 11547 - Automatic Answer
*/

#include <iostream> 

using namespace std;

int main() {
	int cases, n;
	cin >> cases;
	for( int i = 0; i < cases; i++ ){
		cin >> n;
		n *= 567;
		n /= 9;
		n += 7492;
		n *= 235;
		n /= 47;
		n -= 498;
		n /= 10;
		cout << abs(n % 10) << endl;
	}
	
	return 0;
}