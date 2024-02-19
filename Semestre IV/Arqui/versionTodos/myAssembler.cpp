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

class TagPlaceHolder {
public:
	string tagName;
	string typeSpecName, typeName;
	int instructionIndex, type;
	TagPlaceHolder() = default;
	TagPlaceHolder( const string & tn, const string &tpn, const string &tsn, int ii, int type ) : tagName( tn ), typeName( tpn ), typeSpecName(tsn), instructionIndex(ii), type( type ) {};
};

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
			typeAssert( !tags.count( tokens[0] ), tokens, "tag" );
			tags[tokens[0]] = instructionIndex;
			continue;
		}
		tokenAssert( instructions.count( tokens[0] ), tokens, 0 );
		ind = 1;
		act = bitset<InstructionBits>();
		for ( list<ArgumentType>::iterator it = instructions[tokens[0]].dynamic_inst.begin() ; it != instructions[tokens[0]].dynamic_inst.end() ; ++it ) {
			if ( !( ind < tokens.size() && ( it->type != REGISTER || tokens[ind] == "$" ) && ( it->type != TOKEN || tokens[ind] == it->correspondence ) && ( it->type != TAG || isFunction( tokens[ind], isChar ) ) && ( it->type == PSEUDOTAG || isFunction( tokens[ind], isChar ) )   ) ) {
				typeAssert( false, tokens, tokens[0] );
			} else if ( it->type == REGISTER ) {
				typeAssert( ind+1 < tokens.size(), tokens, "register_name" );
				typeAssert( registers.count( tokens[ind+1] ), tokens, "register_name" );
				number = registers[tokens[ind+1]];
				tope = types[instructions[tokens[0]].type][it->correspondence].start + types[instructions[tokens[0]].type][it->correspondence].bits;
				for ( i = types[instructions[tokens[0]].type][it->correspondence].start ; i < tope ; ++i ) {
					act[i] = (number&1);
					number >>= 1;
				}
				if ( number != 0 ) {
					fprintf( stderr, "Error, the space allocated for the register is not enough to represent the number. This is an issue with the instructions_specifications ( particularly the <register> )\n" );
					personalizedThrow();
				}
				++ind; // uno extra porque lo compone el token de '$' y el nombre del registro
			} else if ( it->type == INMEDIATE ) {
				tokenAssert( isNumber( tokens[ind] ), tokens, ind );
				number = convertStringToNum( tokens[ind] );
				tope = types[instructions[tokens[0]].type][it->correspondence].start + types[instructions[tokens[0]].type][it->correspondence].bits;
				for ( i = types[instructions[tokens[0]].type][it->correspondence].start ; i <= tope ; ++i ) {
					act[i] = (number&1);
					number >>= 1;
				}
				tokenAssert( number == 0, tokens, ind );
			} else if ( it->type == TAG ) {
				allTags.push_back( TagPlaceHolder( tokens[ind], instructions[tokens[0]].type, it->correspondence, instructionIndex, TAG ) );
			} else if ( it->type == PSEUDOTAG ) {
				allTags.push_back( TagPlaceHolder( tokens[ind], instructions[tokens[0]].type, it->correspondence, instructionIndex, PSEUDOTAG ) );
			}
			++ind;
		}
		for ( list<pair<string,int>>::iterator it = (instructions[tokens[0]].static_inst).begin() ; it != (instructions[tokens[0]].static_inst).end() ; ++it ) {
			number = it->second;
			TypeSpec tmp = types[instructions[tokens[0]].type][it->first];
			tope = tmp.start + tmp.bits;
			for ( i = tmp.start ; i <= tope ; ++i ) {
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
		if ( allTags.front().type == PSEUDOTAG ) {
			number += startOfProgram;
		}
		number >>= 2;

		TypeSpec tmp =  types[allTags.front().typeName][allTags.front().typeSpecName];
		tope = tmp.start + tmp.bits;
		for ( i = tmp.start ; i <= tope ; ++i ) {
			act[i] = (number&1);
			number >>= 1;
		}

		allTags.pop_front();
	}
	return res;
}

#endif
