import threading, random, time
from threading import Thread, Lock


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()
        self.count = 0
        self.transaction = 100

    def deposit(self):
        for i in range(self.transaction):
            self.count += 1
            self.money = random.randrange(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            elif self.balance <= 500 and self.lock.locked():
                self.lock.release()
                self.balance += self.money
                self.lock.acquire()
            else:
                self.balance += self.money
            print(f'Пополнение: {self.money}. Баланс: {self.balance}.')
            time.sleep(0.001)

    def take(self):
        for i in range(self.transaction):
            self.money = random.randrange(50, 500)
            print(f'Запрос на: {self.money}')
            if self.money <= self.balance:
                self.balance = self.balance - self.money
                print(f'Снятие {self.money}. Баланс {self.balance}')
            elif self.count == self.transaction:
                print('Запрос отклонён')
            elif self.money > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
