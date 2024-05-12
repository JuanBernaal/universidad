/*
Autor: Oscar Vargas Pabon
Fecha: 4/02/2024

ojala funcione
*/

#include <string>
#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <bitset>

using namespace std;

#define InstructionBits 32

class ArgumentType {
public:
	bool token, inmediate, register_name;
	string correspondence;
	ArgumentType( bool t, bool i, bool r, const string &cor ) : token( t ), inmediate( i ), register_name( r ), correspondence( cor  ) {};
};

class Decode {
public:
	list<pair<string,int>> static_inst;
	list<ArgumentType> dynamic_inst;
	Decode() = default;
};

class TypeSpec {
public:
	int bits, start;
	TypeSpec() = default;
	TypeSpec( int b, int s ) : bits( b ) , start( s ) {};
};

class Instruction {
public:
	list<Decode> ways;
	string type;
	Instruction() = default;
	Instruction( const string &str ) : type( str ) {};
};

map<string, map<string,TypeSpec>> types;
map<string, Instruction> instructions;
map<string,int> registers;

void printString( const string &str, FILE *output ) {
	for ( int j = 0 ; j < str.size() ; ++j ) {
		putc( str[j], output );
	}
}

class CloseAbruptly {
private:
	FILE *stream;
public:
	CloseAbruptly( FILE *inStream ) {
		this->stream = inStream;
	}
	void operator () () {
		if ( this->stream != NULL ) fclose( this->stream );
		throw ( "Error" );
	}
};

CloseAbruptly personalizedThrow( NULL );
bool EndOfFile;

void typeAssert( bool cond, const vector<string> &tokens, const string &type ) {
	if ( !cond ) {
		fprintf( stderr, "Error on type '" );
		printString( type, stderr );
		fprintf( stderr, "' The amount of tokens is off on line:\n" );
		for ( int i = 0 ; i < tokens.size() ; ++i ) {
			printString( tokens[i], stderr );
			putc( ' ', stderr );
		}
		putc( '\n', stderr );
		personalizedThrow();
	}
}

void tokenAssert( bool cond, const vector<string> &tokens, int index ) {
	if ( !cond ) {
		fprintf( stderr, "Error on line:\n"  );
		for ( int i = 0 ; i < tokens.size() ; ++i ) {
			if ( i == index ) putc( '^', stderr );
			printString( tokens[i], stderr );
			putc( ' ', stderr );
		}
		putc( '\n', stderr );
		personalizedThrow();
	}
}


bool isChar( char act ) {
	bool res = ( 'a' <= act && act <= 'z' ) || ( 'A' <= act && act <= 'Z' );
	return res;
}

bool isNum( char act ) {
	bool res = ( '0' <= act && act <= '9' );
	return res;
}
bool isHex( char act ) {
	bool res = isNum( act ) || ( 'A' <= act && act <= 'F' );
	return res;
}
bool isFunction( const string &act, bool ( *fun ) ( char ) ) {
	bool res = true;
	int i;
	for ( i = 0 ; i < act.size() && res ; ++i ) res = fun( act[i] );
	if ( !res ) fprintf( stderr, "Salio en %d con |%c|\n", i, act[i] );
	return res;
}
int toDecNum( const string &act ) {
	int res = 0;
	for ( int i = 0 ; i < act.size() ; ++i ) {
		res = ( res*10 ) + act[i]-'0';
	}
	return res;
}

int toHexNum( const string &act ) {
	int res = 0;
	for ( int i = 0 ; i < act.size() ; ++i ) {
		res = ( res * 16 ) + ( ( act[i] <= '9' ) ? act[i]-'0' : act[i]-'A'+10 );
	}
	return res;
}

