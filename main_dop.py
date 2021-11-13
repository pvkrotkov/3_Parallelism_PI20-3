from multiprocessing.pool import ThreadPool
from threading import Thread
import random

mat1 = []
mat2 = []

#генерирует матрицы
def mat12(min, max):
    a = random.randint(min, max)
    b = a
    mat1 = [[random.randint(0, 100) for i in range(b)] for i in range(a)]
    mat2 = [[random.randint(0, 100) for i in range(a)] for i in range(b)]
    return mat1, mat2


def element(index, A, B):
    i, j = index
    res = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res

#третья матрица (перемножение)
def mat3(mat1, mat2):
    s = 0
    c = 0
    s=len(mat1)
    c=len(mat2)
    matrix = [['' for k in range(c)] for k in range(s)]
    proc = s ** c
    pool = ThreadPool(processes=proc)
    for i1 in range(s):
        for j1 in range(c):
            matrix[i1][j1] = pool.apply_async(element, ((i1, j1), mat1, mat2)).get()
    return matrix

#вывод
def print_mat():
    while True:
        try:
            mat1, mat2 = mat12(2, 6)
            print('matrix1:', mat1)
            print('matrix2:', mat2)
            matrix = mat3(mat1, mat2)
            print('matrix:', matrix)
            print('_______________________')
            test = input("Нажмите Command+D, если хотите остановить программу, иначе введите что угодно, чтобы продолжить")
            #при нажатие Command+D останавливает
        except EOFError:
            print("stop")
            break

if __name__ == '__main__':
    Thread(target=print_mat).start()
    
