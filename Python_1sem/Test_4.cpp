#include <iostream>

using namespace std;

int main()
{
    int a, b, c, D;
    a = 1, b = 3, c = 2;
    D = b * b - 4 * a * c;
    if(D < 0 or (a == 0 and b == 0))
    {
        cout << "Нет корней" << endl;
    }
    if(a == 0 and b != 0)
    {
        cout << -c / b << endl;
    }
    if(D == 0)
    {
        cout << -b / (2 * a) << endl;
        
    }
    if(D > 0)
    {
        cout << (-b - D) / (2 * a) << endl;
        cout << (-b + D) / (2 * a) << endl;
    }
}