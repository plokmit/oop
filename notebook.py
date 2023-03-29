import sys
from random import randint
class Players:
    arhive = {}
class Game:
    def __init__(self):
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.black = [_ for _ in range(36) if _ not in self.red]
    def new_player(self, new_name, new_balance = 1000):
        self.new_name = new_name
        if self.new_name not in Players.arhive.keys():
            self.new_balance = new_balance
            Players.arhive[self.new_name] = self.new_balance
            print ("Создан игрок с именем: ", self.new_name, "Balance: ", self.new_balance, sep ="\n")
        else:
            print ("Incorrect name")
    def old_player(self, name):
        self.name = name
        if self.name not in Players.arhive.keys():
            print ("Игрока с таким именем не существует")
            return 0
        if self.name in Players.arhive.keys():
            self.balance = Players.arhive.get(self.name)
            print ("Выбран игрок с именем: ", self.name, "Баланс: ", self.balance)
        bets = {1 : "Straight bet", 2 : "Split bet", 3 : "Basket bet", 4 : 'Four numbers bet', 5 : "Red or black", 6 : "Even or odd"}
        print (bets)
        self.choice_bet = int(input ("Введите ставку, которую вы хотите сделать: "))
        if self.choice_bet not in bets.keys():
            print("Нет такой ставки, давай дубль 2")
            self.choice_bet = int(input("Введите ставку, которую вы хотите сделать: "))
        self.amount_of_bet = int(input("Введите сумму ставки:"))
        while self.amount_of_bet < 50:
            print("Сумма должнна быть больше")
            self.amount_of_bet = int(input("Введите сумму ставки больше 50: "))
        while self.amount_of_bet>self.balance:
            print("На балансе недостаточно средств, остаток: ", self.balance)
            self.amount_of_bet= int(input("Введите сумму ставки мменьше остатка на балансе: "))
        if self.choice_bet == 1:
            number = int(input("Введите 1 число: "))
            if number < 0 or number > 36:
                print("Боже, в рулетке всего 36 чисел, почитай правила и возвращайся")
                return 0
        if self.choice_bet == 2:
            number = [int(input("Введите 2 числа: ")) for _ in range(2)]
        if self.choice_bet == 3:
            number = [int(input("Введите 3 числа: ")) for _ in range(3)]
        if self.choice_bet == 4:
            number = [int(input("Введите 4 числа: ")) for _ in range(4)]
        if self.choice_bet == 5:
            print('''
                1.черные
                2.красные
                        ''')
            temp = int(input("Введите 1 или 2: "))
            if temp ==1:
                number = self.black
            if temp == 2:
                number = self.red
        if self.choice_bet == 6:
            print('''
            1.нечетные
            2.четные
            ''')
            temp = int(input("Введите 1 или 2: "))
            if temp ==1:
                number = [_ for _ in range(1,36,2)]
            if temp == 2:
                number = [_ for _ in range(2,37,2)]
        if type(number)==list:
            for num in number:
                if num < 0 or num > 36:
                    print("Боже, в рулетке всего 36 чисел, почитай правила и возвращайся")
                    return 0
        self.generator_of_number(number)
    def generator_of_number(self, number=None):
        res_of_number = randint(0,36)
        wins = {
            1: 35,
            2: 17,
            3: 11,
            4: 8,
            5: 1,
            6: 1
        }
        if res_of_number == 0:
            print("результат - 0")
        if res_of_number in self.red:
            print("красное", res_of_number)
        else:
            print("черное", res_of_number)
        if type(number) == int:
            if res_of_number == number:
                print("Поздравляем! Вы выиграли: ", self.amount_of_bet*wins[self.choice_bet], "Баланс: ", self.balance+self.amount_of_bet*wins[self.choice_bet])
                self.balance += self.amount_of_bet*wins[self.choice_bet]
                Players.arhive[self.name]=self.balance
            else:
                print("Вы проиграли")
                self.balance -= self.amount_of_bet
                Players.arhive[self.name] = self.balance
        else:
            if res_of_number in number:
                print("Поздравляем! Вы выиграли: ", self.amount_of_bet*wins[self.choice_bet], "Баланс: ", self.balance+self.amount_of_bet*wins[self.choice_bet])
                self.balance += self.amount_of_bet*wins[self.choice_bet]
                Players.arhive[self.name] = self.balance
            else:
                print("Вы проиграли")
                self.balance -= self.amount_of_bet
                Players.arhive[self.name] = self.balance

class Menu:
    def __init__(self):
        self.game = Game()
        self.choices_in_dict = {
            1: self.add_new_player,
            2: self.menu_choise_bet,
            3: self.my_player,
            4: self.quit
        }
    def display(self):
        print ( '''
        Menu:
            1. Создать нового игрока
            2. Начать игру
            3. Посмотреть баланс
            4. Выход
        ''')
    def add_new_player(self):
        print("add new player")
        self.game.new_player(input("Enter name: "))
    def menu_choise_bet(self):
        self.game.old_player(input("Введите имя игрока: "))
    def my_player(self):
        my_player = input("Введите имя игрока: ")
        if my_player in Players.arhive.keys():
            print(Players.arhive.get(my_player))
        else:
            print("Нет игрока с таким именем")
            my_player = input("Введите имя игрока: ")
    def run(self):
        while True:
            self.display()
            choice = int(input("enter action: "))
            action = self.choices_in_dict.get(choice)
            if action:
                action()
            else:
                print("incorrect action")
    def quit(self):
        print("Спасибо, что были с нами. Здесь могла быть ваша реклама")
        sys.exit(0)
if __name__ == "__main__":
    Menu().run()