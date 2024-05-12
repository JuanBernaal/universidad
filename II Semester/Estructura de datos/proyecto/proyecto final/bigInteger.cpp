#include "bigInteger.h"

/* Constructor predeterminado. */
BigInteger::BigInteger(){
}

/*  Constructor que hace una copia.
    Entrada: Un objeto BigInteger constante pasado por referencia.
    Descripción: Este constructor copia los datos privados del BigInteger
    que se le pasa como entrada en el objeto actual.
 */
BigInteger::BigInteger(const BigInteger &num){
    number = num.number;
    sign = num.sign;
}

/*  Constructor. 
    Entrada: Un string constante pasado por referencia.
    Descripción: El string que recibe este constructor se convierte
    en el numero privado del objeto BigInteger, además el constructor
    asigna el signo que tendrá el nuevo objeto BigInteger.
*/ 
BigInteger::BigInteger(const string &str){
    sign = 1;
    if(str[0] == '-')
        sign = -1;
    for(int i = str.size() - 1; i > 0; i--){
        int var = str[i] - 48;
        number.push_back(var);  
    }
    if(str[0] != '-'){
        int var = str[0] - 48;
        number.push_back(var);
    }
}

/*  Constructor valor absoluto.
    Entrada: Un vector de enteros constante y un entero constante.
    Descripción: Este constructor copia el vector de enteros y lo 
    almacena en su representacion del numero BigInteger. Ademas toma
    un entero que representara el signo que tendra esta nueva copia.
    Para propositos de mi proyecto, se utilizo este constructor para
    sacar el valor absoluto de un objeto BigInteger.
*/ 
BigInteger::BigInteger(const vector<int> &vec, const int n){
    number = vec;
    sign = n;
}

/*  Función removeLeadingZeros.
    Descripción: Esta función elimina todos los ceros que estan
    a la izquierda de un objeto BigInteger.
*/
void BigInteger::removeLeadingZeros(){
    while(number.size() > 1 && number.back() == 0){
        number.pop_back();
    }
}

/*  Sobrecarga operator+.
    Entrada: Un objeto BigInteger.
    Salida: Un objeto BigInteger.
    Descripción: Esta sobrecarga suma el objeto actual con el
    objeto pasado como parametro y posteriormente retorna el
    resultado de esa resta. Ninguno de los objetos con los que 
    se hacen las operaciones es modificado.
*/
BigInteger BigInteger::operator+(BigInteger &num){
    BigInteger ans;
    int sum = 0, carry = 0, i = 0;
    if(sign == num.sign){
        while(i < number.size() && i < num.number.size()){
            sum = number[i] + num.number[i] + carry;
            carry = sum / 10;
            sum %= 10;  
            ans.number.push_back(sum);
            i++;
        }
        ans.sign = sign;
        while(i < number.size()){
            sum = number[i] + carry;
            carry = sum / 10;  
            sum %= 10;  
            ans.number.push_back(sum);
            i++;
        }
        while(i < num.number.size()){
            sum = num.number[i] + carry;
            carry = sum / 10;  
            sum %= 10;  
            ans.number.push_back(sum);
            i++;
        }
        if(carry > 0){
            ans.number.push_back(carry);
        }
    }else{
        if(*this < num){
            BigInteger b1(num.number, 1), b2(number, 1);
            ans = b1 - b2;
        }else{
            BigInteger b1(number, 1), b2(num.number, 1);
            ans = b1 - b2;
        }        
    }
    return ans;
}

/*  Sobrecarga operator-.
    Entrada: Un objeto BigInteger.
    Salida: Un objeto BigInteger.
    Descripción: Esta sobrecarga retorna el resultado de restar
    el objeto actual con el objeto pasado como parametro. 
    Ninguno de los objetos con los que se hacen las operaciones 
    es modificado.
*/
BigInteger BigInteger::operator-(BigInteger &num){
    BigInteger ans, abs1(number, 1), abs2(num.number, 1);
    int diff = 0, borrow = 0, n1 = number.size(), n2 = num.number.size(), i = 0;
    if(sign == num.sign){
        if(abs1 == abs2){
            ans.number.push_back(0);
            ans.sign = 1;
        }else if(abs1 < abs2){
            ans = num - *this;
        }else{
            while(i < n1 && i < n2){
                diff = number[i] - borrow - num.number[i];
                if(diff < 0){
                    diff += 10;
                    borrow = 1;
                }else{
                    borrow = 0;
                }
                ans.number.push_back(diff);
                i++;
            }
            while(i < n1){
                diff = number[i] - borrow;
                if(diff < 0){
                    diff += 10;
                    borrow = 1;
                }else{
                    borrow = 0;
                }
                ans.number.push_back(diff);
                i++;
            }
            ans.removeLeadingZeros();
        }
    }else{
        BigInteger c1(number, 1), c2(num.number, 1);
        ans = c1 + c2;
    }
    if(abs1 < abs2)
        if(num.sign == -1)
            ans.sign = 1;
        else
            ans.sign = -1;
    else if(!(abs1 <= abs2) && sign == -1)
        ans.sign = -1;
    else
        ans.sign = 1;
    return ans;
}

