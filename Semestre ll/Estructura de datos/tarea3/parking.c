#include <stdio.h>

int main(){
    int i, cases, shops, var, max, min, k;
    
    scanf("%d", &cases);
    for(i = 1; i <= cases; i++){
        max = 0;
        min = 100;
        scanf("%d", &var);
        for(k = 1; k <= var; k++){
            scanf("%d", &shops);
            if(shops > max){
                max = shops;
            }if(shops < min){
                min = shops;
            }
        }
        printf("%d\n", (max - min) * 2);
    }
    return 0;
}
