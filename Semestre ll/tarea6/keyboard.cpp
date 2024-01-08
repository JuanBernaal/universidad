/* 
    Juan David Bernal Maldonado
    8977771

    La complejidad de este codigo es O(1) porque el tiempo
    de insercion de los datos es 0(1). 
*/
#include <list>
#include <iostream>
#include <string>

using namespace std;

int main(){
    string input;
    while(getline(cin, input) && input != "EOF"){
        list<char> txt;
        list<char>::iterator cursor = txt.begin();
        for(int i = 0; i < input.size(); i++){
            if(input[i] == '['){
                cursor = txt.begin();
            }else if(input[i] == ']'){
                cursor = txt.end();
            }if(input[i] != '[' && input[i] != ']'){
                txt.insert(cursor, input[i]);
            }
        }
        for(list<char>::iterator it = txt.begin(); it != txt.end(); ++it){
            cout << *it;
        }
        printf("\n");
    }
    return 0;
}
