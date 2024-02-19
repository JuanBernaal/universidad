"""
This is the interface of the assembler
The actual assembler is to be written in the file 'assembler.py'
10/02/2024
"""

import sys
import assembler

def printHelp():
	print( """ 
It receives as a predetermined input a file with assembly code from the MIPS 32-bit architecture

An output file can be especified using the comand '-o' or '--output'
				-o <outputFile>
				--output <outputFile>

The assembler version can be consulted using the command '-v' or '--version'
				-v
				--version

This help message can be consulted using the command '-h' or '--help'
				-h
				--help
	""" );

def printVersion():
	print( """
This is the version 1.0 of the assembler.
It was made to translate code in the MIPS 32-bit architecture.
Credits to:
   * Benjamin Ortiz
   * Marco Riascos
   * Juan David Bernal
   * Oscar vargas
	""" );

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

if __name__ == "__main__":
	main();