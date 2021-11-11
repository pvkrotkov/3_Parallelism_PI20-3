from multiprocessing import Pool #Импорт библиотеки для работы с пулом процессов

def write(mat): #Запись в матрицу
    global g
    b = 0
    qq = len(mat)
    fi = open('result.txt', 'a')
    for q in range(qq):
        b += 1
        if b != g:
            fi.write(str(mat[q]) + " ")
        else:
            fi.write(str(mat[q]) + "\n")
            b = 0

def multiplication(x, y):  #Умножение матриц
    rez = sum(i * k for i, k in zip(x, y))
    return rez

if __name__ == '__main__':
    res = 0
    m1 = open('matrix1.txt', 'r')
    matrix1 = []
    for line in m1.readlines():
        cut = line.find('\n')
        if cut != -1:
            c = line[:cut]
            l = c.split(' ')
            result = [int(item) for item in l]
            matrix1.append(result)
        else:
            a = line.split(' ')
            result = [int(item) for item in a]
            matrix1.append(result)
    m1.close()
    m1 = open('matrix1.txt', 'r')
    line_1 = len(m1.readline().split(' ')) #записываем число столбцов первой матрицы
    m1.close()
    m2 = open('matrix2.txt', 'r')
    matrix2 = []
    for line in m2.readlines():
        cut = line.find('\n')
        if cut != -1:
            c = line[:cut]
            l = c.split(' ')
            result = [int(item) for item in l]
            matrix2.append(result)
        else:
            li = line.split(' ')
            result = [int(item) for item in li]
            matrix2.append(result)
    m2.close()
    m2 = open('matrix2.txt', 'r')
    line_2 = len(m2.readline().split(' ')) #записываем число столбцов второй матрицы
    m2.close()
    g = len(matrix1)
    print ('\nA = ', matrix1, len(matrix1), line_1)
    print ('B = ', matrix2, len(matrix2), line_2)
    f = open('result.txt', 'w')
    f.write('')
    with Pool(4) as pool:
        matric = pool.starmap(multiplication, [(i, k) for i in matrix1 for k in zip(*matrix2)])
        write(matric)
