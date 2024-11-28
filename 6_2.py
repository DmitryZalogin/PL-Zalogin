n=int(input("Введите размер массива: "))
arr=[int(input('Введите элемент: ')) for i in range(1,n+1)]
min_e=min(arr)
id=arr.index(min_e)
print("Минимальный элемент: ",min_e, "с индексом", id)
pos=[]
neg=[]
for el in arr:
  if el>0:
	  pos.append(el)
  else: neg.append(el)
print("Положительные элементы: ",pos)
print("Отрицательные элементы: ",neg)   
