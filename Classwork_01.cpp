#include <iostream>

using namespace std;

int my_max(int a, int b)
{
    return (a >= b)? a: b;
}

int my_max(int a, int b, int c)
    {
        return my_max(my_max(a, b), c);
    }

int main()
{
    int a = my_max(5, 7, 8);
    cout << a << endl;
}
