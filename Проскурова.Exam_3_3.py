# 3. Дописать классы Human, House, SmallHouse (как на последнем занятии).
class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name, self.age, 'лет.', 'На счете:', self.__money, 'Дом:', self.__house)

    def make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def by_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.make_deal(house, price)

        else:
            print('No money!')

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, money):
        self.__money += money
        print(f'Получено: {money}. Текущий счет: {self.__money}')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        f_price = self._price*(100-discount)/100
        print(f'Финальная стоимость: {f_price}')
        return f_price


class SmallHouse(House):
    default_area = '40 м2'

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

    def __str__(self):
        return SmallHouse.default_area


sm_house = SmallHouse(10000)

lyudmila = Human('Lyudmila', 39)
lyudmila.by_house(sm_house, 5)

lyudmila.earn_money(10000)
lyudmila.by_house(sm_house, 5)
lyudmila.info()

lyudmila.earn_money(20000)
lyudmila.info()
