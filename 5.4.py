text = input("Введите строку: ")
count = 0
for i in range(len(text)):
    if text[i] == 'а':
        text = text[:i] + 'о' + text[i + 1:]
        count = count+1
print("Количество замен:", count)
print(text)
print("Длина строки:", len(text))
