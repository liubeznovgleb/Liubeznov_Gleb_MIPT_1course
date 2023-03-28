#include <iostream>
using namespace std;
int main() {
    const int MAX_SIZE = 100;
    int arr[MAX_SIZE];
    int n = 0;
    
    // Считываем входной массив
    while (cin >> arr[n] && arr[n] != 0) {
        n++;
    }
    
    // Выводим разность соседних элементов
    for (int i = 0; i < n - 1; i++) {
        cout << arr[i] - arr[i+1] << " ";
    }
    
    return 0;
}