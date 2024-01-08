#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
    int n, i, number, bef, aft, k, indi, finalArray, indica;
    while(scanf("%d",&n) != EOF){
        int flag = 0;
        int array[3001];
        int finalArray[3001] = {0};
        int l = 1;
        for(i = 0; i < n; i++){
            scanf("%d", &number);
            finalArray[i] = 0;
            if(i == 0){
                bef = number;
            }if(i > 0){
                
            array[i] = abs(bef - number);
            bef = number;
                
            }
        }
        for(k = 1; k < n; k++){
            indi = array[k];
            
            if (indi < n){
            finalArray[indi] = 1;
            }
        }
        for(l = 1; l < n; l++){
            indica = finalArray[l];
            if(finalArray[indica] != 1){
                flag = 1;
            }
        }
        if(flag == 0){
            printf("Jolly\n");
        }else{
            printf("Not jolly\n");
        }  
    }
    return 0;
}
