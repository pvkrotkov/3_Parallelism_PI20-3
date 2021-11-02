import random
import time
from multiprocessing import Process, Pool, Event
import keyboard


# определение элемента
def element(index, A, B, size):
    i, j = index
    res = 0
    for k in range(size):
        res += A[i][k] * B[k][j]
    return res


# установка размера матрицы
def set_size(size):
    return [[random.randint(-100, 100) for j in range(size)] for i in range(size)]


# запись матрицы c (почти) уникальным ID
def write_out(mat, name):
    for idents, item in enumerate(mat):
        with open(f'{name[0]}_{random.randint(1, 1000)}.txt', 'w') as file:
            file.write(f"Матрица {idents}:\n")
            for i in item:
                file.write(' '.join([str(j) for j in i]) + '\n')


# получение результата
def get_result(arr, size, pool):
    for i in range(size):
        for j in range(size):
            result = pool.apply_async(element, ((i, j), arr[0], arr[1], size))
            res_matrix = result.get()
            arr[2][i].append(res_matrix)
    return arr[2]


# основное вычисление c автоматическим выборо кол-ва процессов
def general_operations(size, ev_stop):
    while ev_stop.is_set():
        with Pool(processes=size * 2) as pool:
            array1, array2 = set_size(size), set_size(size)
            write_out([array1, array2], ['matrix_1', 'matrix_2'])
            array3 = [[] for i in range(size)]
            array3 = get_result([array1, array2, array3], size, pool)
            write_out([array3], ['matrix_3'])
            time.sleep(5)


# основная функция с остановкой процесса и заданием размера матрицы
def main():
    ev = Event()
    ev.set()
    size = int(input("Задайте размер матрицам: "))
    main_event = Process(target=general_operations, args=(size, ev))
    main_event.start()
    while keyboard.read_key() == "p":
        print("Exiting from program")
        break
    ev.clear()
    main_event.join()


if __name__ == '__main__':
    main()
