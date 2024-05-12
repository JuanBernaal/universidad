#include "biginteger.h"

int main(){
    int casos, n, i;
    string v1, v2, aux;
    BigInteger a("0"), b("0"), c("0");
    BigInteger cero("0");

    cin >> casos;
    cin.ignore();
    while(casos--){
	getline(cin, v1);
	getline(cin, v2);
	a = BigInteger(v1);
	b = BigInteger(v2);
	c = a + b;
	cout << a.toString() << " + " << b.toString() << " = " << c.toString() << endl;
	c = a - b;
	cout << a.toString() << " - " << b.toString() << " = " << c.toString() << endl;
	c = a * b;
	cout << a.toString() << " * " << b.toString() << " = " << c.toString() << endl;
	
	if(cero < a && cero < b){
	    c = a % b;
	    cout << a.toString() << " % " << b.toString() << " = " << c.toString() << endl;
	    c = a / b;
	    cout << a.toString() << " / " << b.toString() << " = " << c.toString() << endl;
	}
	if(a < b)
	    cout << a.toString() << " < " << b.toString() << endl;
	else if(b < a)
	    cout << b.toString() << " < " << a.toString() << endl;
	else if(a == b)
	    cout << a.toString() << " == " << b.toString() << endl;
	cout << a.toString() << " ** 10 = ";
	a.pow(10);
	cout << a.toString() << endl;
    }

    cin >> casos;
    cin.ignore();
    while(casos--){
		getline(cin, v1);
		a = BigInteger(v1);
		cout << a.toString() << endl;
		getline(cin, v2);
		b = BigInteger(v2);
		a.add(b);
		cout << a.toString() << endl;
		getline(cin, v2);
		b = BigInteger(v2);
		a.substract(b);
		cout << a.toString() << endl;
		getline(cin, v2);
		b = BigInteger(v2);
		a.product(b);
		cout << a.toString() << endl;
		getline(cin, v2);
		b = BigInteger(v2);
		if(cero < a && cero < b){
			a.quotient(b);
			cout << a.toString() << endl;
		}
		cin >> n;
		cin.ignore();
		a.pow(n);
		cout << a.toString() << endl;
		getline(cin, v2);
		b = BigInteger(v2);
		if(cero < a && cero < b){
			a.remainder(b);
		cout << a.toString() << endl;
		}
    }

    cin >> casos;
    while(casos--){
	cin >> n;
	cin.ignore();
	list<BigInteger> l;
	for(i = 0; i < n; ++i){
	    getline(cin, aux);
	    l.push_back(BigInteger(aux));
	}
	a = BigInteger::sumarListaValores(l);
	
	b = BigInteger::multiplicarListaValores(l);
	cout << a.toString() << endl;
	cout << b.toString() << endl;
    }

    return 0;
}
