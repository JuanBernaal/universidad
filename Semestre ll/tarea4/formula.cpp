#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector<int> buildVector(string positions){
    vector<int> ans;
    string concatenar = "";
    for(int i = 0; i < positions.size(); i++){
        if(positions[i] != ' '){
            concatenar += positions[i];
        }
        else{
            ans.push_back(stoi(concatenar));
            concatenar = "";
        }
    }
    if(concatenar != ""){
        ans.push_back(stoi(concatenar));
    }
    return ans;
}

int findChampion(vector<vector<int>> arrival, vector<vector<int>> points, int p){
    vector<int> accumulatedPoints(p+1);
    for(int i = 0; i < arrival.size(); i++){
        for(int j = 1; j < arrival[i].size(); j++){
            int pilot = arrival[i][j];
            int pointsEarned = points[i][j + 1];
            accumulatedPoints[pilot] += pointsEarned;
        }
    }
}

int main(){
    int g, p;
    scanf("%d %d", &g, &p);
    while(g != 0 && p != 0){
        vector<vector<int>> arrivalOrderMat;
        cin.ignore();
        for(int i = 0; i < g; i++){
            string arrivalOrder;
            getline(cin, arrivalOrder);
            arrivalOrderMat.push_back(buildVector(arrivalOrder));
        }
        int s;
        vector<vector<int>> scoreSystemMat;
        scanf("%d", &s);
        cin.ignore();
        for(int i = 0; i < s; i++){
            string scoreSystem;
            getline(cin, scoreSystem);
            scoreSystemMat.push_back(buildVector(scoreSystem));
        }
        scanf("%d %d", &g, &p); 
    }   
    return 0; 
}