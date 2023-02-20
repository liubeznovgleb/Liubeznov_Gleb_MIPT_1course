#include <iostream>
#ifndef N
#define N 5
#endif

using namespace std;

int b[N];

int AmountPositive(int (&)[N]);

void moveNegativeToEnd(int (&a)[N])
{ 
    int t = AmountPositive(a);
    int k = 0;
    for (int i = 0; i < N; i++)
    {
        if (a[i] > 0)
        {
            b[k] = a[i];
            k ++;
        }
        else
        {
            b[t] = a[i];
            t ++;
        }
        
    }
    
}

int AmountPositive(int (&a)[N])
{
    int t = 0;
    for (int i = 0; i < N; i++)
    {
        if (a[i] > 0)
        {
            t ++;
        }  
    }
    return t;
}


void read_array(int (&a)[N])
{
    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
    }
}

void print_array(int (&a)[N])
{
    for (int i = 0; i < N; i++)
    {
        cout << b[i] << " ";
    }
}

int main()
{
    int a[N]; int k;
    read_array(a);
    moveNegativeToEnd(a);
    print_array(a);
}