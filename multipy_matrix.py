#import modules
from multiprocessing import Process, Pool

#opening matrixes
matrix1 = open('matrix1.txt', 'r')
matrix2 = open('matrix2.txt', 'r')

#reading matrix1
matrix1_list = []
for line in matrix1:
    line = line.split()
    matrix1_list.append(line)

#reading matrix2
matrix2_list = []
for line in matrix2:
    line = line.split()
    matrix2_list.append(line)

#Multipy function(for one string)
#In result we get 1 string of new matrix
def multipy_matrix(string_number):
    new_file = open('matrix3.txt', 'a')
    matrix3_list = []
    column = -1
    for j in range(len(matrix1_list)):
        column = column + 1
        new_element = 0
        for i in range(len(matrix1_list[string_number])):
            a = int(matrix1_list[string_number][i])*int(matrix2_list[i][column])
            new_element = new_element + a
        #writing in the file right after computation
        new_file.write(str(new_element))
        new_file.write(' ')
        matrix3_list.append(new_element)
    new_file.write('\n')
    new_file.close()

    return matrix3_list


if __name__=='__main__':

    strings = []
    for i in range(len(matrix1_list[0])):
        strings.append(i)

    #making pool
    try:
        p = Pool()
        result = p.map(multipy_matrix, strings)
        p.close()
        p.join()
        
    #print
        print('Конечная матрица:')
        print(result)
    except:
        pass


