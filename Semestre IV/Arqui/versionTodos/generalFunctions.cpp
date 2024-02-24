#ifndef GENERAL_FUNCTIONS
#define GENERAL_FUNCTIONS

#include <string>
#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>

using namespace std;

/**
 * The function `printString` takes a string and outputs each character to a file stream.
 * 
 * @param str The `str` parameter is a constant reference to a string.
 * @param output The `output` parameter in the `printString` function is a pointer to a `FILE` type,
 * which is used to specify the output stream where the characters from the input string `str` will be
 * printed.
 */
void printString( const string &str, FILE *output ) {
	for ( int j = 0 ; j < str.size() ; ++j ) {
		putc( str[j], output );
	}
}

/* The CloseAbruptly class is designed to close a file stream abruptly and throw an error. */
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

/**
 * The function typeAssert checks a condition and prints an error message if it fails, along with the
 * tokens and type involved.
 * 
 * @param cond The `cond` parameter is a boolean value that represents the condition that needs to be
 * true for the type assertion to pass. If the condition is false, an error message will be printed and
 * an exception will be thrown.
 * @param tokens A vector of strings representing tokens or elements that need to be checked for a
 * specific type.
 * @param type The `type` parameter in the `typeAssert` function is a `const string` reference that
 * represents the expected type of the tokens being checked.
 */
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

/**
 * The function `tokenAssert` checks a condition and prints an error message with highlighted token if
 * the condition is not met.
 * 
 * @param cond The `cond` parameter is a boolean value that represents the condition that needs to be
 * checked. If the condition is false, an error message will be printed along with the tokens and an
 * error will be thrown.
 * @param tokens A vector of strings representing tokens or words in a code snippet.
 * @param index The `index` parameter in the `tokenAssert` function represents the position of the
 * token in the vector `tokens` that caused the assertion to fail. It is used to highlight the specific
 * token in the error message by placing a caret (`^`) underneath it.
 */
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

/**
 * The function isChar checks if a given character is a letter (either lowercase or uppercase).
 * 
 * @param act The parameter `act` in the `isChar` function is of type `char`.
 * 
 * @return The function `isChar` returns a boolean value indicating whether the input character `act`
 * is a letter (either lowercase or uppercase).
 */
bool isChar( char act ) {
	bool res = ( 'a' <= act && act <= 'z' ) || ( 'A' <= act && act <= 'Z' );
	return res;
}

/**
 * The function isDec checks if a character is a decimal digit.
 * 
 * @param act The parameter `act` is a character that represents an action or input. The function
 * `isDec` checks if the character `act` is a decimal digit (0-9) and returns a boolean value
 * accordingly.
 * 
 * @return The function isDec is returning a boolean value, which indicates whether the input character
 * is a decimal digit ('0' to '9').
 */
bool isDec( char act ) {
	bool res = ( '0' <= act && act <= '9' );
	return res;
}
/**
 * The function isHex checks if a character is a hexadecimal digit.
 * 
 * @param act The `act` parameter in the `isHex` function represents a single character that you want
 * to check if it is a valid hexadecimal digit.
 * 
 * @return The function `isHex` is returning a boolean value, which indicates whether the input
 * character `act` is a hexadecimal digit.
 */
bool isHex( char act ) {
	bool res = isDec( act ) || ( 'A' <= act && act <= 'F' ) || ( 'a' <= act && act <= 'f' );
	return res;
}
/**
 * The function `isFunction` checks if a given function `fun` returns true for all characters in a
 * given string `act`.
 * 
 * @param act The `act` parameter is a constant reference to a string.
 * @param fun The parameter `fun` is a pointer to a function that takes a `char` as an argument and
 * returns a `bool`.
 * 
 * @return The function `isFunction` returns a boolean value indicating whether the given function
 * `fun` returns true for all characters in the input string `act`.
 */
bool isFunction( const string &act, bool ( *fun ) ( char ) ) {
	bool res = true;
	int i;
	for ( i = 0 ; i < act.size() && res ; ++i ) res = fun( act[i] );
	return res;
}
/**
 * The function `isFunction` checks if a given function pointer returns true for all characters in a
 * string starting from a specified index.
 * 
 * @param act The `act` parameter is a constant reference to a string, which represents the input
 * string that the function will operate on.
 * @param fun The `fun` parameter is a pointer to a function that takes a `char` as input and returns a
 * `bool`.
 * @param strt The `strt` parameter in the `isFunction` function represents the starting index from
 * which the function should begin processing the characters in the `act` string.
 * 
 * @return The function `isFunction` returns a boolean value.
 */
