import random
import math


class MiniCalculator:
    @staticmethod
    def random_maker1():
        operation = ['+', '-', '*']
        symbol = random.choice(operation)
        first_operand = random.randint(2, 9)
        second_operand = random.randint(2, 9)
        print(f'{first_operand} {symbol} {second_operand}')
        return f'{first_operand} {symbol} {second_operand}'

    @staticmethod
    def calculate_result(random_word):
        while True:
            ans = input()
            if ans.isdigit():
                ans = int(ans)
                if eval(random_word) == ans:
                    return "Right!"
                else:
                    return "Wrong!"
            elif ans.lstrip('-').isdigit():
                ans = int(ans)
                if eval(random_word) == ans:
                    return "Right!"
                else:
                    return "Wrong!"
            else:
                print("Incorrect format.")

    def main(self):
        count = 0
        mark = 0
        while True:
            rand = self.random_maker1()
            st = self.calculate_result(rand)
            if st == 'Right!':
                mark = mark + 1
            print(st)
            count = count + 1
            if count == 5:
                break
        print(f'Your mark is {mark} / 5')
        return f'{mark}/5'


class DifficultCalculator:
    @staticmethod
    def random_maker2():
        number = random.randint(11, 29)
        print(number)
        return number

    @staticmethod
    def check_result(num):
        while True:
            ans = input()
            if ans.isdigit():
                ans = int(ans)
                if num ** 2 == ans:
                    return "Right!"
                else:
                    return "Wrong!"
            else:
                print('Wrong format! Try again.')

    def main(self):
        count = 0
        mark = 0
        while True:
            rand = self.random_maker2()
            st = self.check_result(rand)
            if st == 'Right!':
                mark = mark + 1
            print(st)
            count = count + 1
            if count == 5:
                break
        print(f'Your mark is {mark} / 5')
        return f'{mark}/5'


def start():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        choice = int(input())
        if choice not in [1, 2]:
            print("Incorrect format.")
        else:
            break
    if choice == 1:
        calc = MiniCalculator()
        ans = calc.main()
        print("Would you like to save your result to the file? Enter yes or no.")
        choice = input()
        if choice in ['Yes', 'YES', 'yes', 'y']:
            name = input('What is your name?')
            with open('results.txt', 'a', encoding='UTF-8') as result:
                result.write(f'{name}: {ans} in level 1 (simple operations with numbers 2-9).')
            print("The results are saved in 'results.txt'.")
    elif choice == 2:
        calc = DifficultCalculator()
        ans = calc.main()
        print("Would you like to save your result to the file? Enter yes or no.")
        choice = input()
        if choice in ['Yes', 'YES', 'yes', 'y']:
            name = input('What is your name?')
            with open('results.txt', 'a', encoding='UTF-8') as result:
                result.write(f'{name}: {ans} in level 2 (integral squares of 11-29).')
            print("The results are saved in 'results.txt'.")


start()
