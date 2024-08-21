list_goods = ['молоко Хорская Буренка:70:5\n', 'молоко Фермерское:55:10\n',
               'молоко Простоквашино:66:5\n', 'хлеб серый хлебозавод:30:20\n',
               'яйцо 1 кат.:30:40\n', 'яйцо 2 кат.:30:40\n',
              'яйцо 3 кат.:30:40\n', 'макароны Макфа,рожки:30:10\n',
              'макароны Макфа,спагетти:30:10\n', 'сахар 1кг:40:30\n',
              'соль 1 кг:35:30\n', 'масло сливочное:100:20\n',
              'масло подсолнечное:100:20\n', 'говядина 1кг:250:10\n',
              'свинина 1кг:220:10\n', 'баранина 1кг:210:10\n',
              'филе куриное 1кг:200:10\n', 'грудка куриная 1кг:225:10\n',
              'голень куриная 1кг:230:10\n', 'крылышки куриные 1кг:180:10\n',
              'рыба мороженая, Кета 1кг:400:5\n', 'рыба мороженая, Треска 1кг:300:5\n',
              'рыба мороженая, Горбуша 1кг:300:5\n', 'рыба мороженая, Окунь 1кг:300:5\n',
              'чай черный Greenfield 10 пак.:50:20\n', 'Чай черный Lipton 10 пак.:60:20\n',
              'чай зеленый Greenfield 10 пак.:50:20\n', 'Чай зеленый Lipton 10 пак.:60:20\n',
              'мука пшеничная Весёлый мельник 1кг.:40:20\n', 'мука пшеничная Весёлый мельник 2кг.:60:10\n',
              'хлеб ржаной хлебозавод:50:20\n', 'сушки 1кг.:45:20\n',
              'пряники 1кг.:55:20\n', 'булочки плюшки:30:10\n',
              'пирожки с брусникой:30:10\n', 'пирожки с картошкой:30:2\n',
              'пирожки с вишней:30:10\n', 'рис шлифованный 1кг:40:10\n',
              'рис круглозерный 1кг:45:10\n', 'пшено 1кг:50:30\n',
              'крупа гречневая 1кг:60:30\n', 'вермишель Макфа 1кг:45:20\n',
              'картофель 1кг:60:50\n', 'капуста белокочаная 1кг:60:50\n',
              'лук репчатый 1кг:40:50\n', 'морковь 1кг:55:50\n', 'яблоки Новая Зеландия 1кг:60:120'
              ]


mean = 0
count_all = 0
summ = 0
max_price = 0
min_price = 100000
max_index = 0
min_index = 0
set_goods = set()

for good in list_goods:
    price = int(good.split(':')[1])
    summ += price
    count_all += 1
    if price > 100:
        set_goods.add(good)
    if price > max_price:
        max_price = price
        max_index = list_goods.index(good)
        print(f'максимальная цена: {max_price}')
        print(f'индекс максимальной цены {max_index}')
    if price < min_price:
        min_price = price
        min_index = list_goods.index(good)
        print(f'минимальная цена: {min_price}')
        print(f'индекс минимальной цены: {min_index}')

dict_goods = {}
dict_goods['mean'] = summ / count_all
dict_goods['summ'] = summ
dict_goods['count_all'] = count_all

print(dict_goods)
print(set_goods)


def work_with_list(list_goods, is_max_min):
    list_result = []
    max = 0
    min = 999999

    for good in list_goods:
        price = int(good.split(':')[1])

        if price > max:
            max = price

        if price < min:
            min = price

    if is_max_min:
        for good in list_goods:
            price = int(good.split(':')[1])
            name = good.split(':')[0]

            if price == max:
                list_result.append(name)
    else:
        for good in list_goods:
            price = int(good.split(':')[1])
            name = good.split(':')[0]

            if price == min:
                list_result.append(name)

    return list_result


list_goods_max = work_with_list(list_goods, is_max_min=True)
list_goods_min = work_with_list(list_goods, is_max_min=False)

print(list_goods_max)
print(list_goods_min)