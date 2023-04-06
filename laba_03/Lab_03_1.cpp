#include <iostream>
#include <random>
#include <stdlib.h>
#include <time.h>
using namespace std;

std::default_random_engine rng((int)time(0));

struct Node
{
    int x;
    int y;
};

int Sluch_4() {
    int arr[] = {1, 2, 3, 4};
    // std::default_random_engine rng(i + 41 * (int)time(0));
    std::uniform_int_distribution<unsigned> dstr(0, 3);
    int x = arr[dstr(rng)];
    for (unsigned counter = 1; counter != 0; --counter)
        return arr[dstr(rng)];
    return 0;
}

int random_4() {
    srand(time(NULL));
    int x;
    x = (int)time(0);
    // cout << x << " ";
    return x % 4 + 1;
}

Node *random_vector(int x, int y) {
    Node *v = new Node;
    srand(time(NULL));
    v->x = Sluch_4() % x + 1;
    v->y = Sluch_4() % y + 1;
    return v;
}

void print_vector(Node *v) { cout << v->x << " " << v->y << endl; }

void moving(Node *v, int x, int y) {
    int m = Sluch_4();
    if (m == 1) {
        v->x = (v->x - 1);
    }
    if (m == 2) {
        v->x = (v->x + 1);
    }
    if (m == 3) {
        v->y = (v->y - 1);
    }
    if (m == 4) {
        v->y = (v->y + 1);
    }
    // cout << endl;
}

int carrot(Node *v, int x, int y) {
    int w = 0;
    while (v->x != 1 and v->x != x and v->y != 1 and v->y != y) {
        w++;
        moving(v, x, y);
    }
    return w;
}

int main() {
    int x;
    int y;
    // cin >> x;
    // cin >> y;
    int n = 100;
    // s = random_4();
    Node *v = new Node;
    v->x = x / 2;
    v->y = y / 2;
    // v = random_vector(x, y);
    // print_vector(v);
    for (int i = 4; i < 200; i++) {
        int s = 0;
        x = i;
        y = i;
        for (int j = 0; j < n; j++) {
            // cout << carrot(v, x, y) << ", ";
            s += carrot(v, x, y);
            v->x = x / 2;
            v->y = y / 2;
        }
        cout << s / n << ", ";
    }
}