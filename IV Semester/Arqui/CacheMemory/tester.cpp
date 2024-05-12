/*
Autor: Oscar Vargas Pabon, Juan David Bernal
Fecha: 18/04/2024

para hacer el test que bota el generador
*/

#include <iostream>
#include <vector>
#include <stdio.h>

#include "cacheFA.h"
#include "memDRam.h"

const int cantidadBloques = 64;

void leerReporte( std::list<std::pair<int,int>> &report ) {
	int i = 0;
	while ( !report.empty() ) {
		fprintf( stderr, "El nivel %d reporta %d queries manejadas y %d misses\n", ++i, report.front().first, report.front().second );
		report.pop_front();
	}
}

void test( int numeroPrueba ) {
	int tamano; scanf( "%d", &tamano );
	std::vector<Word> strt( tamano );
	for ( int i = 0 ; i < tamano; ++i ) {
		int tmp; scanf("%d", &tmp );
		strt[i] = tmp;
	}
	
	Memory *memory = NULL;
	if ( numeroPrueba == 1 ) {
		fprintf( stderr, "Leyendo directamente de la DRam...\n" );
		memory = new DRam( strt );
	} else if ( numeroPrueba == 2 ) {
		fprintf( stderr, "Leyendo de la memoria Cache...\n" );
		memory = new CacheFA( cantidadBloques, new DRam( strt ) );
	} else {
		fprintf( stderr, "No se reconoce el numero de la prueba...\n" );
		return;
	}
			
	int inst; scanf( "%d", &inst );
	for ( int i = 0 ; i < inst ; ++i ) {
		int type, addr; scanf( "%d %d", &type, &addr );
		
		if ( type == 0 ) {
			int val; scanf( "%d", &val );
			memory->write( addr, val );
		} else {
			printf( "%d\n", memory->read( addr ) );
		}
		
	}
		
	std::list<std::pair<int,int>> tmp = memory->getReport();
	leerReporte( tmp );
	
	delete memory;
}

int main( int argc, char *argv[] ) {
	int numeroPrueba = 2;
	if ( argc > 1 && ( argv[1][0] == '-' && argv[1][1] == 'r' )) {
		numeroPrueba = 1;
	}
	
	try {
		test( numeroPrueba );
	} catch ( ... ) {
		fprintf( stderr,"????????\n" );
	}
	return 0;
}

