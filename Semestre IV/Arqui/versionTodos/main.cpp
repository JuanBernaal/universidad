/*
This is the interface of the assembler
The actual assembler is to be written in the file 'assembler.py'
10/02/2024
*/

#include "myAssembler.cpp"

void printHelp(){
    printf( "It receives as a predetermined input a file with assembly code from the MIPS 32-bit architecture\n");
    printf( "An output file can be especified using the comand '-o' or '--output'\n");
    printf( "				-o <outputFile>\n");
    printf( "				--output <outputFile>\n\n");
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
/*
def main():
	l = sys.argv;
	i = 1;
	inName, outName = -1, -1;
	flag = True;
	while ( flag and i < len( sys.argv ) ) :
		if ( sys.argv[i] == '-v' or sys.argv[i] == '--version' ):
			printVersion();
			flag = False;
		elif ( sys.argv[i] == "-h" or sys.argv[i] == "--help" ) :
			printHelp();
			flag = False;
		elif ( sys.argv[i] == "-o" or sys.argv[i] == "--output" ) :
			i += 1;
			if ( i >= len( sys.argv ) ):
				print( "Error: The command -o doesn't have the required info ( No name was especified )." );
				flag = False;
			else:
				outName = i;
		else:
			inName = i;
		i += 1;
	if ( flag and inName == -1 ):
		print( "Error: No input file was especified." );
	elif ( flag and inName != -1 ):
		assembler.assembleFile( sys.argv[inName], "a.exe" if outName == -1 else (sys.argv[outName]+".exe") );

*/

int main( int argc, char * argv[]) {

	EndOfFile = false;
	read_instructions();
	EndOfFile = false;
	//debug();

	printf( "entra a assemble\n" );
	vector<bitset<InstructionBits>> interm = assemble( argv[1] );
	printf( "sale con %d\n", interm.size() );
	printString( interm[0].to_string(), stdout );
	printf( "\n" );
	return 0;
}