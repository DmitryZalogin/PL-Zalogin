n = int(input('Введите к-во строк:'))

#цикл по вводу матрицы
a = []
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

#проверка суммы для строк
row = sum(a[0])
answer_row = ''
for i in range(1, n):
    if sum(a[i]) == row:
        answer_row = 'True'
    else:
        answer_row = 'False'
        break

#пробелы между матрицами
print()

#перебирает введенную матрицу и делает матрицу а1, где строки меняются местами с колонами
a1 = []
for i in range(n):
    b1 = []
    for j in range(n):
        b1.append(a[j][i])
    a1.append(b1)

#вывод матрицы а1
for i in range(n):
    for j in range(n):
        print(a1[i][j], end='')
    print()

#проверка матрицы a1
column = sum(a1[0])
answer_col = ''
for i in range(1, n):
    if sum(a1[i]) == row:
        answer_col = 'True'
    else:
        answer_col = 'False'
        break

#проверка итоговая колоны + строки
if answer_row == 'True' and answer_col == 'True':
    print('Магическая')
else:
    print('Не магическая')