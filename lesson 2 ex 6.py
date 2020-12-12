kol = int(input('Введите кол-во товаров: '))
item = {'Название': '', 'Цена': '', 'Количество': '', 'Единицы': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Единицы': []}
goods = []
n=1
for k in range(kol):
    item['Название'] = input(f'Введите название товара {n}: ')
    item['Цена'] = input(f'Введите цену товара {n}: ')
    item['Количество'] = input(f'Введите кол-во товара {n}: ')
    item['Единицы'] = input(f'Введите единицы товара {n}: ')

    analytics['Название'].append(item['Название'])
    analytics['Цена'].append(item['Цена'])
    analytics['Количество'].append(item['Количество'])
    analytics['Единицы'].append(item['Единицы'])

    print('Добавлен новый товар:', item)

    n_item = (n, item.copy())
    goods.append(n_item)
    n+=1

print()
print('Информация о товарах:')
for i in goods:
    print(i)

print()
print('Аналитика о товарах: ')
for key, value in analytics.items():
  print("{0}: {1}".format(key, value))