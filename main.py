from multiprocessing import Process, Pool, Queue, Lock, Value
import random
import time


# Функция получения произведения элемента -строки ии столбца
def el(index, matrix1, matrix2):
    i, j = index
    result = 0
    n = len(matrix1[0]) or len(matrix2)
    for k in range(n):
        result = result + matrix1[i][k] * matrix2[k][j]
    return result


# Функция чтения матрицы из файла в список списков, в формате float
def r_m(filename):
    # открываем файл на чтение
    try:
        with open(filename, "r") as matrix_file:
            matrix = []
            for line in matrix_file.readlines():
                matrix.append([float(el) for el in line.split()])
    except:
        matrix = []
    return matrix


# Функция для записи самой матрицы в файл
def w_m(filename, matrix):
    with open(filename, "w") as matrix_file:
        matrix = "\r".join([' '.join(row) for row in [[str(element) for element in row] for row in matrix]])
        matrix_file.write(matrix)
    return


# Функция для записи элемента (по его индексу ) в файл с матрицей
def w_e(filename, index, value, lock):
    i, j = index
    with lock:
        matrix = r_m(filename)
        if len(matrix) <= i:
            for m in range(i - len(matrix) + 1):
                matrix.append([])
        if len(matrix[i]) <= j:
            for m in range(j - len(matrix[i]) + 1):
                matrix[i].append(0)
        matrix[i][j] = value
        w_m(filename, matrix)
    return


# Функция для вычисления конкретного текущего элемента и его последующая запись в файл
def rewrite(args):
    filename, index, matrix1, matrix2 = args
    value = el(index, matrix1, matrix2)
    w_e(filename, index, value, lock)
    return value


# Теперь нужно создать функцию, с помощью которой будем осуществлять pool процессов
def create_arguments(filename, matrix1, matrix2):
    indexes = []
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            indexes.append([filename, (i, j), matrix1, matrix2])
    return indexes


# Сгенерируем рандомную целочисленную матрицу
def gener_matrix(size, start, end):
    return [[random.randint(start, end) for m in range(size)] for m in range(size)]


# запишем матрицу в файл
def queue_creating(que, matrix_size=2, start=0, end=5):
    while True:
        matrix = gener_matrix(matrix_size, start, end)
        filename = f"first matrix{time.time()}.txt"
        w_m(filename, matrix)
        que.put(filename)
        # Задержка во времени между новой записью в файл составляет 5 секунд
        time.sleep(5)


def init(l):
    global lock
    lock = l


def matrix_multiplier(que, run):
    while True:
        if run.value:
            matrix1 = r_m(que.get())
            matrix2 = r_m(que.get())
            filename = f"second matrix{time.time()}.txt"
            indexes = create_arguments(filename, matrix1, matrix2)

            l = Lock()
            proc_count = len(matrix1) + len(matrix2[0])
            pool = Pool(processes=proc_count, initializer=init, initargs=(l,))

            pool.map(rewrite, indexes)
            pool.close()
            pool.join()
            que.put(filename)
        


if __name__ == '__main__':
    matrix_q = Queue()
    run = Value('i', 1)
    queue_process = Process(target=queue_creating, args=[matrix_q])
    queue_process.start()
    multiplier_process = Process(target=matrix_multiplier, args=[matrix_q, run])
    multiplier_process.start()
    proc_list = [queue_process, multiplier_process]

    print("остановить: приостановить генерацию файлов\выйти: завершить выполнение программы")
    while True:
        command = input()
        if command == "остановить":
            run.value = not run.value
        elif command == "выйти":
            for proc in proc_list:
                proc.terminate()
            break
        else:
            pass