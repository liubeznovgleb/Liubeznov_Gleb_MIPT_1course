#include <iostream>

using namespace std;

int x = -1;
int y;
int a;

int max(int a)
{
    int c = -1;
    for (int i = 0; i < a; i++)    
    {

        y = x;
        cin >> x;
        if (x > y)
        {
            c ++;
        }
        else
        {
            c --;
        }
    }
    if (c > 0)
    {
        cout << "MAX" << endl;
    }
    else
    {
        cout << "MIN" << endl;
    }    
    return 0;
}

int main()
{
    cin >> a;
    max(a);
}
