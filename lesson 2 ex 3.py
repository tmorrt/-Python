# Через list
months = [
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12
]

n = int(input('Введите номер месяца: '))

for i in months:
    if n == i:
        if i == 3 or i == 4 or i == 5:
            print("Весна")
        elif i == 6 or i == 7 or i == 8:
            print("Лето")
        elif i == 9 or i == 10 or i == 11:
            print("Осень")
        else:
            print("Зима")

# Через dict
seasons = {
    1: "Весна",
    2: "Лето",
    3: "Осень",
    4: "Зима"
}
if n == 3 or n == 4 or n == 5:
    print(seasons.get(1))
elif n == 6 or n == 7 or n == 8:
    print(seasons.get(2))
elif n == 9 or n == 10 or n == 11:
    print(seasons.get(3))
elif n == 12 or n == 1 or n == 2:
    print(seasons.get(4))