vector<string> tokenize_line( FILE *input ) {
	vector<string> res;
	if ( EndOfFile ) return res;
	string act;
	char t = getc( input );
	bool comment = true;
	while ( t != '\n' && t != EOF && comment ) {
		if ( t == ';' ) {
			comment = false;
		} else if ( isChar( t ) || isHex( t ) ) {
			act.push_back( t );
		} else if ( act.size() > 0 ) {
			res.push_back( act );
			act.clear();
		} 
		if ( !(isChar( t ) | isHex( t ) ) && t != ' ' && t != ';' ) {
			act.push_back( t );
			res.push_back( act );
			act.pop_back();
		}
		t = getc( input );
	}
	while ( !comment && t != '\n' && t != EOF ) t = getc( input );
	if ( act.size() > 0 ) res.push_back( act );
	if ( res.size() == 0 && t != EOF ) res = tokenize_line( input );
	EndOfFile = (t == EOF);
	return res;
}

int read_type_spec( const vector<string> &tokens, int index, int start ) {
	typeAssert( index+3 < tokens.size(), tokens, "type_spec" );

	tokenAssert( tokens[index] == "(", tokens, index );
	tokenAssert( isFunction( tokens[index+1], isChar ), tokens, index+1 );
	tokenAssert( isFunction( tokens[index+2], isNum ), tokens, index+2 );
	tokenAssert( tokens[index+3] == ")", tokens, index+3 );

	int tmp = toDecNum( tokens[index+2] );
	types[tokens[0]][tokens[index+1]] = TypeSpec( tmp, start );
	return tmp;
}

void read_inst_reading( const vector<string> &dynamic_inst, const vector<string> &static_inst, const string &type_inst, const string &inst ) {
	int index = 0;
	Decode act;
	while ( index < dynamic_inst.size() ) {
		if ( dynamic_inst[index] == "reg" ) {
			typeAssert	( index+3 < dynamic_inst.size(), dynamic_inst, "dynamic_inst" );

			tokenAssert( dynamic_inst[index+1] == "(", dynamic_inst, index+1 );
			tokenAssert( types[type_inst].count( dynamic_inst[index+2] ), dynamic_inst, index+2 );
			tokenAssert( dynamic_inst[index+3] == ")", dynamic_inst, index+3 );

			act.dynamic_inst.push_back( ArgumentType( false, false, true, dynamic_inst[index+2] ) );

			index += 4;
		} else if ( dynamic_inst[index] == "inm" ) {
			typeAssert( index+3 < dynamic_inst.size(), dynamic_inst, "dynamic_inst" );

			tokenAssert( dynamic_inst[index+1] == "(", dynamic_inst, index+1 );
			tokenAssert( isFunction( dynamic_inst[index+2], isChar ), dynamic_inst, index+2 );
			tokenAssert( dynamic_inst[index+3] == ")", dynamic_inst, index+3 );

			act.dynamic_inst.push_back( ArgumentType( false, true, false, dynamic_inst[index+2] ) );

			index += 4;
		} else {
			act.dynamic_inst.push_back( ArgumentType( true, false, false, dynamic_inst[index] ) );
			++index;
		}
	}
	index = 0;
	while ( static_inst[index] != "|" ) {
		typeAssert( index+4 < static_inst.size(), static_inst, "static_inst" );

		tokenAssert( isFunction( static_inst[index], isChar ), static_inst, index );
		tokenAssert( static_inst[index+1] == "-", static_inst, index+1 );
		tokenAssert( static_inst[index+2] == ">", static_inst, index+2 );
		tokenAssert( isFunction( static_inst[index+3], isHex ), static_inst, index+3 );
		tokenAssert( static_inst[index+4] == "|", static_inst, index+4 );
		tokenAssert( types[type_inst].count( static_inst[index] ), static_inst, index );

		act.static_inst.push_back( pair<string,int> ( static_inst[index], toHexNum( static_inst[index+3] ) ) );

		index += 5;
	}
	instructions[inst].ways.push_back( act );
}

