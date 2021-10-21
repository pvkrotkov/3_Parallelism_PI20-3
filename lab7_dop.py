import multiprocessing as mp
import random
import sys
import time

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


def matrix12():
    global matrix2, matrix1
    matrix2 = []
    matrix1 = []
    z1 = []
    z2 = []
    zn = int(input('Количество строк и столбцов для двух матриц: '))
    for i in range(zn):
        for j in range(zn):
            z1.append(random.randint(0, 10))
            z2.append(random.randint(0, 10))
        matrix1.append(z1)
        matrix2.append(z2)
        z1 = []
        z2 = []


def pr():
    manager = mp.Manager()
    a = []
    matrix12()
    print('Первая матрица: ', matrix1)
    print('Вторая матрица: ', matrix2)
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
        try:
            time.sleep(1)
        except:
            print('Процесс остановлен')
            sys.exit()
    for p in a:
        p.join()
    print(matrix3)


if __name__ == "__main__":
    pr()
