#include <iostream>

using namespace std;

int main()
{
    int a, b, c, d;
    a = 169;
    b = c = 1;
    d = 0;
    while (a >= b * b + c * c)
    {   
        while (a >= b * b + c * c)
        {
            c ++;
            if (a == b * b + c * c)
            {
                cout << b << endl;
                cout << c << endl;
                b = c = a + 1;
                d = 1;
            }
            
        }
        b ++;
        c = 1;
    }
    if(d == 0)
    {
        cout << "Решений нет" << endl;
    }
    
        

}