void leer() {
	FILE *rawData = fopen( "dummy.txt", "r" );
	personalizedThrow = CloseAbruptly( rawData );
	int tmp, start, index;

	// leer lo que esta bajo la etiqueta .type
	vector<string> tokens = tokenize_line( rawData );
	tokenAssert( tokens[1] == "type", tokens, 1 );
	typeAssert( tokens.size() == 2, tokens, "segment_name" );
	tokens = tokenize_line( rawData );
	while ( tokens[0] != "." ) {
		tokenAssert( isFunction( tokens[0], isChar ), tokens, 0 );
		tokenAssert( tokens[1] == ":", tokens, 1 );
		index = 2; start = 0;
		while ( index < tokens.size() ) {
			start += read_type_spec( tokens, index, start );
			index += 4;
		}
		tokens = tokenize_line( rawData );
	}

	// leer lo que esta bajo la etiqueta .instruction
	tokenAssert( tokens[1] == "instruction", tokens, 1 );
	typeAssert( tokens.size() == 2, tokens, "segment_name" );
	tokens = tokenize_line( rawData );
	while ( tokens[0] != "." ) {
		typeAssert( tokens.size() == 2, tokens, "instruction" );
		tokenAssert( isFunction( tokens[0], isChar ), tokens, 0 );
		tokenAssert( isFunction( tokens[1], isChar ), tokens, 1 );
		string inst_type = tokens[1], inst = tokens[0];

		instructions[inst] = Instruction( inst_type );

		tokens = tokenize_line( rawData );
		while ( tokens[0] != "end" ) {
			read_inst_reading( tokens, tokenize_line( rawData ), inst_type, inst );
			tokens = tokenize_line( rawData );
		}
		typeAssert( tokens.size() == 1, tokens, "instruction" );
		
		tokens = tokenize_line( rawData );
	}

	// leer lo que esta bajo la etiqueta .register
	tokenAssert( tokens[1] == "register", tokens, 1 );
	typeAssert( tokens.size() == 2, tokens, "segment_name" );
	tokens = tokenize_line( rawData );
	while ( tokens[0] != "." ) {
		typeAssert( tokens.size() == 5, tokens, "register" );

		tokenAssert( tokens[0] == "$", tokens, 0 );
		tokenAssert( isFunction( tokens[1], [] ( char act ) -> bool { return isChar ( act ) || isNum( act ) ; } ), tokens, 1 );
		tokenAssert( tokens[2] == "-", tokens, 2 );
		tokenAssert( tokens[3] == ">", tokens, 3 );
		tokenAssert( isFunction( tokens[4], isNum ), tokens, 4 );

		registers[tokens[1]] = toDecNum( tokens[4] );

		tokens = tokenize_line( rawData );
	}
	tokenAssert( tokens[1] == "end", tokens, 1 );
	typeAssert( tokens.size() == 2, tokens, "segment_name" );

	fclose( rawData );
	personalizedThrow = CloseAbruptly( NULL );
}

void debug() {
	printf( "________________________________the types:\n" );
	for ( auto it : types ) {
		printf( "\nType: " );
		printString( it.first, stdout );
		printf( ". With elements: \n" );
		for ( auto it2 : it.second ) {
			printf( "| " );
			printString( it2.first, stdout );
			printf( " -> ( %d, %d ) ", it2.second.bits, it2.second.start );
		}
		putc( '\n', stdout );
	}

	printf( "\n________________________________The instructions:\n\n" );

	for ( auto it : instructions ) {
		printf( "instruction: " );
		printString( it.first, stdout );
		printf( ". of type: " );
		printString( it.second.type, stdout );
		putc( '\n', stdout );
		for ( auto it2 : it.second.ways ) {
			printf( "dynamic bit:\n" );
			for ( auto it3 : it2.dynamic_inst ) {
				printString( it3.correspondence, stdout );
				printf( " -> | token %d | inmediate %d | register %d\n", it3.token, it3.inmediate, it3.register_name );
			}
			printf( "static bit:\n" );
			for ( auto it3 : it2.static_inst ) {
				printString( it3.first, stdout );
				printf( " -> %d | ", it3.second );
			}
			printf( "\n_\n" );
		}
	}

	printf( "\n________________________________The registers:\n\n" );
	for ( auto it : registers ) {
		printString( it.first, stdout );
		printf( " -> %d\n", it.second );
	}
}

