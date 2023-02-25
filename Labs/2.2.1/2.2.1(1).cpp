#include <iostream>
#include <math.h>
#ifndef N
#define N 276
#endif

using namespace std;

void lon(float (&a)[N]) {
    for (int i = 0; i < N; i++) {
        a[i] = log(32.5201 / a[i]);
    }
}

void read_array(float (&a)[N]) {
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }
}

void print_array(float (&a)[N]) {
    for (int i = 0; i < N; i++) {
        cout << a[i] << ", ";
    }
}

int main() {
    float a[N];
    read_array(a);
    lon(a);
    print_array(a);
}