/*  Sobrecarga operator*.
    Entrada: Un objeto BigInteger.
    Salida: Un objeto BigInteger.
    Descripción: Esta sobrecarga retorna el resultado de 
    multiplicar el objeto actual con el objeto pasado 
    como parametro. Ninguno de los objetos con los que se 
    hacen las operaciones es modificado.
*/
BigInteger BigInteger::operator*(BigInteger &num){
    BigInteger ans;
    int n1 = number.size(), n2 = num.number.size();
    vector<int> result(n1 + n2, 0);
    for(int i = 0; i < n1; i++){
        int carry = 0;
        for(int j = 0; j < n2; j++){
            int product = number[i] * num.number[j] + result[i + j] + carry;
            carry = product / 10;  
            result[i + j] = product % 10;
        }
        result[i + n2] = carry;
    }
    while(!result.empty() && result.back() == 0){
        result.pop_back();
    }
    ans.sign = sign * num.sign;
    ans.number = result;
    return ans;
}

/*  Sobrecarga operator/.
    Entrada: Un objeto BigInteger.
    Salida: Un objeto BigInteger.
    Descripción: Esta sobrecarga retorna el resultado de dividir
    el objeto actual con el objeto pasado como parametro. 
    Ninguno de los objetos con los que se hacen las operaciones 
    es modificado.
*/
BigInteger BigInteger::operator/(BigInteger& num){
    BigInteger zero("0"), ans;
    if(*this == zero || *this < num)
        ans = zero;
    else{
        BigInteger dividend = *this,  divisor = num, quotient("0"), remainder("0");
        for(int i = dividend.number.size() - 1; i >= 0; i--){
            BigInteger b1("10"), b2(to_string(dividend.number[i]));
            remainder = remainder * b1 + b2;
            int count = 0;
            while(!(remainder < divisor)){
                remainder = remainder - divisor;
                count++;
            }
            quotient.number.insert(quotient.number.begin(), count);
        }
        quotient.removeLeadingZeros();
        ans = quotient;
    }
    return ans;
}

/*  Sobrecarga operator%.
    Entrada: Un objeto BigInteger.
    Salida: Un objeto BigInteger.
    Descripción: Esta sobrecarga retorna el residuo de 
    una division entre el objeto actual y el pasado como
    parametro. Ninguno de los objetos con los que se hacen 
    las operaciones es modificado.
*/
BigInteger BigInteger::operator%(BigInteger& num) {
    BigInteger zero("0"), ans;
    if(*this == zero || *this < num){
        ans = *this;
    }else{
        BigInteger dividend = *this, divisor = num, remainder("0");
        for(int i = dividend.number.size() - 1; i >= 0; --i){
            BigInteger b1("10"), b2(to_string(dividend.number[i]));
            remainder = remainder * b1 + b2;
            while(!(remainder < divisor)){
                remainder = remainder - divisor;
            }
        }
        remainder.removeLeadingZeros();
        ans = remainder;
    }
    return ans;
}

/*  Sobrecarga operator==.
    Entrada: Un objeto BigInteger.
    Salida: Un booleano.
    Descripción: Esta sobrecarga retorna true si
    los dos objetos BigInteger son iguales, de
    no serlo, retorna false.
*/
bool BigInteger::operator==(BigInteger &num){
    return number == num.number && sign == num.sign;
}

