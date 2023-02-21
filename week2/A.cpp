#include <iostream>
#ifndef N
#define N 1
#endif

using namespace std;

void reverseArray(int (&a)[N]) {
    int x;
    for (int i = 0; i < (N + 1) / 2; i++) {
        x        = a[i];
        a[i]     = a[N - i];
        a[N - i] = x;
    }
}

void read_array(int (&a)[N]) {
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }
}

void print_array(int (&a)[N]) {
    for (int i = 1; i <= N; i++) {
        cout << a[i] << " ";
    }
}

int main() {
    int a[N];
    read_array(a);
    reverseArray(a);
    print_array(a);
}