#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector<string> morseCode = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
                          ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", ".-.-.-", "--..--", "..--..", ".----.", "-.-.--",
                          "-..-.", "-.--.", "-.--.-", ".-...", "---...", "-.-.-.", "-...-", ".-.-.", "-....-", "..--.-", ".-..-.", ".--.-."};
vector<string> symbols = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5",
                          "6", "7", "8", "9", ".", ",", "?", "'", "!", "/", "(", ")", "&", ":", ";", "=", "+", "-", "_", "\"", "@"};


vector<string> dotSplit(string word){
    vector<string> lista;
    string concatenar;
    for(int i = 0; i < word.size(); i++){
        if(word[i] != ' '){
            concatenar += word[i];
        }if(word[i] == ' ' || i == word.size() -1){
            lista.push_back(concatenar);
            concatenar = "";
        }if(word[i] == ' ' && word[i + 1] == ' '){
            concatenar += " ";
        }
    }
    return lista;
}

int main(){
    int numCases;
    vector<string> morseList;
    string inptMorse;
    vector<string> listaFinal;
    scanf("%d", &numCases);
    cin.ignore();
    for(int i = 0; i < numCases; i++){
        if(i > 0){
            printf("\n");
        }
        getline(cin, inptMorse);
        morseList = dotSplit(inptMorse);
        printf("Message #%d\n", i + 1);
        for(int j = 0; j < morseList.size(); j++){
            int flag = 0;
            for(int k = 0; k < morseCode.size() && flag == 0;k++){
                if(morseList[j] == morseCode[k]){
                    cout << symbols[k];
                }else if(morseList[j] == " "){
                    cout << " ";
                    flag = 1;
                }
            }
        }
        if(i < numCases){
            printf("\n");
        }
    }
    return 0;
}
