#include <iomanip>
#include <iostream>
using namespace std;
int main() {
    short int *ptr;   // объявление указателя на short int
    ptr = new short int[10];   // выделение памяти на 10 элементов
    for (int i = 0; i < 10; i++) {
        ptr[i] = i;   // присвоение каждому элементу значение равное его индексу
        cout << hex << setw(2) << setfill('0') << (long long)(ptr + i)
             << " ";   // вывод 16-теричного представления каждого указателя
    }
    cout << endl;
    for (int i = 0; i < 10; i++) {
        cout << ptr[i] << " ";   // вывод значения каждого элемента массива
    }
    cout << endl;
    for (int i = 0; i < 10; i += 2) {
        *(ptr + i) *= *(ptr + i);   // изменение значения каждого второго
                                    // элемента массива, возведение в квадрат
    }
    for (int i = 0; i < 10; i++) {
        cout << ptr[i] << " ";   // вывод всех значений в массиве
    }
    delete[] ptr;   // освобождение выделенной памяти
    return 0;
}