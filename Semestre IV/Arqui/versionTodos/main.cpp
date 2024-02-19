/*
This is the interface of the assembler
The actual assembler is to be written in the file 'assembler.py'
10/02/2024
*/

#include "myAssembler.cpp"

void assemble( char *, char *, int );

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
    printf( "This help message can be consulted using the command '-h' or '--help'\n");
    printf( "				-h\n" );
    printf( "				--help\n" );
}

void printVersion() {
	printf( "This is the version 1.0 of the assembler.\n" );
    printf( "It was made to translate code in the MIPS 32-bit architecture.\n" );
    printf( "Credits to:\n" );
    printf( "   * Benjamin Ortiz\n" );
    printf( "   * Marco Riascos\n" );
    printf( "   * Juan David Bernal\n" );
    printf( "   * Oscar vargas\n" );
}


void printInstructions( const vector<bitset<InstructionBits>> &prog ) {
    for ( int i = 0; i < prog.size() ; ++i ) {
        string tmp = prog[i].to_string();
        for ( int j = tmp.size()-1 ; j >= 0 ; --j ) {
            printf( "%c", tmp[j] );
        }
        printf( "\n" );
    }
}

void main2( int argc, char * argv[] ){
    char StandardOuput[] = "a.exe";
	int i = 1, startAdress = 0;
	int inName = -1, outName = -1;
	bool flag = true;
	while ( flag && i < argc ) {
		if ( argv[i] == "-v" || argv[i] == "--version" ) {
			printVersion();
			flag = false;
		} else if ( argv[i] == "-h" || argv[i] == "--help" ) {
			printHelp();
			flag = false;
		} else if ( argv[i] == "-o" or argv[i] == "--output" ) {
			i += 1;
			if ( i >= argc ){
				printf( "Error: The command -o doesn't have the required info ( No name was especified ).\n" );
				flag = false;
            } else {
				outName = i;
            }
        } else if ( argv[i] == "-s" || argv[i] == "--start" ) {
            i += 1;
            if ( i >= argc ) {
                printf( "Error: The command -s doesn't have the required info ( No address was especified ).\n" );
                flag = false;
            } else {
                string tmp;
                for ( int k = 0 ; argv[i][k] != '\0' ; ++k ) tmp.push_back( argv[i][k] );
                startAdress = convertStringToNum( tmp );
            }
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
		assemble( argv[inName], output, startAdress ); // hacer esto
    }
}
}
void assemble( char *inputFile, char *outputFile, int programStart ) {
	EndOfFile = false;
	read_instructions();
	EndOfFile = false;

    startOfProgram = programStart;
	vector<bitset<InstructionBits>> interm = assemble( inputFile );

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

int main( int argc, char * argv[]) {

    printf( "Comienza a leer las instrucciones en dummy.txt\n" );
	EndOfFile = false;
	read_instructions();
	EndOfFile = false;
	//debug();
    printf( "termina de leer las instrucciones en dummy.txt\n" );

    startOfProgram = 0;

	printf( "entra a assemble\n" );
	vector<bitset<InstructionBits>> interm = assemble( argv[1] );
	printf( "sale con %d\n", interm.size() );
    for ( int i = 0; i < interm.size() ; ++i ) {
        string tmp = interm[i].to_string();
        for ( int j = tmp.size()-1 ; j >= 0 ; --j ) {
            printf( "%c", tmp[j] );
        }
        printf( "\n" );
    }
	return 0;
}