#include "bigInteger.h"
#include <stdio.h>
#include <string>
#include <string.h>

int main(){
    
    BigInteger num("12345");
    BigInteger num2("21223");
    BigInteger num3 = num + num2;
    printf("El resultado de la suma es: ");
    num3.printBigInteger();
    int suma = 12345 + 21223;
    printf("El resultado correcto de la suma es: %d\n", suma);

    return 0;
}