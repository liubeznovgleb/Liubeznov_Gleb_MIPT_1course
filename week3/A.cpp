#include <iostream>
#ifndef N
#define N 5
#endif

using namespace std;

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

void selectSort(int (&a)[N]) {
    int k;
    int n = N;
    for (int j = 0; j < N; j++) {
        for (int i = 0; i < n; i++) {
            k = a[i];
            if (a[i] > a[i + 1]) {
                a[i] = a[i + 1];
                a[i + 1] = k;
            }
        }
        n = n - 1;
    }
}

int main() {
    int a[N];
    read_array(a);
    selectSort(a);
    print_array(a);
}