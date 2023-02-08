#include <iostream>

using namespace std;

int main()
{
    int a, b;
    a = 60;
    b = 40;
    while (a != b)
    {
        if (a > b)
        {
            a = a - b;
        }
        else
        {
            b = b - a;
        }  
    }
    cout << a << endl;
}