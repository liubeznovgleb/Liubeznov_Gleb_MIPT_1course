#include <iostream>

using namespace std;


int a;

int fac(int a)
{
    return a / 5 + a / 25 + a / 125 + a / 625 + a / 3125 + a / 15625 + a / 78125;
}

int main()
{
    cin >> a;
    cout << fac(a) << endl;
}