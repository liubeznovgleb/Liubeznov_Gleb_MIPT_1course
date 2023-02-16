#include <iostream>

using namespace std;



int pol(int a)
{
    int c = 1;
    int x = a;
    int d = 10;
    while (x > 0)
    {
        d *= 10;
        x /= 10;
    }
    while (a > 0)
    {
        d /= 100;
        if (a % 10 != a / d)
        {
            c = 0;
        }
        a = (a - (a / d * d) - (a % 10)) / 10;
    }
    return c;
    
}

int main()
{
    int a;
    cin >> a;
    cout << ((pol(a) == 1)? "YES": "NO") << endl;
}
