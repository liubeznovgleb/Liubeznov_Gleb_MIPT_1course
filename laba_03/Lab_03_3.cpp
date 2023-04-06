#include <iostream>
#include <random>
#include <stdlib.h>
#include <time.h>

using std::cin;
using std::cout;
using std::endl;

std::default_random_engine rng((int)time(0));

const int N = 3;

struct Node
{
    int x;
    // int y;
    int cond = 1;
    int x_prev = x;
    // int y_prev = y;
};

int Sluch_4() {
    int arr[] = {1, 2, 3, 4};
    // std::default_random_engine rng(i + 41 * (int)time(0));
    std::uniform_int_distribution<unsigned> dstr(0, 3);
    int x = arr[dstr(rng)];
    for (unsigned counter = 1; counter != 0; --counter)
        return arr[dstr(rng)] % 2 + 1;
    return 0;
}

Node *random_vector(int x, int y) {
    Node *v = new Node;
    srand(time(NULL));
    v->x = Sluch_4() % x + 1;
    //  v->y = Sluch_4() % y + 1;
    //v->x = x / 2;
    // v->y = y / 2;
    return v;
}

void print_vector(Node *v) { cout << v->x << " " << v->cond << endl; }

void moving_mass(Node *a[N], int x, int y) {
    for (int i = 0; i < N; i++) {
        if (a[i]->x == 1 or a[i]->x == x) {
            a[i]->cond = 0;
        } else if (a[i]->cond == 1) {
            int m = Sluch_4();
            if (m == 1) {
                a[i]->x = (a[i]->x - 1);
                a[i]->x_prev = a[i]->x + 1;
            } else if (m == 2) {
                a[i]->x = (a[i]->x + 1);
                a[i]->x_prev = a[i]->x - 1;
            } else if (m == 3) {
                a[i]->x = (a[i]->x - 1);
                a[i]->x_prev = a[i]->x + 1;
            } else if (m == 4) {
                a[i]->x = (a[i]->x + 1);
                a[i]->x_prev = a[i]->x - 1;
                // print_vector(a[i]);
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (a[i]->x == a[j]->x) {
                    a[i]->x = a[i]->x_prev;
                    // a[i]->y = a[i]->y_prev;
                }
                if (a[i]->x - a[j]->x == 1 or a[i]->x - a[j]->x == -1) {
                    a[i]->cond = 0;
                    a[j]->cond = 0;
                }
            }
        }
    }
}

int carrot(Node *a[N], int x, int y) {
    int w = 0;
    int count = N;
    while (count > 0) {
        count = 0;
        for (int i = 0; i < N; i++) {
            if (a[i]->cond == 1) {
                count++;
            }
        }
        if (count > 0) {
            moving_mass(a, x, y);
            w++;
        }
        count = 0;
        for (int i = 0; i < N; i++) {
            if (a[i]->cond == 1) {
                count++;
            }
        }
    }
    return w;
}

Node *mass(int N, int x, int y) {
    Node *a[N];
    for (size_t i = 0; i < N; i++) {
        a[i] = random_vector(x, y);
    }
    return *a;
}

int main() {
    int x;
    int y;
    Node *a[N];
    // cin >> x;
    // cin >> y;
    int count = N;
    for (int j = 10; j < 205; j++) {
        int s = 0;
        // cout << "j = " << j << endl;
        x = j - 1;
        y = j - 1;
        for (int k = 0; k < 100; k++) {
            for (int i = 0; i < N; i++) {
                a[i] = random_vector(x, y);
            }
            // print_vector(a[1]);
            int w = 0;
            s += carrot(a, x, y);
        }
        cout << s / 100 << ", ";
    }
}