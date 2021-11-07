from multiprocessing.pool import ThreadPool
from threading import Thread


matrix1 = open('mat1.txt', 'r') #открываем файлы
matrix2 = open('mat2.txt', 'r')

mat1_l = []
for l in matrix1:  # первая матрица
    l = l.split()
    for i in range(len(l)):
        l[i] = int(l[i])
    mat1_l.append(l)

mat2_l = []
for l in matrix2:  # вторая матрица
    l = l.split()
    for i in range(len(l)):
        l[i] = int(l[i])
    mat2_l.append(l)


def element(index, A, B):
    i,j=index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res

def matrix3(mat1, mat2): # третья матрица (перемножение)

    s = len(mat1)
    c = len(mat2)
    mat3 = [['' for k in range(c)] for k in range(s)]
    proc = s**c
    p = ThreadPool(processes=proc)
    for i1 in range(s):
        for j1 in range(c):
            mat3[i1][j1] = p.apply_async(element, ((i1, j1), mat1, mat2)).get()
    file = open("mat3.txt", "w")
    file.write(str(mat3))
    file.close()
    return mat3

def print_mat():  # вывод
    print('1 матрица: ', mat1_l)
    print('2 матрица: ', mat2_l)
    print('1*2: ',matrix3(mat1_l,mat2_l))

if __name__ == '__main__':
     Thread(target=print_mat).start()
