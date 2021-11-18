from multiprocessing import Process, Pool
import csv
from random import randint


def display(matrix):
    max_len = 0
    matrix = [x for x in matrix if x]
    for row in matrix:
        len_list = list(map(str, row))
        max_len_local = len(max(len_list, key=len))
        if max_len_local > max_len:
            max_len = max_len_local
    print('-'*((max_len+1)*len(matrix[0])+1))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('|', end='')
            print(str(matrix[i][j]).center(max_len), end='')
        print('|')
        print('-'*((max_len+1)*len(matrix[0])+1))


def read_matrix(path):
    with open(path, 'r') as matrix_csv:
        matrix = list(csv.reader(matrix_csv, delimiter=';'))
        matrix_list = list(map(lambda row: list(map(float, row)), matrix))
    return matrix_list


def element(element):
    index = element[0]
    A = element[1]
    B = element[2]
    i, j = index
    res = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        num = round(A[i][k] * B[k][j], 2)
        res += num
    return res


def gen_matrix(n, k):
    matrix = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]

    with open("matrix_"+str(k)+".csv", 'w') as matrix_csv:
        writer = csv.writer(matrix_csv, delimiter=';')
        for row in matrix:
            writer.writerow(row)
    return matrix

def main():
    while True:
        try:
            user_input = int(input("Введите 0, чтобы выйти.\nВведите размер матриц: "))
            if (user_input == 0):
                break
        except ValueError:
            print("Введите число")
            continue
        else:
            matrix_1 = gen_matrix(user_input, 1)
            matrix_2 = gen_matrix(user_input, 2)
            num_of_processes = Pool(processes=len(matrix_1)*len(matrix_2[0]))
            elements = [[[i, j], matrix_1, matrix_2] for i in range(len(matrix_1)) for j in range(len(matrix_2[0]))]
            result = num_of_processes.map(element, elements)

            with open('result.csv', 'w') as res:
                writer = csv.writer(res, delimiter=';')
                for row in range(0, len(result), len(matrix_2[0])):
                    writer.writerow(result[row:row + len(matrix_2[0])])

            matrix = read_matrix("result.csv")
            print('Матрица 1')
            display(matrix_1)
            print('Матрица 2')
            display(matrix_2)
            print('Результат')
            display(matrix)


if __name__ == '__main__':
    main()