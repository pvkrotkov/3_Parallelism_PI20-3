from multiprocessing import Process, Pool
import csv
from random import *

'''
Program would generate random matrix the the size given by user and then create files for matrix1, matrix2 and result
'''

#function to generate matrix and write it in a file
def gen_matrix(n, name):
    res = [sample([x for x in range(1,100)], n) for _ in range(n)]

    with open(name, 'w') as f:
        writer = csv.writer(f, delimiter=';')
        for row in res:
            writer.writerow(row)

    print(res)

#function to multiply matrix
def multiply(args):
    i, j, = args[0] 
    A, B = args[1:] 
    res = 0

    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    
    return res

#function to take input from user and avoid negative input and strings
def take_input_length():
    flag = False
    while flag == False:
        try:
            inpt = int(input('Enter the length of your matrix: \n'))
        except:
            print('Wrong input')
        else:
            if inpt>0:
                flag = True
            else:
                print('Enter number greater than 0!')
    return inpt

#function that gets a name of the file and returns matrix from that file 
def open_matrix(name):
    with open(name, 'r') as f:
        file = csv.reader(f, delimiter=';')
        res = [ list(map(int, row)) for row in file]
    return res

def write_result(name, matrix):
    with open(name, 'w') as f:
        file = csv.writer(f, delimiter=';')
        for row in matrix:
            file.writerow(row)

def main():
    #take the length of matrix from user
    length = take_input_length()

    #generate two matrix
    gen_matrix(length, 'matrix1.csv')
    gen_matrix(length, 'matrix2.csv')

    #open two matrix
    matrix1 = open_matrix('matrix1.csv')
    matrix2 = open_matrix('matrix2.csv')

    #define the amount of precesses by the length of matrix
    proc_amount = Pool(processes=len(matrix1[0])*len(matrix2))

    #put all the numbers in matrix into one colomn of numbers
    elements = [((i,j), matrix1, matrix2) for i in range(len(matrix1[0])) for j in range(len(matrix2))]

    #multiply elements
    result = proc_amount.map(multiply, elements)

    #bring back one colomn into matrix
    result_matrix = [result[i:i+len(matrix2)] for i in range(0, len(matrix1[0])*len(matrix2), len(matrix2))]

    print(result_matrix)

    #write result matrix into a separate file
    write_result('result_matrix.csv', result_matrix)


if __name__ == '__main__':
    main()
