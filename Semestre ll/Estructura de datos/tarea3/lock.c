#include <stdio.h>

int main(){
    int initial, first, second, third;
    scanf("%d %d %d %d", &initial, &first, &second, &third);
    while((initial + first + second + third) != 0){
        int ans = 720; 
        ans += (initial - first + 40) % 40 * 9;
        ans += 360;
        ans += (second - first + 40) % 40 * 9;
        ans += (second - third + 40) % 40 * 9;
        printf("%d\n", ans);
        scanf("%d %d %d %d", &initial, &first, &second, &third);
    }
}