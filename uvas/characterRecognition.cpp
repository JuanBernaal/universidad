/*
Autor: Juan David Bernal Maldonado.
MM/DD/YY: 05/11/2024.
*/

#include <iostream>

using namespace std;

int getNumber ( char a, char b ) {
	int ans;
	if ( a == '.' && b == '*') ans = 1;
	else if ( a == '*' && b == '.') ans = 2;
	else if ( a == '.' && b == '.' ) ans = 3;
	return ans;
}

int main() {
	string line;
	for(int i = 0; i < 4; i++){
		cin >> line;
	}
	cin >> line;
	int pen, prev, i = 0;
	while( i < line.size() ) {
		pen = line[i];
		prev = line[i + 1];
		i += 4;
		cout << getNumber( pen, prev );
	}
	cout << endl;
	cin >> line;
	return 0;
}