words = input("Введите текст: ").split()
k=1
for i in words:
    print(k, i[:10])
    k+=1
