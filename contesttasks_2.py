
def task_1(m, n):
    a = [[5 * i + j for j in range(m)] for i in range(n)]
    print(a)

def task_2(n, m):
    a = [[*[2 for i in range(j)], *[0], *[1 for i in range(m - j - 1)]] for j in range(n)]
    print(a)

def task_3(n):
    a = [[*[j for i in range(j + 1)], *[i for i in range(j+1, n)]] for j in range(n)]
    print(a)


def task_4():
    with open('task_4.txt') as f:
        a = list(f)
        a = list(map(lambda x: x.rstrip(), a))
        a = a[::-1]
        print(*a, sep='\n')


def task_5():
    with open('task_4.txt') as f:
        a = list(f)
        a = list(map(lambda x: x.rstrip(), a))
        a = a[::-1]
        b = []
        for i in a:
            i = i[::-1]
            b.append(i)
        print(*b, sep='\n')



def task_6():
    with open('task_6.txt', encoding='UTF-8') as f:
        a = list(f)
        print(a)
        a = list(map(lambda x: x.rstrip(), a))
        print(a)
task_6()



