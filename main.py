from multiprocessing import Process,Pool, Manager
from random import randint

def forpotok(matrix1, matrix2, ind, All):
    res = All.an

    for  k in range(0, len(matrix2[0])):
        res[ind].append(element((ind, k), matrix1, matrix2))
    All.an = res


def check_matr(All):
    while All.lst_mat:
        procs = []
        lst = All.lst_mat
        matrix1, matrix2 = lst.pop()
        All.lst_mat = lst
        All.an = [[] for i in range(len(matrix1))]
        for i in range(0, len(matrix1)):
            proc = Process(target=forpotok, args=(matrix1, matrix2, i, All))
            procs.append(proc)
            proc.start()
        for proc in procs:
            proc.join()
        print(All.an)
        if All.com == "exit":
            break


def matrix_gen(All):
    while True:
        if All.com == "exit":
            break
        stro1 = randint(2, 5)
        stol1 = randint(2, 5)
        stro2 = randint(2, 5)
        stol2 = stro1
        matrix1 = [[randint(-5, 5) for i in range(stro1)] for i in range(stol1)]
        matrix2 = [[randint(-5, 5) for i in range(stro2)] for i in range(stol2)]
        lst = All.lst_mat
        lst.append((matrix1,matrix2))
        All.lst_mat = lst



def element(index, A, B):
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


if __name__ == '__main__':
    mn = Manager()
    All = mn.Namespace()
    All.lst_mat = []
    All.com = ''
    genproc =Process(target=matrix_gen, args=([All]))
    genproc.start()
    matproc =Process(target=check_matr, args=([All]))
    matproc.start()
    while All.com != "exit":
        All.com = input()
    matproc.join()
