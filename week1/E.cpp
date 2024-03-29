#include <iostream>

using namespace std;

int base; int power;

int recursive_power(int base, int power)
{
    if (power == 0)
    {
        return 1;
    }
    else
    {
        return base * recursive_power(base, power - 1);
    } 
}

int main()
{
    cin >> base >> power;
    cout << recursive_power(base, power) << endl;
}