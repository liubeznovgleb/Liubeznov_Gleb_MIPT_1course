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
    cout << endl;
}

void doubleSelectSort(int (&a)[N]) {
    int min;
    int max;
    int k = 0;
    int p;
    int mink;
    int maxk;
    for (int j = 0; j < N / 2; j++) {
        min = a[j];
        max = a[j];
        for (int i = j; i < N - j; i++) {
            if (a[i] >= max) {
                max = a[i];
                maxk = i;
            }
            if (a[i] <= min) {
                min = a[i];
                mink = i;
            }
        }
        cout << min << endl;
        cout << max << endl;
        cout << mink << " " << maxk << endl;
        if (mink == N - 1 - j or maxk == j)
        {
            a[mink] = a[j];
            a[j] = min;
            print_array(a);
        }
        else{
            a[mink] = a[j];
            a[j] = min;
            a[maxk] = a[N - j];
            a[j] = max;
        }
    }
}

int main() {
    int a[N];
    // read_array(a);
    // doubleSelectSort(a);
    // print_array(a);
    while (true)
    {
        cout << "хуй" << endl;
    }
    
}