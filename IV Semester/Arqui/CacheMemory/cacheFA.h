/*
Autor: Oscar Vargas Pabon, Juan David Bernal
Fecha: 19/04/2024

representa 
*/

#ifndef CACHE_FA_H
#define CACHE_FA_H

#include "memory.h"
#include <vector>
#include <map>

#define BlockSize 32

class CacheFA : public Memory {
	private:
	
	std::map<int,int> tagLocation;
	// ¿de esta manera vamos a manejar el bloque?
	std::vector<std::vector<Word>> block;
	std::vector<int> tag;
	std::vector<bool> validBit;
	
	int FIFOhead;
	Memory *upperLevel;
	
	// funciones auxiliares
	static int getTag( int );
	static int getOffset( int );
	
	void handleMiss( int );
	
	public:
	// constructor
	CacheFA ( int, Memory * );
	
	// metodos
	void write( int, Word ) override;
	int read( int ) override;
	std::list<std::pair<int,int>> getReport() override;
	
	~CacheFA();
};

#endif