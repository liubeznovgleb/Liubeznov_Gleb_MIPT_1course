#include <iostream>

using namespace std;

int N = 100000;

int a[1000000];

int research(int a[1000000]) {
    for (int i = 0; i < N; i++) {
        if (a[i] == N) {
            return 1;
        }
    }
    return 0;
}

int main(){
    for (int i = 0; i < N; i++) {
        a[i] = i;
    }
    cout << research(a) << endl;
}
