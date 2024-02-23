
#ifndef READ_SPECS
#define READ_SPECS

#include "generalFunctions.cpp"

#define TOKEN 0
#define INMEDIATE 1
#define REGISTER 2
#define TAG 3
#define PSEUDOTAG 4

/* The class `ArgumentType` in C++ represents a type of argument with an integer type and a
corresponding string. */
class ArgumentType {
public:
	int type;
	string correspondence;
	ArgumentType( int t, const string &cor ) : type( t ), correspondence( cor  ) {};
};

/* The TypeSpec class in C++ represents a type specification with attributes for bits and start
position. */
class TypeSpec {
public:
	int bits, start;
	TypeSpec() = default;
	TypeSpec( int b, int s ) : bits( b ) , start( s ) {};
};

/* The class `Instruction` in C++ contains lists of static and dynamic instructions along with a type
string. */
class Instruction {
public:
	list<pair<string,int>> static_inst;
	list<ArgumentType> dynamic_inst;
	string type;
	Instruction() = default;
	Instruction( const string &str ) : type( str ) {};
};

map<string, map<string,TypeSpec>> types;
map<string, Instruction> instructions;
map<string,int> registers;

/**
 * The function `read_type_spec` reads and validates a type specification from a vector of tokens in
 * C++.
 * 
 * @param tokens The `tokens` parameter is a vector of strings that contains the input tokens to be
 * processed by the `read_type_spec` function.
 * @param index The `index` parameter in the `read_type_spec` function represents the current position
 * in the vector `tokens` where the function is reading and processing tokens. It is used to access
 * specific tokens in the vector during the parsing process.
 * @param start The `start` parameter in the `read_type_spec` function is used to indicate the starting
 * index of the current token being processed within the vector of tokens. It helps in keeping track of
 * the position in the vector while parsing and validating the tokens.
 * 
 * @return The function `read_type_spec` is returning an integer value `tmp`.
 */
int read_type_spec( const vector<string> &tokens, int index, int start ) {
	typeAssert( index+3 < tokens.size(), tokens, "type_spec" );

	tokenAssert( tokens[index] == "(", tokens, index );
	tokenAssert( isFunction( tokens[index+1], isChar ), tokens, index+1 );
	
	tokenAssert( isNumber( tokens[index+2] ), tokens, index+2 );

	tokenAssert( tokens[index+3] == ")", tokens, index+3 );

	int tmp = convertStringToNum( tokens[index+2] );
	types[tokens[0]][tokens[index+1]] = TypeSpec( tmp, start );
	return tmp;
}

/*
Ampliar para TAG y PSEUDOTAG
*/

/**
 * The function `read_instruction_specs` processes dynamic and static instruction specifications for a
 * given instruction type and name.
 * 
 * @param dynamic_inst The `dynamic_inst` parameter is a vector of strings that contains dynamic
 * instruction specifications. These specifications define the type and format of arguments for a
 * particular instruction.
 * @param static_inst The `static_inst` parameter in the `read_instruction_specs` function is a vector
 * of strings that contains static instructions for a particular type of instruction. These static
 * instructions are parsed and processed within the function to extract relevant information for
 * further processing.
 * @param type_inst The `type_inst` parameter in the `read_instruction_specs` function represents the
 * type of instruction being processed. It is used to determine the specific type of instruction being
 * read and to validate certain tokens based on the type of instruction.
 * @param inst The `inst` parameter in the `read_instruction_specs` function represents the specific
 * instruction being processed. It is used to store information about the dynamic and static components
 * of the instruction in the `instructions` data structure.
 */
