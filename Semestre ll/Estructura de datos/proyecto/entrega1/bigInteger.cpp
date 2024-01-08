#include "bigInteger.h"
#include <string>
#include <iostream> 
#include <vector>
#include <algorithm>

int charToInt(char c){
    int ans = c - 48;
    return ans;
}

bool isEqual(vector<int> v, vector<int> v2){
    bool ans = false;
    if(v.size() == v2.size()){
        int i = 0;
        while(v[i] == v2[i]){
            i++;
        }
        if(i == v.size()){
            ans = true;
        }
    }else{
        ans = false;
    }
    return ans;
}

BigInteger::BigInteger(){                               /* Constructor predeterminado. */
}

BigInteger::BigInteger(string strg){                    /* Constructor. */
    sign = 1;
    for(int i = strg.size() - 1; i >= 0; i--){
        if(strg[0] == '-')
            sign = -1;
        else{
            int var = charToInt(strg[i]);
            number.push_back(var);
        }
    } 
}

void BigInteger::printBigInteger(){                     /* Imprimir el numero. */
    for(int i = number.size() - 1; i >= 0; i--){
        cout << number[i];
    }
    printf("\n");
}

int BigInteger::len(){
    return number.size();
}

int BigInteger::info(int pos){
    return number[pos];
}

vector<int> BigInteger::value(){
    vector<int> ans = number;
}

BigInteger BigInteger::operator+ (BigInteger &num){
    BigInteger ans;
    int sum = 0, carry = 0;
    int n1 = number.size();
    int n2 = num.len();
    for(int i = 0; i < max(n1, n2); i++){
        if((i < n1) && (i < n2)){
            sum = number[i] + num.info(i);
            if(carry == 1){
                carry--;
                sum++;
            }if(sum > 9){
                sum -= 10;
                carry++;
            }
        }else{
            if(n1 > i){
                sum = number[i];
            }else{
                sum = num.info(i);
            }
        }
        ans.number.push_back(sum);
    }
    return ans;
}

BigInteger BigInteger::operator- (BigInteger &num){
    BigInteger ans;
    return ans;
}

BigInteger BigInteger::operator* (BigInteger &num){
    BigInteger ans;
    return ans;
}

BigInteger BigInteger::operator/ (BigInteger &num){
    BigInteger ans;
    return ans;
}

BigInteger BigInteger::operator% (BigInteger &num){
    BigInteger ans;
    return ans;
}

bool BigInteger::operator== (BigInteger &num){
    bool ans;
    return ans;
}

bool BigInteger::operator< (BigInteger &num){
    bool ans = false;
    if(number.size() < num.len()){
        ans = true;
    }else if(number.size() == num.len()){
        if(number[number.size() - 1] < num.info(num.len() - 1)){
            return true;
        }
    }
    return ans;
}

bool BigInteger::operator<= (BigInteger &num){
    bool ans = false;
    if(number.size() < num.len()){
        ans = true;
    }else if(number.size() == num.len()){
        if(number[number.size() - 1] < num.info(num.len() - 1)){
            return true;
        }
    }else if(isEqual(number, num.value())){
        ans = true;
    }
    return ans;
}

void BigInteger::add(BigInteger &num){

}
void BigInteger::product(BigInteger &num){

}
void BigInteger::substract(BigInteger &num){

}
void BigInteger::quotient(BigInteger &num){

}
void BigInteger::remainder(BigInteger &num){

}
void BigInteger::pow(BigInteger &num){

}
string BigInteger::toString(){

}