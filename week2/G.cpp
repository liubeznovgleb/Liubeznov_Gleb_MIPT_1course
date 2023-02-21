#include <iostream>
#ifndef N
#define N 7
#endif

using namespace std;

int findUnique(int (&a)[N]) {
    int t = 1;
    for (int i = 0; i < N; i++) {
        if (t % a[i] == 0) {
            t /= a[i];
        } else {
            t *= a[i];
        }
    }
    return t;
}

void read_array(int (&a)[N]) {
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }
}

int main() {
    int a[N];
    read_array(a);
    cout << findUnique(a) << endl;
}