#include <iostream>
#include <vector>
#include <map>

using namespace std;

vector<string> split(string s){
    vector<string> ans;
    string word = "";
    for(int i = 0; i < s.size(); i++){
        if(s[i] == ' '){
            ans.push_back(word);
            word = "";
        }else
            word += s[i];
    }
    ans.push_back(word);
    return ans;
}

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