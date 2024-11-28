with open('vvod.txt', '+r') as file:
    s = file.readlines()
    #n - как в 8 кол-во строк
    n = len(s)

    a = []
    for i in range(n):
        #если это не последняя строка, то срезаем \n
        if i != n - 1:
            b = []
            b.extend(s[i][:-1])
            a.append(b)
        #если это последняя строка, то вставляем целиком
        else:
            b = []
            b.extend(s[i])
            a.append(b)

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

with open('vivod.txt', '+w') as vivod:
    for i in range(len(a2)):
        row = ''.join(a2[i])
        vivod.write(row + '\n')