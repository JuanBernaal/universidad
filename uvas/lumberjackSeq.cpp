/*
Author: Juan David Bernal Maldonado
12/03/2023
*/

#include <iostream>
#include <vector>

using namespace std;

int main(){
    int cases;
    cin >> cases;
    vector<int> v;
    string ans;
    cout << "Lumberjacks:" << endl;

    // Test cases
    for(int i = 0; i < cases; i++){

        // Add lumberjacks to the vector
        for(int j = 0; j < 10; j++){
            int lenght;
            cin >> lenght;
            v.push_back(lenght);
        }

        // Case 1: Lowest to highest
        int max = v[0];
        bool flagLH = true;
        for(int j = 1; j < v.size(); j++){
            if(max < v[j])
                max = v[j];
            else
                flagLH = false;
        }

        // Case 2: Higher to lowest
        int min = v[0];
        bool flag = true;
        for(int i = 1; i < v.size(); i++){
            if(min > v[i])
                min = v[i];
            else
                flag = false;
        }

        // No matter if it is Lower to higher or Higher to lower, it is an orden
        if(flagLH == true || flag == true)
            cout << "Ordered" << endl;          
        else
            cout << "Unordered" << endl;
        
        v.clear();
    }
        
    return 0;
}