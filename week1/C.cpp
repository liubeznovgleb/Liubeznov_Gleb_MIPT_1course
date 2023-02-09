#include <iostream>

using namespace std;

int year(int a)
{
    if ((a % 4 == 0 and a % 100 != 0) or a % 400 == 0)
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }
    return 0;
}

int main()
{
    int a;
    cin >> a;
    year(a);
}