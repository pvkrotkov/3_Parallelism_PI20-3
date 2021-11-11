from random import randint
from multiprocessing import Pool


def matrix_gen(matrix_size, max_value):
    matrix_a = [[randint(0, max_value) for j in range(matrix_size)] for i in range(matrix_size)]
    matrix_b = [[randint(0, max_value) for j in range(matrix_size)] for i in range(matrix_size)]
    return matrix_a, matrix_b


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()
    print()


def default_multiplication(a, b):
    ar, ac, br, bc = len(a), len(a[0]), len(b), len(b[0])
    p = Pool()
    s = 0
    t = []
    res = []
    for z in range(0, ar):
        for j in range(0, bc):
            for i in range(0, ac):
                s = calculate_element((i, j, z), a, b, s)
            t.append(s)
            s = 0
        res.append(t)
        t = []
    return res


def calculate_element(index, a, b, s):
    i, j, z = index
    s += a[z][i] * b[i][j]
    return s


def process_multiplication(x,y):
    rez = sum(i*k for i, k in zip(x, y))
    return rez


def reformat_matrix(matrix):
    outsize = int(len(matrix)**(1/2))
    outmatrix = []
    row = []
    for i, element in enumerate(matrix):
        row.append(element)
        if (i+1) % outsize == 0:
            outmatrix.append(row)
            row = []
    return outmatrix


def main():
    matrix_size = int(input("Введите размер матрицы: "))
    max_value = int(input("Введите максимальное значение элемента в матрицу: "))
    matrix_a, matrix_b = matrix_gen(matrix_size, max_value)
    print('Matrix A:')
    print_matrix(matrix_a)
    print('Matrix B:')
    print_matrix(matrix_b)
    with Pool(4) as pool:
        matrix = pool.starmap(process_multiplication, [(i, k)for i in matrix_a for k in matrix_b])
    print('Result:')
    print_matrix(reformat_matrix(matrix))


if __name__ == '__main__':
    main()
