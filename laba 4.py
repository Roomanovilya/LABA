# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
# B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
# Для отладки использовать не случайное заполнение, а целенаправленное.
# Вид матрицы А: 
# D  Е
# С  В
# Для простоты все индексы в подматрицах относительные. 
# По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
# Программа должна использовать функции библиотек numpy  и mathplotlib
# 19.Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество нулей в нечетных столбцах,
# умноженное на К больше, чем произведение чисел в нечетных строках,
# то поменять местами В и С симметрично, иначе В и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * F-1, иначе вычисляется выражение (A-1 +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А.
# Выводятся по мере формирования А, F и все матричные операции последовательно.

import numpy as np
import matplotlib.pyplot as plt

K=int(input("Введите К="))
N=int(input("Введите N="))
"""формирем матрицы размером N/2xN/2 с случайным заполнением от -10 до 10 """
D = np.array(np.random.randint (-10, 10, ((N//2), (N//2))))
E = np.array(np.random.randint (-10, 10, ((N//2), (N//2))))
C = np.array(np.random.randint (-10, 10, ((N//2), (N//2))))
B = np.array(np.random.randint (-10, 10, ((N//2), (N//2))))
A = np.hstack((np.vstack((D,C)),np.vstack((E,B))))
print('Матрица A \n ',A)
if ((np.count_nonzero(E[:,1::2]==0))*K)>(np.prod(E[1::2])):
    B=np.fliplr(B)
    C=np.fliplr(C)
    F = np.hstack((np.vstack((D,B)),np.vstack((E,C))))
    print('Матрица F \n ',F)
else:
    F = np.hstack((np.vstack((D,C)),np.vstack((B,E))))
    print('Матрица F \n ',F)
                   
if  np.linalg.det(A)>sum(np.fliplr(A).diagonal()+np.diagonal(A)):
    N=np.subtract((np.dot(A,np.transpose(A))),(np.dot(K,(np.linalg.inv(F)))))
    print('A*A^T – K * F^(-1) = ',N)
else:
    N=np.dot((np.subtract(np.linalg.inv(F)+np.tril(A),np.transpose(F))),K)
    print('(A^(-1) +G-F^(T))*K = ',N)

plt.title("Зависимости: y = tan от элементов F, x = arctan от элементов F")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(np.tan(F),np.arctan(F),linestyle="--",color="r",marker='o',markersize=7)
plt.show()

sr= np.mean(F, axis=0)
plt.title('Средние значения столбцов в матрице F')
plt.xlabel('Номер столбца')
plt.ylabel('Среднее значение')
plt.bar(range(len(sr)), sr)
plt.show()


c=[]
l=[]
for i in range(10):
    count=np.count_nonzero(F==i)
    c.append(count)
    l.append(f'Цифра {i}: {count}')
plt.title('Количество каждой цифры от 0 до 9 в матрице F')
plt.pie(c, labels=l, autopct='%1.1f%%')
plt.show()
