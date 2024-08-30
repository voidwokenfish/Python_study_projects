class Good:
    '''Класс товара'''

    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price

class GoodList:
    '''Класс со списком товаров'''

    def __init__(self):
        self.good_list = []

    def add_good_in_list(self, good: Good):
        '''Добавляем товар в список'''

        self.good_list.append(good)

    def get_mean_price(self):
        '''Получаем среднюю цену товаров'''

        sum_price = 0
        sum_count = 0

        for good in self.good_list:
            sum_price += int(good.price)
            sum_count += int(good.count)

        print(f'sum goods = {sum_price}')
        print(f'sum count = {sum_count}')

        mean = sum_price / sum_count

        return mean


    def get_good_with_max_price(self):
        '''Получаем товар с максимальной ценой'''

        name = ''
        max_price = 0

        for good in self.good_list:
            if good.price > max_price:
                max_price = good.price
                name = good.name

        return name

    def get_good_with_min_price(self):
        '''Получаем товар с минимальной ценой'''

        name = ''
        min_price = 10000

        for good in self.good_list:
            if good.price < min_price:
                min_price = good.price
                name = good.name

        return name

    def get_good_with_max_count(self):
        '''Получаем товар с максимальным количеством'''

        name = ''
        max_count = 0

        for good in list_with_goods:
            if good.count > max_count:
                max_count = good.count
                name = good.name

        return name

    def get_good_with_min_count(self):
        '''Получаем товар с максимальным количеством'''

        name = ''
        min_count = 0

        for good in list_with_goods:
            if good.count < min_count:
                min_count = good.count
                name = good.name

        return name


good_list = GoodList()

with open('list_of_goods.txt', 'r') as file:
    list_with_goods = file.readlines()

    for str_good in list_with_goods:
        list_good = str_good.split(':')

        name = list_good[0]
        price = list_good[1]
        count = list_good[2]

        good_list.add_good_in_list(Good(name, price, count))
        good_list.get_mean_price()


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