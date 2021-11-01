from multiprocessing import Process, Pipe

def times(line, column, send_end): #calculating matrix element
    res = 0
    for i in range(len(line)):
        res += line[i] * column[i]
    send_end.send(res) #sending to output list

if __name__ == '__main__':
    with open('matrix1.txt', 'r') as f:
        matrix1 = [[int(num) for num in line.split(',')] for line in f]  #read matrix 1
    with open('matrix2.txt', 'r') as f:
        matrix2 = [[int(num) for num in line.split(',')] for line in f] #read matrix 2
    if len(matrix1[0]) != len(matrix2): #checking the possibility of matrix multiplication
        print("matrix multiplication is not possible, because column length of matrix 1 is not equal to the number of columns of matrix 2")
        raise SystemExit
        
    rows = [[] for i in matrix2[0]]
    [rows[i].append(j[i]) for i in range(len(rows)) for j in matrix2] #change matrix 2 elements to rows
    pipe_list = [] #creaate output list
    for line in matrix1: #start process for each element of the matrix
        for column in rows:
            recv_end, send_end = Pipe(False)
            proc = Process(target=times, args=([line, column, send_end])) #the process itself
            pipe_list.append(recv_end) #append "res" from function to output list
            proc.start()
            proc.join()
    result_list = [x.recv() for x in pipe_list] #decrypt output list
    result_list = [result_list[i:i+len(matrix2[0])] for i in range(0, len(result_list), len(matrix2[0]))] #creating matrix type list
    with open('output.txt', 'w') as testfile:
        for row in result_list:
            testfile.write(', '.join([str(a) for a in row]) + '\n') #creating file with output
    print('you can check result in output.txt')











#print(rows)
