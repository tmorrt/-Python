lst = []
n = int(input('Введите кол-во элементов в списке: '))

for i in range(n):
    lst.append(input('Введите элемент списка: '))
print(lst)

for i in range(0, len(lst) - 1, 2):
    a = lst[i]
    lst[i] = lst[i+1]
    lst[i+1] = a
print(lst)
