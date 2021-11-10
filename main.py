from multiprocessing import Process,Pool

def get_data_from_f(file):# считывание данных с файла
    with open(file, 'r', newline='\n') as f:
        rows = [row for row in f.readlines()]
        rows = [row.rstrip().split(',') for row in rows]
    try:
        for row in range(len(rows)):
            for el in range(len(rows[row])):
                rows[row][el] = int(rows[row][el]) # конвертирование чисел-символов в числа integer
        return rows
    except:
        print('Неверный тип данных! Введите только числа через запятую без пробелов.')

def element(index, A, B): # перемножение матриц
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    with open('/Users/yaseminhertek/VS_code/3_Parallelism_PI20-3/raw_results.txt', 'a') as f:
        f.write(str(res)+' ')

    return res

def result_mat(m1,m2): # запись полученных результатов в матрицу
    global N
    #создаем результирующую матрицу с необходимой размерностью
    resmat = [['*' for col in range(len(m2[0]))] for row in range(len(m1))]
    
    #вычисляем значения с помощью функции и записываем в результирующую матрицу
    proc = Pool(processes=N)
    for row in range(len(m1)):
        for col in range(len(m2)):
            resmat[row][col]=proc.apply_async(element, ((row,col), m1, m2)).get()
    
    # записываем результирующую матрицу (все элементы строковые) в файл
    strresmat = [[str(resmat[i][j]) for j in range(len(resmat[i]))] for i in range(len(resmat))]
    f = open('/Users/yaseminhertek/VS_code/3_Parallelism_PI20-3/resmat.txt', 'w')
    for i in range(len(strresmat)):
        f.write(','.join(strresmat[i])+'\n')
    f.close()
    
    return resmat

#значения для работы в консоли
#matrix1 = [[1, 2], [3, 4]]
#matrix2 = [[2, 0], [1, 2]]

matrix1 = get_data_from_f('/Users/yaseminhertek/VS_code/3_Parallelism_PI20-3/mat1.txt')
matrix2 = get_data_from_f('/Users/yaseminhertek/VS_code/3_Parallelism_PI20-3/mat2.txt')

N = len(matrix1)*len(matrix2[0])
# необходимо в многопроцессорных программах
if __name__=='__main__':
    # для вывода ответа на консоль
    #print(result_mat(matrix1,matrix2))
    result_mat(matrix1,matrix2)