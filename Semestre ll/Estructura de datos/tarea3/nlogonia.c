#include <stdio.h>

int main(){
    int input, x, y, _, x1, y1;
    scanf("%d", &input);
    scanf("%d", &x);
    scanf("%d", &y);
    while(input != 0){
        for(_ = 1; _ <= input; _++){
           scanf("%d", &x1);
           scanf("%d", &y1); 
           if((x1 == x) || (y1 == y)){
            printf("divisa\n");
           }else if((x1 < x) && (y1 > y)){
            printf("NO\n");
           }else if((x1 > x) && (y1 > y)){
            printf("NE\n");
           }else if((x1 > x) && (y1 < y)){
            printf("SE\n");
           }else if((x1 < x) && (y1 < y)){
            printf("SO\n");
           }
        }
        scanf("%d", &input);
        if(input != 0){
            scanf("%d", &x);
            scanf("%d", &y);
        }
    }
    return 0;
}
