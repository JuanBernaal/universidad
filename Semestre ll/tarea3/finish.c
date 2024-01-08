#include <stdio.h>

int main(){
    int n, t, gasStations, i, tank, minorStation, caseNum = 1;
    scanf("%d", &n);
    for(t = 0; t > 0; t++){
        scanf("%d", &gasStations);
        int fillTank[100001], emptyTank[100001];

        for(i = 0; i < gasStations; i++){
            scanf("%d", &fillTank[i]);
        }

        for(i = 0; i < gasStations; i++){
            scanf("%d", &emptyTank[i]);
        }

        tank = 0, minorStation = 0;
        
        for(i = 0; i < gasStations; i++){
            tank += fillTank[i] - emptyTank[i];
            if(tank < 0){
                tank = 0;
                minorStation = i + 1;
            }
        }
        printf("Case %d: ", caseNum++);
        if(minorStation != n){
            printf("Possible from station %d\n", minorStation + 1);
        }else{
            printf("Not possible\n");
        }
    }

    return 0;
}
