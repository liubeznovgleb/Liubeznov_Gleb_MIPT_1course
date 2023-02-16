#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    a = 100, b = 1;
    while(b <= a)
    {   
        c = 2;
        while (c < b)
        {
            if (b % c == 0)
            {
                c = b + 1;
            }
            c ++;
        }
        if (c == b)
        {
            cout << b << endl;
        }
        b ++;      
    }
}