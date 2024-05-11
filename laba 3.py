# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
# состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
# Для тестирования использовать не случайное заполнение, а целенаправленное.
# вид матрицы А
# D Е
# С В
# Каждая из матриц B,C,D,E имеет вид
#   4
#  3 1
#   2
# 19.Формируется матрица F следующим образом: если в Е количество нулей в нечетных столбцах в области 4, умноженное на К больше,
# чем произведение чисел в нечетных строках в области 1,
# то поменять в С симметрично области 1 и 2 местами, иначе В и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего вычисляется выражение: A*F+ K* F T .
# Выводятся по мере формирования А, F и все матричные операции последовательно.

import random

k = int(input('Введите k = '))
n = int(input('Введите n = '))

# Функция для быстрого вывода любой матрицы
def print_matrix(mtr, mtr_name, size):
    print('Матрица ', mtr_name, ': \n')
    for i in range(size):
        for j in range(size):
            print('{:>3d}'.format(mtr[i][j]), end='  ')
        print()
    print()

# матрица A
A=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(random.randint(-10, 10))
    A.append(a)
print_matrix(A, 'A', n)

n2=n//2
n3=n//2
n4=n
if n%2!=0:
    n3=n//2+1
    n4=n-1
# матрица F
F = [[0] * n4 for _ in range(n4)]
# подматрица D   
D = []
for i in range(n2):          
    d = []
    for j in range(n2):
        d.append(int(A[i][j]))
    D.append(d)
    
print_matrix(D, 'D', n2)
# подматрица E 
E = []
for i in range(n2):
    e = []
    for j in range(n3, n):
        e.append(int(A[i][j]))
    E.append(e)
print_matrix(E, 'E', n2)
# подматрица C 
C=[]
for i in range(n3, n):
    c=[]
    for j in range(n2):
        c.append(int(A[i][j]))
    C.append(c)
print_matrix(C, 'C', n2)
# подматрица B
B = []
for i in range(n3, n):
    b = []
    for j in range(n3, n):
        b.append(int(A[i][j]))
    B.append(b)
print_matrix(B, 'B', n2)

s=[] 
S=[]
for i in range(n2 // 2):
    for j in range(i+1,n2 - 1 - i):
        s.append(E[i][j])
        if j % 2 == 0:
            S.append(E[i][j])        
s1=0 
for i in S:
    if i==0:
        s1+=1
print('количество нулей в нечетных столбцах E в области 4, умноженное на К: ', s1 * k)

q = []
Q = []
for j in range(n2-1,(n2//2),-1):
    for i in range(n2-j,n2-(n2-j)):
        q.append(E[i][j])
        if i%2==0:
            Q.append(E[i][j])
w = 1
for i in Q:
    w *= i
print('произведение чисел в нечетных строках E в области 1: ', w)

# cимметрично измененняем области 1 и 2 подматрицы С 
if (s1*k)>w:
    c2=C.copy()
    for i in range(n2//2,n2):
        for j in range(n2-i,i):
            c2[i][j], c2[j][i]=c2[j][i],  c2[i][j]                                 
    print('cимметрично измененняем области 1 и 2 подматрицы С')
    print_matrix(c2, "C", n2)
    for i in range(n2):
        for j in range(n2):
            F[i][j] = D[i][j]
    for i in range(n2, n4):
        for j in range(n2):
            F[i][j] = c2[i - n2][j - n2]
    for i in range(n2,n4):
        for j in range(n2,n4):
            F[i][j] = B[i - n2][j - n2]
    for i in range(n2):
        for j in range(n2, n4):
            F[i][j] = E[i][j - n2]
    print_matrix(F, "F", n4)
# несимметрично меняем местами подматрицы B и E
else:
    print('несимметрично меняем местами подматрицы B и E')
    for i in range(n2,n4):
        for j in range(n2,n4):
            F[i][j] = E[i - n2][j - n2]
    for i in range(n2):
        for j in range(n2):
            F[i][j] = D[i][j]
    for i in range(n2, n4):
        for j in range(n2):
            F[i][j] = C[i-n2][j]
    for i in range(n2):
        for j in range(n2, n4):
            F[i][j] = B[i][j - n2]
    print_matrix(F, "F", n4)
       
A_F = [[0] * n for _ in range(n4)]
K_FT = [[0] * n for _ in range(n4)]
m = [[0] * n for _ in range(n4)]
for i in range(n4):
    for j in range(n4):
        A_F[i][j] = A[i][j] * F[i][j]
for i in range(n4):
    for j in range(n4):
        K_FT[i][j] = k * F[j][i]
for i in range(n4):
    for j in range(n4):
        m[i][j] = A_F[i][j] + K_FT[i][j]
        
def print_supermatrix(mtr, mtr_name, size):
    print('Матрица ', mtr_name, ': \n')
    for i in range(size):
        for j in range(size):
            print('{:>5d}'.format(mtr[i][j]), end='  ')
        print()
    print()

print_supermatrix(m, ' A*F+ K* F T = ', n4)

