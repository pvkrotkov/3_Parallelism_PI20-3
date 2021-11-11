from multiprocessing import Pool

def element(index):
    global A
    global B
    i, j = index
    res = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res

def procLen(m1,m2) -> int:
    x = len(m1[0])
    y = len(m2)
    return x*y 
def matrix1() -> list:
    result = []
    with open("matrix1","r") as f:
        for i in f:
            result.append(list(map(int,i.split())))
    return result

def matrix2() -> list:
    result = []
    with open("matrix2","r") as f:
        for i in f:
            result.append(list(map(int,i.split())))
    return result

def writeToFile(result):
    open("result_matrix","w").close()
    with open("result_matrix","a") as f:
        for line in result:
            print(" ".join(str(x) for x in line), file=f)
        
        
A = matrix1()
B = matrix2()
print(A)
print(B)
pool = Pool(processes=procLen(A,B))

k = pool.map(element, [(i,j) for i in range(len(A[0])) for j in range(len(B))])
result = []
for i in range(len(A[0])):
    result.append([])
    for j in range(len(B)):
        result[-1].append(k[0])
        k.remove(k[0])

writeToFile(result)
