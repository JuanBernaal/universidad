/*
Autor: Oscar Vargas Pabon
Fecha: 4/02/2024

ojala funcione
*/

#ifndef THE_ASSEMBLER
#define THE_ASSEMBLER

#include "readSpecs.cpp"
#include <bitset>

using namespace std;

int startOfProgram;

map<string, int> tags;

#define InstructionBits 32

/* The class TagPlaceHolder represents a placeholder for a tag with various attributes such as tag
name, type names, instruction index, and type. */
class TagPlaceHolder {
public:
	string tagName;
	string typeSpecName, typeName;
	int instructionIndex, type;
	TagPlaceHolder() = default;
	TagPlaceHolder( const string & tn, const string &tpn, const string &tsn, int ii, int type ) : tagName( tn ), typeName( tpn ), typeSpecName(tsn), instructionIndex(ii), type( type ) {};
};

/**
 * The function `assemble` reads an input file, processes assembly instructions, and generates a vector
 * of bitsets representing the assembled instructions.
 * 
 * @param inFile The function `assemble` reads instructions from a file specified by the `inFile`
 * parameter, processes them, and returns a vector of bitsets representing the assembled instructions.
 * 
 * @return The function `assemble` returns a vector of bitsets, where each bitset represents an
 * assembled instruction.
 */
vector<bitset<InstructionBits>> assemble( char *inFile ) {
	FILE *rawAssemble = fopen( inFile, "r" );
	personalizedThrow = CloseAbruptly( rawAssemble );

	list<TagPlaceHolder> allTags;
	int instructionIndex = 0;

	vector<bitset<InstructionBits>> res;
	bitset<InstructionBits> act;
	vector<string> tokens = tokenize_line( rawAssemble );
	int ind, number, tope, i;
	while ( tokens.size() > 0 ) {
		if ( tokens.size() == 2 && isFunction( tokens[0], isChar ) && tokens[1] == ":" ) {
			tags[tokens[0]] = instructionIndex;
			tokens = tokenize_line( rawAssemble );
			continue;
		}
		tokenAssert( instructions.count( tokens[0] ), tokens, 0 );
		ind = 1;
		act = bitset<InstructionBits>();
		for ( list<ArgumentType>::iterator it = instructions[tokens[0]].dynamic_inst.begin() ; it != instructions[tokens[0]].dynamic_inst.end() ; ++it ) {
			typeAssert( ind < tokens.size(), tokens, "instruction" );
			if ( it->type == REGISTER ) {
				tokenAssert( tokens[ind] == "$", tokens, ind );
				typeAssert( ind+1 < tokens.size(), tokens, "register_name" );
				typeAssert( registers.count( tokens[ind+1] ), tokens, tokens[ind+1] );
				number = registers[tokens[ind+1]];
				TypeSpec tmp = types[instructions[tokens[0]].type][it->correspondence];
				tope = tmp.start;
				for ( i = tmp.start + tmp.bits-1 ; i >= tope ; --i ) {
					act[i] = (number&1);
					number >>= 1;
				}
				if ( number != 0 ) {
					fprintf( stderr, "Error, the space allocated for the register is not enough to represent the number. This is an issue with the instructions_specifications ( particularly the <register> )\n" );
					personalizedThrow();
				}
				++ind; // uno extra porque lo compone el token de '$' y el nombre del registro
			} else if ( it->type == INMEDIATE ) {
				bool sign = true;
				if ( tokens[ind] == "-" ) {
					sign = false; // para leer los negativos
					typeAssert( ind+1 < tokens.size(), tokens, "Negative_inmediate" );
					++ind;
				}
				tokenAssert( isNumber( tokens[ind] ), tokens, ind );
				number = convertStringToNum( tokens[ind] );
				number = ( sign ) ? number : (~number)+1;
				
				TypeSpec tmp = types[instructions[tokens[0]].type][it->correspondence];
				tope = tmp.start;
				for ( i = tmp.start + tmp.bits-1 ; i > tope ; --i ) {
					act[i] = (number&1);
					number >>= 1;
				}
				if ( !sign ) {
					act[tope] = !sign;
				} else {
					act[tope] = (number&1);
				}
			} else if ( it->type == TAG ) {
				tokenAssert( isFunction( tokens[ind], isChar ), tokens, ind );
				allTags.push_back( TagPlaceHolder( tokens[ind], instructions[tokens[0]].type, it->correspondence, instructionIndex, TAG ) );
			} else if ( it->type == PSEUDOTAG ) {
				tokenAssert( isFunction( tokens[ind], isChar ), tokens, ind );
				allTags.push_back( TagPlaceHolder( tokens[ind], instructions[tokens[0]].type, it->correspondence, instructionIndex, PSEUDOTAG ) );
			} else if ( it->type == TOKEN ) {
				tokenAssert( tokens[ind] == it->correspondence, tokens, ind );
			}
			++ind;
		}
		for ( list<pair<string,int>>::iterator it = (instructions[tokens[0]].static_inst).begin() ; it != (instructions[tokens[0]].static_inst).end() ; ++it ) {
			number = it->second;
			TypeSpec tmp = types[instructions[tokens[0]].type][it->first];
			tope = tmp.start;
			for ( i = tmp.start + tmp.bits-1 ; i >= tope ; --i ) {
				act[i] = (number&1);
				number >>= 1;
			}
			if ( number != 0 ) {
				fprintf( stderr, "Error, the space allocated for the constant is not enough to represent the number. This is an issue with the instructions_specifications ( particularly the <static_inst> )\n" );
				personalizedThrow();
			}
		}

		res.push_back( act );

		tokens = tokenize_line( rawAssemble );
		instructionIndex += 4; // porque salta de 4 en 4
	}
	fclose( rawAssemble );
	personalizedThrow = CloseAbruptly( NULL );

	while ( !allTags.empty() ) {
		if ( !tags.count( allTags.front().tagName ) ) {
			fprintf( stderr, "Error: Ther tag: '" );
			printString( allTags.front().tagName, stderr );
			fprintf( stderr, "' used in line %d is never defined.\n", allTags.front().instructionIndex );
			personalizedThrow();
		}
		number = tags[allTags.front().tagName];
		if ( allTags.front().type == TAG ) {
			number += startOfProgram;
		} else if ( allTags.front().type == PSEUDOTAG ) {
			number = number - allTags.front().instructionIndex;
		}
		number >>= 2;

		TypeSpec tmp =  types[allTags.front().typeName][allTags.front().typeSpecName];
		tope = tmp.start;
		if ( allTags.front().type == PSEUDOTAG ) ++tope;
		for ( i = tmp.start + tmp.bits-1 ; i >= tope ; --i ) {
			act[i] = (number&1);
			number >>= 1;
		}
		if ( allTags.front().type == PSEUDOTAG ) {
			act[tmp.start] = ( tags[allTags.front().tagName] < allTags.front().instructionIndex );
		}

		allTags.pop_front();
	}
	return res;
}

#endif
