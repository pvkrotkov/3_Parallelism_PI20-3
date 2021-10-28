from multiprocessing.pool import ThreadPool

matrix1 = []
matrix2 = []
v = []
w = []

with open("matrix_1.txt", "r") as mat1:
    for j in mat1:
        v = j.split()
        for i in range(len(v)):
            v[i] = int(v[i])
        matrix1.append(v)

with open("matrix_2.txt", "r") as mat2:
    for line1 in mat2:
        w = line1.split()
        for i in range(len(w)):
            w[i] = int(w[i])
        matrix2.append(w)


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
    file = open("matrix.txt", "w")
    file.write(str(matrix))
    file.close()
    return matrix


def printing():
    print('matrix1:', matrix1)
    print('matrix2:', matrix2)
    matrix = matrix3(matrix1, matrix2)
    print('matrix:', matrix)


if __name__ == '__main__':
    printing()
