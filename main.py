from multiprocessing import Process, Pipe, Event
import random
import time
import keyboard # using module keyboard

def times(line, column, send_end): #calculating matrix element
    res = 0
    for i in range(len(line)):
        res += line[i] * column[i]
    send_end.send(res) #sending to output list

def stop(event): #if button q is pressed
    while True:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            event.set()
            break

def matrix_gen(k): #generating matrix
    rows = [[] for i in range(k)]
    for row in rows:
        [row.append(random.randint(1, 100)) for i in range(k)]
    return rows

def multiplier(base): #function that multiplies generated matrixes
    matrix_base = base
    while True:
        matrix_new = matrix_gen(len(matrix_base[0]))
        rows = [[] for i in matrix_new[0]]
        [rows[i].append(j[i]) for i in range(len(rows)) for j in matrix_new]
        pipe_list = []

        for line in matrix_base: #start different process for each element of the matrix
            for column in rows:
                recv_end, send_end = Pipe(False)
                proc = Process(target=times, args=([line, column, send_end])) #the process itself
                proc.daemon = True
                pipe_list.append(recv_end) #append "res" from function to output list
                proc.start()

        output = [x.recv() for x in pipe_list] #decrypt output list
        output = [output[i:i+len(matrix_new[0])] for i in range(0, len(output), len(matrix_new[0]))] #creating matrix type list

        matrix_base = output # set matrix base for next iteration
        print('\n========================= matrix multiplication result =========================\n')
        s = [[str(e) for e in row] for row in output] #output matrix
        lens = [max(map(len, col)) for col in zip(*s)] #output matrix
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens) #output matrix
        table = [fmt.format(*row) for row in s] #output matrix
        print ('\n'.join(table)) #output matrix
        print('\ncreating and multiplying a new matrix ... ') #informing user that programm is still running
        print('\n PRESS "q" FOR QUIT\n')
        time.sleep(2)


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
    print('you can check matrix1 * matrix2 result in output.txt')
    size = input('set matrix size (for example: "3") - ')
    gener = matrix_gen(int(size)) #set matrix size
    print('Now we are going to generate and multiply matrix.\nIf you want to quit press "q" key')
    jobs = []
    events = Event()
    main_proc = Process(target=multiplier, args=[gener])
    jobs.append(main_proc)
    main_proc.start()
    stop(events) #call a function that waits for a button "q" to be pressed
    if events.is_set(): #exit programm if q is pressed
            print("\nexit from program")
            [i.terminate() for i in jobs]
            raise SystemExit
