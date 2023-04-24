#include <iostream>
#include <random>
#include <stdlib.h>
#include <time.h>

using std::cin;
using std::cout;
using std::endl;

std::default_random_engine rng((int)time(0));

const int N = 200;

struct Node
{
    int x;
    int y;
    int cond = 1;
    int x_prev = x;
    int y_prev = y;
};

int Sluch_4() {
    int arr[] = {
        1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14,
        15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,
        29,  30,  31,  32,  33,  34,  35,  36,  37,  38,  39,  40,  41,  42,
        43,  44,  45,  46,  47,  48,  49,  50,  51,  52,  53,  54,  55,  56,
        57,  58,  59,  60,  61,  62,  63,  64,  65,  66,  67,  68,  69,  70,
        71,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,  84,
        85,  86,  87,  88,  89,  90,  91,  92,  93,  94,  95,  96,  97,  98,
        99,  100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
        113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
        127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140,
        141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154,
        155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
        169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182,
        183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196,
        197, 198, 199, 200};
    // std::default_random_engine rng(i + 41 * (int)time(0));
    std::uniform_int_distribution<unsigned> dstr(0, 199);
    int x = arr[dstr(rng)];
    for (unsigned counter = 1; counter != 0; --counter)
        return arr[dstr(rng)];
    return 0;
}

Node *random_vector(int x, int y) {
    Node *v = new Node;
    srand(time(NULL));
    v->x = Sluch_4() % (x - 1) + 1;
    v->y = Sluch_4() % (y - 1) + 1;
    // cout << v->x << " " << v->y << endl;
    //  v->x = x / 2;
    //  v->y = y / 2;
    return v;
}

Node *null_vector() {
    Node *v = new Node;
    v->cond = 0;
    v->x = v->y = 1;
}

void print_vector(Node *v) {
    cout << v->x << " " << v->y << " " << v->cond << endl;
}

void moving_mass(Node *a[N], int x, int y, int j) {
    for (int i = 0; i < j; i++) {
        // print_vector(a[i]);
        if (a[i]->x == 1 or a[i]->x == x or a[i]->y == 1 or a[i]->y == y) {
            a[i]->cond = 0;
        } else if (a[i]->cond == 1) {
            int m = Sluch_4() % 4 + 1;
            if (m == 1) {
                a[i]->x = (a[i]->x - 1);
                a[i]->x_prev = a[i]->x + 1;
            } else if (m == 2) {
                a[i]->x = (a[i]->x + 1);
                a[i]->x_prev = a[i]->x - 1;
            } else if (m == 3) {
                a[i]->y = (a[i]->y - 1);
                a[i]->y_prev = a[i]->y + 1;
            } else if (m == 4) {
                a[i]->y = (a[i]->y + 1);
                a[i]->y_prev = a[i]->y - 1;
            }
        }
        // print_vector(a[i]);
    }
    for (int i = 0; i < j; i++) {
        for (int k = i + 1; k < j; k++) {
            if (a[i]->x == a[k]->x and a[i]->y == a[k]->y) {
                a[i]->x = a[i]->x_prev;
                a[i]->y = a[i]->y_prev;
            }
            if ((a[i]->x == a[k]->x and
                 (a[i]->y - a[k]->y == 1 or a[i]->y - a[k]->y == -1)) or
                (a[i]->y == a[k]->y and
                 (a[i]->x - a[k]->x == 1 or a[i]->x - a[k]->x == -1))) {
                a[i]->cond = 0;
                a[k]->cond = 0;
            }
        }
    }
}

void check(Node *a[N], int x, int y, int j) {
    int n = j;
    for (int i = 0; i < j; i++) {
        // print_vector(a[i]);
        if (a[i]->x == 1 or a[i]->x == x or a[i]->y == 1 or a[i]->y == y) {
            a[i]->cond = 0;
        }
        for (int i = 0; i < j; i++) {
            for (int k = i + 1; k < n; k++) {
                if (a[i]->x == a[k]->x and a[i]->y == a[k]->y) {
                    a[k]->cond = 0;
                }
            }
        }
    }
}

int carrot(Node *a[N], int x, int y, int j) {
    int w = 0;
    int count = j;
    check(a, x, y, j);
    while (count > 0) {
        count = 0;
        for (int i = 0; i < j; i++) {
            if (a[i]->cond == 1) {
                count++;
            }
        }
        if (count > 0) {
            moving_mass(a, x, y, j);
            w++;
        }
        count = 0;
        for (int i = 0; i < j; i++) {
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
    int n = 100;
    // int array[n];              // array on stack
    // int *array = new int[n];   // array on heap (n can be non-const)
    int x;
    int y;
    Node *a[N];
    // cin >> x;
    // cin >> y;
    int count = N;
    for (int j = 2; j < 70; j+=6) {
        int s = 0;
        // cout << "j = " << j << endl;
        x = 10;
        y = 10;
        for (int k = 0; k < 10000; k++) {
            Node *a[N];
            for (int i = 0; i < j; i++) {
                a[i] = random_vector(x, y);
            }
            // print_vector(a[1]);
            int w = 0;
            s += carrot(a, x, y, j);
        }
        cout << s / 10000 << ", ";
    }
    for (int i = 0; i < 70; i++) {
        delete a[i];
    }
}