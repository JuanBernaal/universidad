#include <iostream>
#include <vector>

using namespace std;

class BigInteger{
    private:
        vector<int> number;
        int sign;
    public:
        BigInteger(){
        }
        BigInteger(const string &str){                    /* Constructor. */
            sign = 1;
            if(str[0] == '-')
                sign = -1;
            for(int i = str.size() - 1; i > 0; i--){
                int var = str[i] - 48;
                number.push_back(var);  
            }
            if(str[0] != '-'){
                int var = str[0] - 48;
                number.push_back(var);
            }
        }

        bool operator< (BigInteger &num){
            bool ans;
            if(sign != num.sign)
                ans = sign < num.sign;
            else if(number.size() != num.number.size()){
                if(sign == -1 && num.sign == -1)
                    ans = number.size() > num.number.size();
                else
                    ans = number.size() < num.number.size();
            }else{
                int i = num.number.size() - 1;
                while(number[i] == num.number[i])
                    i--;
                if(sign == 1 && num.sign == 1)
                    ans = number[i] < num.number[i];
                else
                    ans = number[i] > num.number[i]; 
            }if(*this == num){
                ans = false;
            }
            return ans;
        }
        bool operator== (BigInteger &num){
            return number == num.number && sign == num.sign;
        }

        string toString(){
            string ans;
            if(sign == -1)
                ans += "-";
            for(int i = number.size() - 1; i >= 0; i--){
                char l = number[i] + 48;  
                ans += l;
            }
            return ans;
        }
};

void clearStrings(string &s1, string &s2, string &s3, string &s4){
    s1 = "";
    s2 = "";
    s3 = "";
    s4 = "";
}

void matchStrings(string &str1, string &str2){
    if(str1.size() != str2.size()){
        if(str1.size() < str2.size()){
            while(str1.size() < str2.size())
                str1 += "0";
        }else if(str1.size() > str2.size()){
            while(str1.size() > str2.size())
                str2 += "0";
        }
    }
}

int main(){
    string int1, float1, int2, float2, input;
    int cont = 1;
    while(getline(cin, input)){
        int i = 0;
        string ans;
        while(input[i] != '.'){
            int1 += input[i];
            i++;
        }i++;
        while(input[i] != ' '){
            float1 += input[i];
            i++;
        }i++;
        while(input[i] != '.'){
            int2 += input[i];
            i++;
        }i++;
        while(i != input.size()){
            float2 += input[i];
            i++;
        }

        matchStrings(float1, float2);

        BigInteger b1(int1);
        BigInteger f1(float1);
        BigInteger b2(int2);
        BigInteger f2(float2);

        if(b1 < b2)
            ans = "Smaller";
        else if(b1 == b2){
            if(f1 == f2)
                ans = "Same";
            else if(f1 < f2)
                ans = "Smaller";
            else
                ans = "Bigger";
        }else
            ans = "Bigger"; 

        cout << "Case " << cont << ": " << ans << endl;
        cont++;

        clearStrings(int1, float1, int2, float2);
    }
    return 0;
}