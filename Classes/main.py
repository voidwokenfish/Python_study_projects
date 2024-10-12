class Player:
    def __init__(self, health, attack, armor, inventory):
        self.health = health
        self.attack = attack
        self.armor = armor
        self.inventory = inventory

    def attributes(self):
        """ Атрибуты, влияющие на персонажа"""
        pass

    def equipment(self):
        """ Берем вещи из инвентаря и надеваем туть"""
        pass


class Inventory:
    items: list

    def __init__(self):
        self.items = list()

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __getattr__(self, item):
        print(f' {item} not exist')
        return None

    def __setattr__(self, key, value):
        print(f'{key} not exist')

class Item:

    def __init__(self, item: str, stackable: bool, weight: float=0.0, value: float=0.0):
        self.item = item
        self.stackable = stackable
        self.weight = weight
        self.value = value






class Mob:
    def __init__(self, health, attack, armor):
        self.health = health
        self.attack = attack
        self.armor = armor

    def take_damage(self, damage):
        """ Формула расчета получаемого урона"""
        pass

    def loot(self):
        """ Формирует лут c мобов"""
        pass



class Demon(Mob):
    def __init__(self, health, attack, armor):
        super().__init__(health=health, attack=attack, armor=armor)

    def demon_passive(self):
        """ Пассивка доступная мобу демон!"""
        pass

class Orcoid(Mob):
    def __init__(self, health, attack, armor):
        super().__init__(health=health, attack=attack, armor=armor)

    def orcoid_passive(self):
        """Пассивка оркоидов"""
        pass

class Orc(Orcoid):
    def __init__(self, health, attack, armor):
        super().__init__(health=health, attack=attack, armor=armor)

    def enrage(self):
        """Пассивка класса орк"""
        pass

class Goblin(Orcoid):
    def __init__(self, health, attack, armor):
        super().__init__(health=health, attack=attack, armor=armor)

    def backstab(self):
        """Пассивка класса гоблин"""
        pass

