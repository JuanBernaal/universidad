/* 
    Autor: Juan David Bernal Maldonado. 
    Codigo: 8977771

    Complejidad computacional:
    La complejidad general de este codigo es de O(n^2) porque se recorre una lista y
    se elimina un elemento de ella.
*/
#include <iostream>
#include <list>
#include <string>
#include <algorithm>

using namespace std;
typedef list<int>::iterator Iterator;

int main(){
    int p, c, num, caseNumber = 1;
    list<int> queue, attended;
    char input;
    scanf("%d %d", &p, &c);
    while(p != 0 && c != 0){
        int limit = 1;
        while(limit <= p && limit < 1001){
            queue.push_back(limit);
            limit++;
        }
        for(int i = 0; i < c; i++){
            cin >> input;
            if(input == 'N'){
                Iterator it = queue.begin();
                attended.push_back(*it);
                queue.push_back(*it);
                queue.erase(it);
            }else{
                int num;
                bool flag = true;
                cin >> num;
                if(num > 1000){
                    queue.push_front(num);
                }else{
                    for(Iterator it = queue.begin(); it != queue.end() && flag; it++){
                        if(*it == num){
                            queue.push_front(*it);
                            queue.erase(it);
                            flag = false;
                        }
                    }
                }
            }
        }
        printf("Case %d:\n", caseNumber);
        caseNumber++;
        for(Iterator it = attended.begin(); it != attended.end(); it++){
            cout << *it << endl;
        }
        queue.clear();
        attended.clear();
        scanf("%d %d", &p, &c);
    }
    return 0;
}
