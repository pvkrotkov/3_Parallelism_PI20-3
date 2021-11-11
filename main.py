from multiprocessing import Pool, cpu_count


def elem(m):
    res = 0
    m1, m2 = m
    for y in range(len(m1)):
        res += m1[y] * m2[y]
    return res
def read_matr(file_name):
    f = open(file_name, 'r')
    l = [line.strip().split('\t') for line in f]
    f.close()
    return l
def write_matr(ls, u, t):
    f = open('Matrixs_multiplication.txt', 'w')
    k = 0
    for i in range(u):
        if i != 0:
            f.write('\n')
        for j in range(t):
            f.write(f"{new_ls[k]}\t")
            k += 1


if __name__ == '__main__':
    A = read_matr('first_matrix.txt')
    B = read_matr('second_matrix.txt')
    res_matr = [[0 for j in range(len(B))] for i in range(len(A))]

    ls = []

    for i in range(len(A)):
        for j in range(len(B[1])):
            ls.append(([int(o) for o in A[i]], [int(k[j]) for k in B]))

    p = Pool(cpu_count())
    new_ls = p.map(elem, ls)
    k = 0
    write_matr(new_ls, len(res_matr), len(res_matr[0]))
    for i in range(len(res_matr)):
        for j in range(len(res_matr[i])):
            res_matr[i][j] = new_ls[k]
            k += 1
    print(res_matr)
