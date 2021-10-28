from multiprocessing.pool import ThreadPool
from threading import Thread
import random
import time
import keyboard
import sys

matrix1 = []
matrix2 = []
v = []
w = []


def matrix12(min, max):
    a = random.randint(min, max)
    b = a
    matrix1 = [[random.randint(0, 100) for i in range(b)] for i in range(a)]
    matrix2 = [[random.randint(0, 100) for i in range(a)] for i in range(b)]
    return matrix1, matrix2


def element(index, A, B):
    i, j = index
    res = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


def matrix3(matrix1, matrix2):
    s = 0
    c = 0
    for a in matrix1:
        s += 1
    for a1 in matrix2:
        c += 1
    matrix = [['' for k in range(c)] for k in range(s)]
    proc = s ** c
    pool = ThreadPool(processes=proc)
    for i1 in range(s):
        for j1 in range(c):
            matrix[i1][j1] = pool.apply_async(element, ((i1, j1), matrix1, matrix2)).get()
            if keyboard.is_pressed('ctrl'):
                print('Stopped')
                sys.exit()
    return matrix


def printing():
    while True:
        matrix1, matrix2 = matrix12(2, 5)
        print('matrix1:', matrix1)
        print('matrix2:', matrix2)
        matrix = matrix3(matrix1, matrix2)
        print('matrix:', matrix)
        time.sleep(5)
        print('_______________________')


if __name__ == '__main__':
    Thread(target=printing).start()
    input()
