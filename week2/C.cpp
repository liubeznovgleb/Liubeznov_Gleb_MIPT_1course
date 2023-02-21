#include <iostream>
#ifndef N
#define N 6
#endif

using namespace std;

void print_array(int (&a)[N]);

void shiftRight(int (&a)[N], int k) {
    int(a1)[k];
    int(a2)[N - k];
    int t_1 = 0;
    int t_2 = 0;
    for (int i = 0; i < k; i++) {
        a1[i] = a[N - k + i];
    }
    for (int i = 0; i < N - k; i++) {
        a2[t_1] = a[i];
        t_1++;
    }
    for (int i = 0; i < k; i++) {
        a[i] = a1[i];
    }
    for (int i = k; i < N; i++) {
        a[i] = a2[t_2];
        t_2++;
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
    int k;
    cin >> k;
    read_array(a);
    shiftRight(a, k);
    print_array(a);
}