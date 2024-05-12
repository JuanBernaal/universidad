/*
Autor: Oscar Vargas Pabon, Juan David Bernal
Fecha: 18/04/2024

Un generador con queries aleatorias para probar la implementacion de la cache
*/

#include <iostream>
#include <random>
#include <ctime>

const int tamano = 3072;
const int wordBitSize = 8; // 1 byte

int main(  ) {
	
	int Instrucciones; std::cin >> Instrucciones;
	
	std::mt19937 mt( time(NULL) );

	std::cout << tamano << '\n';
	for ( int i = 0 ; i < tamano ; ++i ) std::cout << mt() % ( 1 << wordBitSize ) << '\n';
	
	std::cout << Instrucciones << '\n';
	
	for ( int i = 0 ; i < Instrucciones ; ++i ) {
		int type = mt()&1, addr = mt()%tamano;
		
		std::cout << type << ' ' << addr;
		if ( type == 0 ) {
			int val = mt() % ( 1 << wordBitSize );
			std::cout << ' ' << val;
		}
		std::cout << '\n';
	}
	
	return 0;
}