/*  Sobrecarga operator<.
    Entrada: Un objeto BigInteger.
    Salida: Un booleano.
    Descripción: Esta sobrecarga retorna true si
    el objeto actual es menor que el pasado como parametro, 
    de no ser menor, retorna false.
*/
bool BigInteger::operator<(BigInteger &num){
    bool ans;
    if(sign != num.sign)
        ans = sign < num.sign;
    else if(number.size() != num.number.size()){
        if(sign == -1 && num.sign == -1)
            ans = number.size() > num.number.size();
        else
            ans = number.size() < num.number.size();
    }else{
        int i = num.number.size() - 1;
        while(number[i] == num.number[i])
            i--;
        if(sign == 1 && num.sign == 1)
            ans = number[i] < num.number[i];
        else
            ans = number[i] > num.number[i]; 
    }if(*this == num){
        ans = false;
    }
    return ans;
}

/*  Sobrecarga operator<=.
    Entrada: Un objeto BigInteger.
    Salida: Un booleano.
    Descripción: Esta sobrecarga retorna true si
    el objeto actual es menor o igual que el pasado 
    como parametro, de no serlo, retorna false.
*/
bool BigInteger::operator<=(BigInteger &num){
    bool ans = false;
    if(*this < num)
        ans = true;
    else if(*this == num)
        ans = true;
    return ans;
}

/*  Función add.
    Entrada: Un objeto BigInteger.
    Descripción: Esta función modifica el objeto actual,
    asignandole el resultado de sumar el objeto actual con el
    objeto pasado como parametro.
*/
void BigInteger::add(BigInteger &num){
    *this = *this + num;
}

/*  Función product.
    Entrada: Un objeto BigInteger.
    Descripción: Esta función modifica el objeto actual,
    asignandole el resultado de multiplicar el objeto actual 
    con el objeto pasado como parametro.
*/
void BigInteger::product(BigInteger &num){
    *this = *this * num;
}

/*  Función substract.
    Entrada: Un objeto BigInteger.
    Descripción: Esta función modifica el objeto actual,
    asignandole el resultado de restar el objeto actual con el
    objeto pasado como parametro.
*/
void BigInteger::substract(BigInteger &num){
    *this = *this - num;
}

/*  Función quotient.
    Entrada: Un objeto BigInteger.
    Descripción: Esta función modifica el objeto actual,
    asignandole el resultado de dividir el objeto actual 
    con el objeto pasado como parametro.
*/
void BigInteger::quotient(BigInteger &num){
    *this = *this / num;
}

/*  Función remainder.
    Entrada: Un objeto BigInteger.
    Descripción: Esta función modifica el objeto actual,
    asignandole el residuo de la division entre
    el objeto actual y el objeto pasado como parametro.
*/
void BigInteger::remainder(BigInteger &num){
    *this = *this % num;
}

/*  Función pow.
    Entrada: Un numero entero.
    Descripción: Esta función modifica el objeto actual,
    asignandole el resultado de elevar el objeto actual 
    al numero pasado como parametro.
*/
void BigInteger::pow(int num){
    BigInteger result("1");
    for(int i = 0; i < num; i++)
        result = result * *this;
    *this = result;
}

/*  Función toString.
    Salida: Un string.
    Descripción: Esta funcion toma el objeto actual 
    BigInteger y lo convierte en una cadena.
*/
string BigInteger::toString(){
    string ans;
    if(sign == -1)
        ans += "-";
    for(int i = number.size() - 1; i >= 0; i--){
        char l = number[i] + 48;  
        ans += l;
    }
    return ans;
}

/*  Función sumarListaValores.
    Entrada: Una lista de objetos BigInteger.
    Salida: Un BigInteger.
    Descripción: Esta función retorna el resultado
    de sumar todos los elementos de la lista pasada
    como parametro.
*/
BigInteger BigInteger::sumarListaValores(list<BigInteger> &l){
    BigInteger ans("0");
    for(list<BigInteger>::iterator it = l.begin(); it != l.end(); it++)
        ans.add(*it);
    return ans;
}

/*  Función multiplicarListaValores.
    Entrada: Una lista de objetos BigInteger.
    Salida: Un BigInteger.
    Descripción: Esta función retorna un objeto BigInteger, el cual
    es el resultado de multiplicar todos los elementos de la lista 
    pasada como parametro.
*/
BigInteger BigInteger::multiplicarListaValores(list<BigInteger> &l){
    BigInteger ans("1");
    for(list<BigInteger>::iterator it = l.begin(); it != l.end(); it++)
        ans.product(*it);
    return ans;
}
