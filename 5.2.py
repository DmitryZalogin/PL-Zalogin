from itertools import count

text = input("Введите строку: ")
count = 0
for i in range(len(text)):
    if text[i] == ':':
        text = text[:i] + '%' + text[i + 1:]
        count = count+1
print("Количество замен:", count)
