/*
Autor: Juan David Bernal Maldonado
01/08/2024
*/

#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(){
    int cases, num, max;
    string link;
    vector<string> links;

    cin >> cases;

    for(int i = 0; i < cases; i++){
        for(int j = 0; j < 10; j++){
            cin >> link >> num;
            if(j == 0){
                links.push_back(link);
                max = num;
            }else if(num > max){
                max = num;
                links.clear();
                links.push_back(link);
            }else if(num == max)
                links.push_back(link);
        }
        printf("Case #%d:\n", i + 1);
        for(int i = 0; i < links.size(); i++){
            cout << links[i] << endl;
        }
    }

    

    return 0;
}