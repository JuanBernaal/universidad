/*
Autor: Juan David Bernal Maldonado
MM/DD/YY: 11/27/2023
*/

#include <vector>
#include <iostream>

using namespace std;

vector<int> makeList(int a, int b, int c, int d, int e, int f){
    vector<int> ans;
    ans.push_back(a);
    ans.push_back(b);
    ans.push_back(c);
    ans.push_back(d);
    ans.push_back(e);
    ans.push_back(f);

    return ans;
}

// Encuentra el menor valor de una lista
int minor(vector<int> v){
    int min = v[0];
    for(int i = 1; i < 6; i++){
        if(v[i] < min)
            min = v[i]; 
    }
    return min;
}

int main(){
    int bottle;
    while(cin >> bottle){
        vector<int> bin1, bin2, bin3;
        bin1.push_back(bottle);
        for(int i = 1; i < 9; i++){
            cin >> bottle;
            if(i < 3)
                bin1.push_back(bottle);
            else if(i < 6)
                bin2.push_back(bottle);
            else
                bin3.push_back(bottle);
        }
        
        int BCG, BGC, CBG, CGB, GBC, GCB;

        // Estas sumas son la fuerza bruta para encontrar el menor.

        BCG = bin2[0] + bin3[0] + bin1[2] + bin3[2] + bin1[1] + bin2[1];
        BGC = bin2[0] + bin3[0] + bin1[1] + bin3[1] + bin1[2] + bin2[2];
        CBG = bin2[2] + bin3[2] + bin1[0] + bin3[0] + bin1[1] + bin2[1];
        CGB = bin2[2] + bin3[2] + bin1[1] + bin3[1] + bin1[0] + bin2[0];
        GBC = bin2[1] + bin3[1] + bin1[0] + bin3[0] + bin1[2] + bin2[2];
        GCB = bin2[1] + bin3[1] + bin1[2] + bin3[2] + bin1[0] + bin2[0];

        vector<int> lst = makeList(BCG, BGC, CBG, CGB, GBC, GCB);
        int ans = minor(lst);
        string s;

        if(ans == BCG)
            s = "BCG";

        else if(ans == BGC)
            s = "BGC";
        
        else if(ans == CBG)
            s = "CBG";

        else if(ans == CGB)
            s = "CGB";

        else if(ans == GBC)
            s = "GBC";

        else if(ans == GCB)
            s = "GCB";

        cout << s << " " << ans << endl;
    }

    return 0;
}