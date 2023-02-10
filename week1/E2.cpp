#include <iostream>

using namespace std;

int base; int power;

int my_power(int base, int power)
{
    int y = 1;
    if (power == 0)
    {
        return 1;
    }
    
    for (int i = 0; i < power; i++)
    {
        y *= base;
    }
    return y;
}

int main()
{
    cin >> base >> power;
    cout << my_power(base, power) << endl;
}