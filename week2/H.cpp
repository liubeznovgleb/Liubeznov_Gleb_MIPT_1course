#include <iostream>
#ifndef N
#define N 1
#endif
#ifndef M
#define M 3
#endif

using namespace std;

void print_transposed(int (&a)[N][M]) {
    int m = 0;
    for (int j = 0; j < M; j++) {
        for (int i = 0; i < N; i++) {
            cout << a[i][j] << " ";
            m++;
            if (m % N == 0) {
                cout << endl;
            }
        }
    }
}

void read_array(int (&a)[N][M]) {
    int d = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> a[i][j];
        }
    }
}

int main() {
    int a[N][M];
    read_array(a);
    print_transposed(a);
}