bool isFunction( const string &act, bool ( *fun ) ( char ), int strt ) {
	bool res = true;
	int i;
	for ( i = strt ; i < act.size() && res ; ++i ) res = fun( act[i] );
	return res;
}

/**
 * The function `isNumber` checks if a given string represents a number in decimal or hexadecimal
 * format.
 * 
 * @param act The `act` parameter is a constant reference to a string, which is being passed to the
 * `isNumber` function. The function checks if the string represents a number by evaluating certain
 * conditions based on the content of the string.
 * 
 * @return The function `isNumber` is returning a boolean value. The value is determined by the
 * expression `( isFunction( act, isDec ) || ( act.size() >= 3 && act[0] == '0' && act[1] == 'x' &&
 * isFunction( act, isHex, 2 ) ) )`.
 */
bool isNumber( const string &act ) {
    bool res = ( isFunction( act, isDec ) || ( act.size() >= 3 && act[0] == '0' && act[1] == 'x' && isFunction( act, isHex, 2 ) ) );
    return res;
}

/**
 * The function `toDecNum` converts a string representing a decimal number to an integer.
 * 
 * @param act The `act` parameter in the `toDecNum` function is a constant reference to a string. This
 * function is designed to convert a string representing a decimal number into an integer.
 * 
 * @return The function `toDecNum` is returning an integer value that represents the decimal number
 * converted from the input string `act`.
 */
int toDecNum( const string &act ) {
	int res = 0;
	for ( int i = 0 ; i < act.size() ; ++i ) {
		res = ( res*10 ) + act[i]-'0';
	}
	return res;
}

/**
 * The function `toHexNum` converts a hexadecimal string to its corresponding integer value.
 * 
 * @param act The function `toHexNum` takes a string `act` as input and converts it to a decimal number
 * assuming that the string represents a hexadecimal number. The function starts iterating from index 2
 * of the string `act` to skip the "0x" prefix commonly used to denote hexadecimal numbers in
 * 
 * @return The function `toHexNum` takes a string `act` as input, which is assumed to be a hexadecimal
 * number in the form of a string (e.g., "0x1A2F"). The function converts this hexadecimal number to
 * its decimal equivalent and returns the decimal value as an integer.
 */
int toHexNum( const string &act ) {
	int res = 0, corr;
	for ( int i = 2 ; i < act.size() ; ++i ) {
        if ( 'A' <= act[i] && act[i] <= 'F' ) {
            corr = act[i]-'A'+10;
        } else if ( 'a' <= act[i] && act[i] <= 'f' ) {
            corr = act[i]-'a'+10;
        } else {
            corr = act[i]-'0';
        }
		res = ( res * 16 ) + corr;
	}
	return res;
}

/**
 * The function `convertStringToNum` converts a string to a number, either in hexadecimal or decimal
 * format based on the input string.
 * 
 * @param act The `act` parameter is a constant reference to a string that represents a numerical
 * value. The function `convertStringToNum` takes this string as input and converts it to an integer
 * value based on its format. If the string starts with "0x" and is determined to be a hexadecimal
 * number
 * 
 * @return The function `convertStringToNum` returns an integer value after converting the input string
 * `act` to a numerical value. The function checks if the input string represents a hexadecimal number
 * (if it starts with "0x" and is a valid hexadecimal number) and then converts it to a hexadecimal
 * number using the `toHexNum` function. If the input string is not a hexadecimal number, it
 */
int convertStringToNum( const string &act ) {
    int res;
    if ( act[0] == '0' && act[1] == 'x' && isFunction( act, isHex, 2 ) ) {
        res = toHexNum( act );
    } else {
        res = toDecNum( act );
    }
    return res;
}

/**
 * The function `tokenize_line` reads a line from a file, tokenizes it based on certain conditions, and
 * returns a vector of strings representing the tokens.
 * 
 * @param input The `tokenize_line` function you provided seems to tokenize a line read from a file
 * stream based on certain conditions. However, there are some issues in the implementation that need
 * to be addressed.
 * 
 * @return The function `tokenize_line` returns a vector of strings containing the tokens parsed from
 * the input file.
 */
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


#endif