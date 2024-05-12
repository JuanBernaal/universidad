/*
This is the interface of the assembler
The actual assembler is to be written in the file 'assembler.py'
10/02/2024
*/

#include "myAssembler.cpp"
#include <cstring>

void assemble( char *, char *, int );
void dev_testing( char *input);


/**
 * The function `printHelp` provides a detailed description of the command-line options for a MIPS
 * 32-bit architecture assembly code assembler.
 */
void printHelp(){
    printf( "It receives as a predetermined input a file with assembly code from the MIPS 32-bit architecture\n");
    printf( "An output file can be especified using the comand '-o' or '--output'\n");
    printf( "				-o <outputFile>\n");
    printf( "				--output <outputFile>\n\n");
    printf( "An address in wich the program starts can be especified with the command '-s' or '--start'\n" );
    printf( "               -s <address>\n" );
    printf( "               --start <address>\n\n" );
    printf( "The assembler version can be consulted using the command '-v' or '--version'\n");
    printf( "				-v\n");
    printf( "				--version\n\n" );
    printf( "The assembler output can be printed through the console using the command '-p' or '--print'\n");
    printf( "				-p\n");
    printf( "				--print\n\n" );
    printf( "This help message can be consulted using the command '-h' or '--help'\n");
    printf( "				-h\n" );
    printf( "				--help\n" );
}

/**
 * The function `printVersion` prints information about the version and creators of an assembler
 * program for translating code in the MIPS 32-bit architecture.
 */
void printVersion() {
	printf( "This is the version 1.0 of the assembler.\n" );
    printf( "It was made to translate code in the MIPS 32-bit architecture.\n" );
    printf( "Credits to:\n" );
    printf( "   * Oscar vargas\n" );
    printf( "   * Benjamin Ortiz\n" );
    printf( "   * Juan David Bernal\n" );
    printf( "   * Marco Riascos\n" );
    
}


/**
 * The function `printInstructions` prints out the binary representation of instructions stored in a
 * vector of bitsets in reverse order.
 * 
 * @param prog A vector of bitsets representing instructions, where each bitset contains a fixed number
 * of bits (InstructionBits).
 */
void printInstructions( const vector<bitset<InstructionBits>> &prog ) {
    for ( int i = 0; i < prog.size() ; ++i ) {
        string tmp = prog[i].to_string();
        for ( int j = tmp.size()-1 ; j >= 0 ; --j ) {
            printf( "%c", tmp[j] );
        }
        printf( "\n" );
    }
}

/**
 * The main function in C++ parses command line arguments to assemble a file and output the result.
 * 
 * @param argc `argc` is the argument count, which represents the number of arguments passed to the
 * program when it is executed. In the context of the `main` function in C or C++, `argc` holds the
 * number of command-line arguments including the name of the program itself.
 * @param argv argv is an array of strings that contains the command-line arguments passed to the
 * program when it is executed. In the provided code snippet, the main function is processing these
 * arguments to determine the actions to be taken by the program.
 * 
 * @return The `main` function is returning an integer value of 0.
 */
