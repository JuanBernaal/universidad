/*
    * Autor: Juan David Bernal Maldonado.
    * Fecha de creacion: 23 de Abril del 2023.
    * Proyecto final Estructuras de Datos 2023-1.
    * 
    * Archivo encabezado libreria TAD BigInteger.
    * Version: 1.0.
*/

#ifndef BIGINTEGER_H
#define BIGINTEGER_H

#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

class BigInteger{
    private:
        vector<int> number;
        int sign;
    public:
        BigInteger();
        BigInteger(const BigInteger &num);
        BigInteger(const string &str);
        BigInteger(const vector<int> &vec, const int n);

        void removeLeadingZeros();

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
        void pow(int num);
        string toString();

        static BigInteger sumarListaValores(list<BigInteger> &l);
        static BigInteger multiplicarListaValores(list<BigInteger> &l); 
};

#endif