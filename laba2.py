#Натуральные числа, содержащие не более одной группы из 3 подряд идущих 7. Список используемых в числах нечетных цифр выводить отдельно прописью
import re
d_db = {'1': 'один',  '3': 'три', '5': 'пять', '7': 'семь', '9': 'девять'}
h = 0

with open("text.txt") as file:
    buffer = file.read()
    if not buffer:
        print("\nФайл text.txt пустой.\nДобавьте непустой файл в директорию или переименуйте существующий файл.")
    buffer = re.findall(r"(?:^|\D)(?:\d*777\d*|\D*777\D*)(?:$|\D)", buffer)
    for i in buffer :
        h = 1
        odd_digits = '' 
        for digit in i: 
            if digit in '13579':
                odd_digits += digit
        print(i)
        if odd_digits:
            print('Нечетные цифры:', ', '.join([d_db[digit] for digit in odd_digits]))
        else:
            print('Нечетных цифр нет.')
if h == 0:
    print("В файле отсутствует группа из трёх подряд идущих цифр 7")
