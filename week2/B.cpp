#include <iostream>
#ifndef N
#define N 10
#endif

using namespace std;

void print_array(int (&a)[N]);

void shiftRight(int (&a)[N]) {
    int x;
    int y;
    x    = a[0];
    a[0] = a[N - 1];
    for (int i = 1; i < N; i++) {
        y    = a[i];
        a[i] = x;
        x    = y;
    }
}

void read_array(int (&a)[N]) {
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }
}

void print_array(int (&a)[N]) {
    for (int i = 0; i < N; i++) {
        cout << a[i] << " ";
    }
}

int main() {
    int a[N];
    read_array(a);
    shiftRight(a);
    print_array(a);
}