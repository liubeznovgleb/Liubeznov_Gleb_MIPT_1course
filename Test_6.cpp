#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    a = 169;
    b = c = 1;
    while (a >= b * b + c * c)
    {   
        while (a >= b * b + c * c)
        {
            c ++;
            if (a == b * b + c * c)
            {
                cout << b << endl;
                cout << c << endl;
                b = c = a;
            }
            
        }
        b ++;
        c = 1;
    }
        

}