/* 
Author: Juan David Bernal Maldonado.
MM/DD/YY: 05/11/2024.
UVA: 11332 - Summing Digits.
*/

#include <iostream> 

using namespace std;

int main() {
	int n;
	while ( cin >> n && n != 0 ) {
		int ans = 0, tmp = 0;
		while ( n != 0 ) {
			ans += n % 10;
			n /= 10;
		} while ( ans > 9 ) {
			tmp = 0;
			while ( ans != 0 ) {
				tmp += ans % 10;
				ans /= 10;
			}
			ans = tmp;
		}
		cout << ans << endl;
	}
	return 0;
}