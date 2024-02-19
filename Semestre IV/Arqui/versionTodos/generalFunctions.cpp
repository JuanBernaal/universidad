
#ifndef GENERAL_FUNCTIONS
#define GENERAL_FUNCTIONS

#include <string>
#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>

using namespace std;

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

bool isDec( char act ) {
	bool res = ( '0' <= act && act <= '9' );
	return res;
}
bool isHex( char act ) {
	bool res = isDec( act ) || ( 'A' <= act && act <= 'F' );
	return res;
}
bool isFunction( const string &act, bool ( *fun ) ( char ) ) {
	bool res = true;
	int i;
	for ( i = 0 ; i < act.size() && res ; ++i ) res = fun( act[i] );
	if ( !res ) fprintf( stderr, "Salio en %d con |%c|\n", i, act[i] );
	return res;
}
bool isFunction( const string &act, bool ( *fun ) ( char ), int strt ) {
	bool res = true;
	int i;
	for ( i = strt ; i < act.size() && res ; ++i ) res = fun( act[i] );
	if ( !res ) fprintf( stderr, "Salio en %d con |%c|\n", i, act[i] );
	return res;
}

bool isNumber( const string &act ) {
    bool res = ( isFunction( act, isDec ) || ( act.size() >= 3 && act[0] == '0' && act[1] == 'x' && isFunction( act, isHex, 2 ) ) );
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

int convertStringToNum( const string &act ) {
    int res;
    if ( act[0] == '0' && act[1] == 'x' && isFunction( act, isHex, 2 ) ) {
        res = toHexNum( act );
    } else {
        res = toDecNum( act );
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


#endif