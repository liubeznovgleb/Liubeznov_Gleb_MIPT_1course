#include <iostream>
#ifndef N
#define N 5
#endif

using namespace std;

int findLastZero(int (&a)[N]) {
    int t = 0;
    int i = N / 2 - 1;
    int k = 1;
    while (t != 1) {
        if (a[i] == 0 and a[i + 1] == 1) {
            t = 1;
        }
        if (a[i] == 0 and a[i + 1] == 0) {
            i = i + (N / (2 * k));
            k *= 2;
        }
        if (a[i] == 1 and a[i + 1] == 1) {
            i = i - (N / (2 * k));
            k *= 2;
        }
    }
    return i;
}

void read_array(int (&a)[N]) {
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }
}

int main() {
    int a[N];
    read_array(a);
    cout << findLastZero(a) << endl;
}