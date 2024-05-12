#ifndef BIGINTEGER_H
#define BIGINTEGER_H

#include <string>
#include <iostream>
#include <vector>

using namespace std;

class BigInteger{
    private:
        vector<int> number;
        int sign;
    public:
        BigInteger();
        BigInteger(string num);
        
        void printBigInteger();

        int len();
        int info(int pos); 
        vector<int> value();

        BigInteger operator+ (BigInteger &num); 
        BigInteger operator- (BigInteger &num);
        BigInteger operator* (BigInteger &num);
        BigInteger operator/ (BigInteger &num);
        BigInteger operator% (BigInteger &num);
        bool operator== (BigInteger &num);
        bool operator< (BigInteger &num);
        bool operator<= (BigInteger &num);

        void add(BigInteger &num);
        void product(BigInteger &num);
        void substract(BigInteger &num);
        void quotient(BigInteger &num);
        void remainder(BigInteger &num);
        void pow(BigInteger &num);
        string toString();
};

#endif
