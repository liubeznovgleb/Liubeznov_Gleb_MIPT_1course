#include <iostream>

using namespace std;

int i;

int fibonacci(unsigned i)
{
    if (i == 0)
    {
        return 0;
    }
    if (i == 1)
    {
        return 1;
    }
    return fibonacci(i - 1) + fibonacci(i - 2); 
}

int main()
{
    cin >> i;
    cout << fibonacci(i) << endl;
}