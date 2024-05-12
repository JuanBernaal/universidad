/*
Autor: Oscar Vargas Pabon, Juan David Bernal
Fecha: 18/04/2024

una simulacion de la DRAM
*/

#ifndef MEM_DRAM_H
#define MEM_DRAM_H

#include <vector>
#include "memory.h"

class DRam : public Memory {
	private:
	std::vector<Word> mem;
	public:
	// constructores
	DRam( int );
	DRam( std::vector<Word> );
	
	// metodos
	void write( int, Word ) override;
	int read( int ) override;
	std::list<std::pair<int,int>> getReport() override;
	
	~DRam();
};



#endif