int main( int argc, char * argv[] ){
    //dev_testing( argv[1] ); return 0; //para hacer las pruebas

    char StandardOuput[] = "a.exe";
	int i = 1, startAdress = 0;
	int inName = -1, outName = -1;
	bool flag = true, file = true;
	while ( flag && i < argc ) {
		if ( strcmp( argv[i], "-v" ) == 0 || strcmp( argv[i], "--version" ) == 0 ) {
			printVersion();
			flag = false;
		} else if ( strcmp( argv[i], "-h" ) == 0 || strcmp( argv[i],  "--help" ) == 0 ) {
			printHelp();
			flag = false;
		} else if ( strcmp( argv[i],  "-o" ) == 0 || strcmp( argv[i], "--output" ) == 0 ) {
			i += 1;
			if ( i >= argc ){
				printf( "Error: The command -o doesn't have the required info ( No name was especified ).\n" );
				flag = false;
            } else {
				outName = i;
            }
        } else if ( strcmp( argv[i], "-s" ) == 0 || strcmp( argv[i], "--start" ) == 0 ) {
            i += 1;
            if ( i >= argc ) {
                printf( "Error: The command -s doesn't have the required info ( No address was especified ).\n" );
                flag = false;
            } else {
                string tmp;
                for ( int k = 0 ; argv[i][k] != '\0' ; ++k ) tmp.push_back( argv[i][k] );
                startAdress = convertStringToNum( tmp );
            }
        } else if ( strcmp( argv[i], "-p" ) == 0 || strcmp( argv[i], "--print" ) == 0 ) {
            file = false;
        } else {
			inName = i;
        }
		i += 1;
	if ( flag && inName == -1 ) {
		printf( "Error: No input file was especified." );
    } else if ( flag && inName != -1 ) {
        char *output;
        if ( outName != -1 ) {
            int len = 1;
            for ( int i = 0; argv[outName][i] != '\0' ; ++i ) ++len;
            output = (char*) malloc( sizeof(char*) * (len+4) );
            for ( int i = 0 ; argv[outName][i] != '\0' ; ++i ) output[i] = argv[outName][i];
            output[len] = '.';
            output[len+1] = 'e';
            output[len+2] = 'x';
            output[len+2] = 'e';
            output[len+3] = '\0';
        } else {
            output = StandardOuput;
        }
		assemble( argv[inName], ( file ) ? output : NULL, startAdress ); // hacer esto
    }
}
return 0;
}
/**
 * The function `assemble` reads instructions from an input file, assembles them into binary format,
 * and writes the output to a specified file or prints it if no output file is provided.
 * 
 * @param inputFile The `inputFile` parameter in the `assemble` function is a pointer to a character
 * array that represents the input file from which instructions are read for assembling.
 * @param outputFile The `outputFile` parameter in the `assemble` function is a pointer to a character
 * array that specifies the name of the output file where the assembled instructions will be written.
 * If `outputFile` is `NULL`, the assembled instructions will be printed to the console instead of
 * being written to a file
 * @param programStart The `programStart` parameter in the `assemble` function is used to specify the
 * starting address of the program in memory. This parameter indicates where the program's instructions
 * should be loaded into memory for execution. It helps in determining the memory location from which
 * the program's execution should begin.
 * 
 * @return The function `assemble` does not have a return type specified, so it does not explicitly
 * return anything. However, it performs various operations like reading instructions, assembling
 * input, printing instructions, and writing to an output file based on the provided parameters. The
 * function may return void or it may have side effects like writing to a file or printing
 * instructions.
 */
void assemble( char *inputFile, char *outputFile, int programStart ) {
	EndOfFile = false;
	read_instructions();
	EndOfFile = false;

    startOfProgram = programStart;
	vector<bitset<InstructionBits>> interm = assemble( inputFile );

    if ( outputFile == NULL ) {
        printInstructions( interm );
        return;
    }

    FILE *output = fopen( outputFile, "wb" );
	personalizedThrow = CloseAbruptly( output );

    unsigned int act = 0;
    for ( int i = 0; i < interm.size() ; ++i ) {
        act = 0u;
        for ( int j = InstructionBits-1 ; j >= 0 ; --j ) {
            act = ( act << 1 ) + ( interm[i][j] );
        }
        fwrite ( &act, 1, sizeof( act ), output  );
    }

    fclose( output );
	personalizedThrow = CloseAbruptly( NULL );
}

/**
 * The function `dev_testing` reads instructions from a file, assembles them, and prints the resulting
 * bitset values.
 * 
 * @param input The `dev_testing` function seems to be reading instructions from a file named
 * `dummy.txt`, processing them, and then assembling them into a vector of bitsets. The `assemble`
 * function is likely responsible for converting the input into a binary representation.
 */
void dev_testing( char *input) {

    printf( "Comienza a leer las instrucciones en dummy.txt\n" );
	EndOfFile = false;
	read_instructions();
	EndOfFile = false;
	//debug();
    printf( "termina de leer las instrucciones en dummy.txt\n" );

    startOfProgram = 0;

	printf( "entra a assemble\n" );
	vector<bitset<InstructionBits>> interm = assemble( input );
	printf( "sale con %d\n", interm.size() );
    for ( int i = 0; i < interm.size() ; ++i ) {
        string tmp = interm[i].to_string();
        for ( int j = tmp.size()-1 ; j >= 0 ; --j ) {
            printf( "%c", tmp[j] );
        }
        printf( "\n" );
    }
}