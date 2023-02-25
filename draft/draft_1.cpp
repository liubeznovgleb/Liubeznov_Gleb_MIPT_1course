#include <iostream>

using namespace std;

void fact(int &a) {
    int res = 1;
    for (int i = 1; i <= a; i++) {
        res *= i;
    }
    cout << res << endl;
}

int main() {
    int a;
    cin >> a;
    fact(a);
}