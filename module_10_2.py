from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power, count_enemy=100):
        super().__init__()
        self.name = name
        self.power = power
        self.count_enemy = count_enemy
        self.count_day = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.count_enemy > 0:
            self.count_enemy = self.count_enemy - self.power
            self.count_day += 1
            print(f'{self.name} сражается {self.count_day} день(дня)...,',
                  f'осталось {self.count_enemy} воинов.')
            sleep(1)

            if self.count_enemy == 0:
                print(f'{self.name} одержал победу спустя {self.count_day} дней(дня)!')
                return None


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