vector<bitset<InstructionBits>> assemble( char *inFile ) {
	FILE *rawAssemble = fopen( inFile, "r" );
	personalizedThrow = CloseAbruptly( rawAssemble );

	vector<bitset<InstructionBits>> res;
	bitset<InstructionBits> act;
	vector<string> tokens = tokenize_line( rawAssemble );
	int ind, number, tope, i; bool correct;
	list<Decode>::iterator it;
	while ( tokens.size() > 0 ) {
		tokenAssert( instructions.count( tokens[0] ), tokens, 0 );
		correct = false;
		for ( it = instructions[tokens[0]].ways.begin() ; it != instructions[tokens[0]].ways.end() && !correct ; ++it ) {
			ind = 1; correct = true;
			act = bitset<InstructionBits>();
			for ( list<ArgumentType>::iterator it2 = it->dynamic_inst.begin() ; it2 != it->dynamic_inst.end() && correct ; ++it2 ) {
				if ( !( ind < tokens.size() && ( !it2->register_name || tokens[ind] == "$" ) && ( !it2->token || tokens[ind] == it2->correspondence ) ) ) {
					correct = false;
				} else if ( it2->register_name ) {
					typeAssert( ind+1 < tokens.size(), tokens, "register_name" );
					typeAssert( registers.count( tokens[ind+1] ), tokens, "register_name" );
					number = registers[tokens[ind+1]];
					tope = types[instructions[tokens[0]].type][it2->correspondence].start + types[instructions[tokens[0]].type][it2->correspondence].bits;
					for ( i = types[instructions[tokens[0]].type][it2->correspondence].start ; i < tope ; ++i ) {
						act[i] = (number&1);
						number >>= 1;
					}
					if ( number != 0 ) {
						fprintf( stderr, "Error, the space allocated for the register is not enough to represent the number. This is an issue with the instructions_specifications ( particularly the <register> )\n" );
						throw( "error" );
					}
					++ind; // uno extra porque lo compone el token de '$' y el nombre del registro
				} else if ( it2->inmediate ) {
					tokenAssert( isFunction( tokens[ind], isHex ), tokens, ind );
					number = toHexNum( tokens[ind] );
					tope = types[instructions[tokens[0]].type][it2->correspondence].start + types[instructions[tokens[0]].type][it2->correspondence].bits;
					for ( i = types[instructions[tokens[0]].type][it2->correspondence].start ; i <= tope ; ++i ) {
						act[i] = (number&1);
						number >>= 1;
					}
					tokenAssert( number == 0, tokens, ind );
				}
				++ind;
			}
		}
		--it; // alcanza a aumentar el iterador aunque la siguiente iteracion no entre
		typeAssert( correct, tokens, "general_instruction" );
		for ( list<pair<string,int>>::iterator it2 = (it->static_inst).begin() ; it2 != (it->static_inst).end() ; ++it2 ) {
			number = it2->second;
			tope = types[instructions[tokens[0]].type][it2->first].start + types[instructions[tokens[0]].type][it2->first].bits;
			for ( i = types[instructions[tokens[0]].type][it2->first].start ; i <= tope ; ++i ) {
				act[i] = (number&1);
				number >>= 1;
			}
			if ( number != 0 ) {
				fprintf( stderr, "Error, the space allocated for the constant is not enough to represent the number. This is an issue with the instructions_specifications ( particularly the <static_inst> )\n" );
				throw( "error" );
			}
		}

		res.push_back( act );

		tokens = tokenize_line( rawAssemble );
	}
	fclose( rawAssemble );
	personalizedThrow = CloseAbruptly( NULL );
	return res;
}

int main( int argc, char * argv[]) {
	EndOfFile = false;
	leer();
	EndOfFile = false;
	//debug();
	printf( "entra a assemble\n" );
	vector<bitset<InstructionBits>> interm = assemble( argv[1] );
	printf( "sale con %d\n", interm.size() );
	printString( interm[0].to_string(), stdout );
	printf( "\n" );
	return 0;
}
