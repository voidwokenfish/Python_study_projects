with open("./list_of_goods.txt", "r", encoding="utf-8") as file:
    list_goods = file.readlines()


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