#include <iostream>
#ifndef N
#define N 3
#endif

using namespace std;

void mergeArrays(int (&a)[N], int (&b)[N], int (&c)[2 * N])
{
    int t = 0; int k = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = k; j < N; j++)
        {
            if (b[j] <= a[i])
            {
                c[t] = b[j];
                k ++;
                t ++;
            }
        }
        c[t] = a[i];
        t ++;
        
        
    }
    for (int j = k; j < N; j++)
    {
        c[t] = b[j];
        t ++;
    }
    
    
}

void read_array(int (&a)[N], int(&b)[N])
{
    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < N; i++)
    {
        cin >> b[i];
    }
}

void print_array(int (&c)[2 * N])
{
    for (int i = 0; i < 2 * N; i++)
    {
        cout << c[i] << " ";
    }
}

int main()
{
    int a[N]; int b[N]; int c[2 * N];
    read_array(a, b);
    mergeArrays(a, b, c);
    print_array(c);
}