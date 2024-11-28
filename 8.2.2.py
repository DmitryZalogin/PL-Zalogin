n = int(input('Введите к-во столбцов:'))
a = []

#цикл по вводу матрицы
for i in range(n):
    b = []
    for i1 in range(n):
        b.append(int(input('Введите число:')))
    a.append(b)

#вывод матрицы а
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()

#перебирает введенную матрицу и делает матрицу а1, где строки меняются местами с колонами
a1 = []
for i in range(n):
    b1 = []
    for j in range(n):
        b1.append(a[j][i])
    a1.append(b1)

#замена столбцов
first = a1[0]
last = a1[-1]

a1[0] = last
a1[-1] = first

#обратная замена колон на строки
a2 = []
for i in range(n):
    b2 = []
    for j in range(n):
        b2.append(a1[j][i])
    a2.append(b2)

#пробелы между матрицами
print()

#вывод матрицы а2
for i in range(n):
    for j in range(n):
        print(a2[i][j], end='')
    print()
