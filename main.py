from multiprocessing import Process, Pool
import csv
from random import randint


def multiply(args):
    i, j, = args[0] # индекс текущего элемента
    A, B = args[1:] # матрицы
    res = 0

    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    with open('temp_results.csv', 'a+') as temp_file: # файл с промежуточными результами
        writer = csv.writer(temp_file, delimiter=';')
        writer.writerow([res])

    return res


def generate_matrix(n, filename):
    matrix = [[randint(0,10) for i in range(n)] for j in range(n)]

    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=';')
        for row in matrix:
            writer.writerow(row)

    print(matrix)


def main():
    DIMENSION = ''
    while True:
        print('Введите ноль (0), чтобы прекратить генерацию и закончить вычисления. ')
        DIMENSION = int(input('Размерность матриц - одно число, большее единицы: '))
        if not DIMENSION:
            break

        #генерируем матрицы
        generate_matrix(DIMENSION, 'm1.csv')
        generate_matrix(DIMENSION, 'm2.csv')

        # чтение файлов с матрицами
        with open('m1.csv', 'r') as m1:
            m1_file = csv.reader(m1, delimiter=';')
            m1 = [ list(map(int, row)) for row in m1_file]
        with open('m2.csv', 'r') as m2:
            m2_file = csv.reader(m2, delimiter=';')
            m2 = [ list(map(int, row)) for row in m2_file]

        # определяем количество процессов с помощью размерностей матриц
        pool = Pool(processes=len(m1[0])*len(m2))
        # подготавливаем данные для передаче в распараллеленную функцию
        elements = [((i,j), m1, m2) for i in range(len(m1[0])) for j in range(len(m2))]
        # вычисляем значения и заносим результаты в список
        result = pool.map(multiply, elements)
        # из плоского списка делаем матрица нужного размера
        res_matrix = [result[i:i+len(m2)] for i in range(0, len(m1[0])*len(m2), len(m2))]
        print(res_matrix)

        # запись результирующей матрицы
        with open('res_matrix.csv', 'w') as res_file:
            writer = csv.writer(res_file, delimiter=';')
            for row in res_matrix:
                writer.writerow(row)


if __name__ == '__main__':
    main()