void read_instruction_specs( const vector<string> &dynamic_inst, const vector<string> &static_inst, const string &type_inst, const string &inst ) {
	int index = 0;
	while ( index < dynamic_inst.size() ) {
		if ( dynamic_inst[index] == "reg" ) {

			typeAssert	( index+3 < dynamic_inst.size(), dynamic_inst, "dynamic_inst" );

			tokenAssert( dynamic_inst[index+1] == "(", dynamic_inst, index+1 );
			tokenAssert( types[type_inst].count( dynamic_inst[index+2] ), dynamic_inst, index+2 );
			tokenAssert( dynamic_inst[index+3] == ")", dynamic_inst, index+3 );

			instructions[inst].dynamic_inst.push_back( ArgumentType( REGISTER, dynamic_inst[index+2] ) );

			index += 4;
		} else if ( dynamic_inst[index] == "inm" ) {
			typeAssert( index+3 < dynamic_inst.size(), dynamic_inst, "dynamic_inst" );

			tokenAssert( dynamic_inst[index+1] == "(", dynamic_inst, index+1 );
			tokenAssert( isFunction( dynamic_inst[index+2], isChar ), dynamic_inst, index+2 );
			tokenAssert( dynamic_inst[index+3] == ")", dynamic_inst, index+3 );

			instructions[inst].dynamic_inst.push_back( ArgumentType( INMEDIATE, dynamic_inst[index+2] ) );

			index += 4;
		} else if ( dynamic_inst[index] == "tag" ) {
			typeAssert( index+3 < dynamic_inst.size(), dynamic_inst, "dynamic_inst" );
			tokenAssert( dynamic_inst[index+1] == "(", dynamic_inst, index+1 );
			tokenAssert( isFunction( dynamic_inst[index+2], isChar ), dynamic_inst, index );
			tokenAssert( dynamic_inst[index+3] == ")", dynamic_inst, index+3 );

			instructions[inst].dynamic_inst.push_back( ArgumentType( TAG, dynamic_inst[index+2] ) );

			index += 4;
		} else if ( dynamic_inst[index] == "pseudoTag" ) {
			typeAssert( index+3 < dynamic_inst.size(), dynamic_inst, "dynamic_inst" );
			tokenAssert( dynamic_inst[index+1] == "(", dynamic_inst, index+1 );
			tokenAssert( isFunction( dynamic_inst[index+2], isChar ), dynamic_inst, index );
			tokenAssert( dynamic_inst[index+3] == ")", dynamic_inst, index+3 );

			instructions[inst].dynamic_inst.push_back( ArgumentType( PSEUDOTAG, dynamic_inst[index+2] ) );

			index += 4;
		} else {
			instructions[inst].dynamic_inst.push_back( ArgumentType( TOKEN, dynamic_inst[index] ) );
			++index;
		}
	}
	index = 0;
	while ( static_inst[index] != "|" ) {
		typeAssert( index+4 < static_inst.size(), static_inst, "static_inst" );

		tokenAssert( isFunction( static_inst[index], isChar ), static_inst, index );
		tokenAssert( static_inst[index+1] == "-", static_inst, index+1 );
		tokenAssert( static_inst[index+2] == ">", static_inst, index+2 );
		tokenAssert( isNumber( static_inst[index+3] ), static_inst, index+3 );
		tokenAssert( static_inst[index+4] == "|", static_inst, index+4 );
		tokenAssert( types[type_inst].count( static_inst[index] ), static_inst, index );

		instructions[inst].static_inst.push_back( pair<string,int> ( static_inst[index], convertStringToNum( static_inst[index+3] ) ) );

		index += 5;
	}
}

/**
 * The function `read_instructions` reads and processes different segments of data from a file based on
 * specific tags and formats.
 * 
 * @return This function does not have a return value as it is declared as void. It reads instructions
 * from a file and processes them accordingly, but it does not return any value.
 */
void read_instructions() {
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
		read_instruction_specs( tokens, tokenize_line( rawData ), inst_type, inst );

		tokens = tokenize_line( rawData );

		typeAssert( tokens[0] == "end", tokens, "instruction" );
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
		tokenAssert( isFunction( tokens[1], [] ( char act ) -> bool { return isChar ( act ) || isDec( act ) ; } ), tokens, 1 );
		tokenAssert( tokens[2] == "-", tokens, 2 );
		tokenAssert( tokens[3] == ">", tokens, 3 );
		tokenAssert( isNumber( tokens[4] ), tokens, 4 );

		registers[tokens[1]] = convertStringToNum( tokens[4] );

		tokens = tokenize_line( rawData );
	}
	tokenAssert( tokens[1] == "end", tokens, 1 );
	typeAssert( tokens.size() == 2, tokens, "segment_name" );

	fclose( rawData );
	personalizedThrow = CloseAbruptly( NULL );
}


/**
 * The debug function prints information about types, instructions, and registers in a C++ program.
 */

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
		printf( "dynamic bit:\n" );
		for ( auto it3 : it.second.dynamic_inst ) {
			printString( it3.correspondence, stdout );
			printf( " -> | token %d | inmediate %d | register %d\n", it3.type == TOKEN, it3.type == INMEDIATE, it3.type == REGISTER );
		}
		printf( "static bit:\n" );
		for ( auto it3 : it.second.static_inst ) {
			printString( it3.first, stdout );
			printf( " -> %d | ", it3.second );
		}
		printf( "\n_\n" );
	}

	printf( "\n________________________________The registers:\n\n" );
	for ( auto it : registers ) {
		printString( it.first, stdout );
		printf( " -> %d\n", it.second );
	}
}

#endif