import multiprocessing as mp


def element(index, A, B, que):
    i, j = index
    res = 0
    matrix4 = [0, 0, 0]
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    matrix4[0] = i
    matrix4[1] = j
    matrix4[2] = res
    que.put(matrix4)


def matrix1():
    global matrix1
    matrix1 = []
    a1 = []
    with open("matrix1.txt", "r") as file:
        for line in file:
            a1 = line.split()
            for i in range(len(a1)):
                a1[i] = int(a1[i])
            matrix1.append(a1)


def matrix2():
    global matrix2
    matrix2 = []
    a1 = []
    with open("matrix2.txt", "r") as file:
        for line in file:
            a1 = line.split()
            for i in range(len(a1)):
                a1[i] = int(a1[i])
            matrix2.append(a1)



def pr():
    manager = mp.Manager()
    a = []
    matrix1()
    matrix2()
    matrix3 = []
    z = []
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            z.append(0)
        matrix3.append(z)
        z = []
    que = manager.Queue()
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            p = mp.Process(target=element, args=((i, j), matrix1, matrix2, que))
            a.append(p)
    for p in a:
        p.start()
        r = que.get()
        matrix3[r[0]][r[1]] = r[2]
    for p in a:
        p.join()
    print(matrix3)
    with open("matrix3.txt", "w") as file:
        for i in range(len(matrix3)):
            for j in range(len(matrix3[i])):
                file.write(str(matrix3[i][j]))
                file.write(' ')
            file.write('\n')


if __name__ == "__main__":
    pr()
