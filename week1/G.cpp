#include <iostream>

using namespace std;

int n; int x_1; int x_2; int x_3; int c;

int local(int n)
{
    int c = 0;
    cin >> x_1 >> x_2;
    for (int i = 0; i < n - 2; i++)
    {
        cin >> x_3;
        if (x_1 < x_2 and x_2 > x_3)
        {
            c++;
        }
        if (x_1 > x_2 and x_2 < x_3)
        {
            c--;
        }
        x_1 = x_2;
        x_2 = x_3;
    }
    return c;
}

int main()
{
    cin >> n;
    c = local(n);
    if (c == 0)
    {
        cout << "EQUAL";
    }
    else if (c > 0)
    {
        cout << "MAX";
    }
    else
    {
        cout << "MIN";
    }  
}