lst = [7, 5, 3, 3, 2]
print(lst)
while 1:
    new = int(input("Введите новый элемент: "))
    for i in range (len(lst)):
        if new > lst[i]:
            lst.insert(i, new)
            break
        elif new <= min(lst):
            lst.append(new)
            break
    print(lst)