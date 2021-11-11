from multiprocessing import Process, Pool
import random


def creating(n):
	return [random.randint(1,10) for i in range(n)]


def element(lst1, lst2, number, index):
	n = len(lst1[0]) or len(lst2)
	value = 0
	for i in range(n):
		value += lst1[number][i] * lst2[i][index]
	return value


def final(lst1, lst2):
	n = len(lst1)
	obr = []
	for i in range(n):
		for j in range(n):
			obr.append([i,j])
	obr = [[lst1, lst2, i[0], i[1]] for i in obr]
	pool = Pool(len(obr))
	otv = pool.starmap(element, obr)
	lst = []
	main = []
	k = 0
	for i in otv:
		k += 1
		if k%n != 0:
			lst.append(i)
		else:
			lst.append(i)
			main.append(lst)
			lst = []
	print(' A * B = ',main)
	mat3 = open('mat3.txt', 'w')
	for i in main:
		mat3.write(' '.join([str(j) for j in i])+'\n')
	mat3.close()
	choose()


def start():
	if __name__ == "__main__":
		try:
			n = int(input('Введите размерность квадратной матрицы: '))
			osn1 = [[n] for i in range(n)]
			osn2 = [[n] for i in range(n)]
			pool = Pool(2)
			mat1 = pool.starmap(creating, osn1)
			mat2 = pool.starmap(creating, osn2)
			print(' Матрица A:\n',mat1)
			print(' Матрица B:\n',mat2)
			print()
			final(mat1, mat2)
		except ValueError:
			print('Неправильный ввод')

def read_mat():
	try:
		mat1 = open('mat1.txt', 'r')
		mat2 = open('mat2.txt', 'r')
	except:
		choice = input('Матриц нет, создать? (д/н)')
		if choice == '1' or choice == 'д' or choice == 'Д' or choice == 'l' or choice == 'L':
			mat1 = open('mat1.txt', 'w')
			mat2 = open('mat2.txt', 'w')
			mat1.write('1 2 3\n4 5 6\n7 8 9')
			mat2.write('7 8 9\n10 11 12\n13 14 15')
			mat1.close()
			mat2.close()
			mat1 = open('mat1.txt', 'r')
			mat2 = open('mat2.txt', 'r')
		else:
			choose()
	lst1 = []
	for i in mat1:
		lst = []
		for j in i.split(' '):
			lst.append(int(j))
		lst1.append(lst)
	lst2 = []
	for i in mat2:
		lst = []
		for j in i.split(' '):
			lst.append(int(j))
		lst2.append(lst)
	print(' Матрица A:\n',lst1)
	print(' Матрица B:\n',lst2)
	print()
	final(lst1, lst2)
	

def choose():
	print('ПЕРЕМНОЖЕНИЕ МАТРИЦ\n')
	choice = input('1 - Загрузка матриц\n2 - генерация матриц\n3 - выход\n')
	if choice == '2':
		start()
	elif choice == '1':
		read_mat()
	elif choice == '3':
		pass
	else:
		print('Выберите что-то')
		choose()

choose()
