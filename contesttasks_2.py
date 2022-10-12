
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



def task_7(a):
    return a[0]

with open("input.txt", "r", encoding='utf-8') as f:
    b = f.readlines()
    ar = [i.split() for i in b]

    ars = sorted(ar, key = g)
    maxb = ars[0][3]
    i = 0
    b = maxb
    sets = set()
    while b == maxb:
        sets = sets.union({ars[i][2]}, sets)
        i += 1
        if i < len(ars):
            b = ars[i][3]
        else:
            break
    print(*sets)
    
    
def task_8(a):
    return a[0]
with open("input.txt", "r", encoding='utf-8') as f:
    b = f.readlines()
    ar = [i.split() for i in b]

    ars = sorted(ar, key = g)
    for i in ars:

        print(*(i[:2] + i[3:4]))
        

with open("input.txt", "r", encoding='utf-8') as f:
    b = f.readlines()
    a = [i.split() for i in b]
    ar = [[], [], []]
    for i in a:
        ar[int(i[2]) - 9].append(i)
    sb9 = sum(int(ar[0][i][3]) for i in range(len(ar[0]))) / len(ar[0])
    sb10 = sum(int(ar[1][i][3]) for i in range(len(ar[1]))) / len(ar[1])
    sb11 = sum(int(ar[2][i][3]) for i in range(len(ar[2]))) / len(ar[2])
    print(sb9, sb10, sb11)



