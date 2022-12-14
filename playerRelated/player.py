import random


class Event:
    def __init__(self):
        pass

    def lottery(self, action):
        money = random.randint(20, 100)
        if action == 'win':
            print(f'You won the lottery! You got {money}!')
            return money
        elif action == 'lose':
            print('You didn\'t win!')
        else:
            print('Please put in one of the following: win\nlose')


class Stats:
    def __init__(self):
        self.strength = 0
        self.crafting = 0
        self.talking = 0

    def raiseStat(self, stat, desired):
        if stat == 'strength':
            self.strength += desired
        elif stat == 'crafting':
            self.crafting += desired
        elif stat == 'talking':
            self.talking += desired
        else:
            print('Please input one of the following: strength\ncrafting\ntalking')

    def setStat(self, stat, desired):
        if stat == 'strength':
            self.strength = desired
        elif stat == 'crafting':
            self.crafting = desired
        elif stat == 'talking':
            self.talking = desired
        else:
            print('Please input one of the following: strength\ncrafting\ntalking')

    def getStat(self, stat):
        if stat == 'strength':
            return self.strength
        elif stat == 'crafting':
            return self.crafting
        elif stat == 'talking':
            return self.talking
        else:
            print('Please input one of the following: strength\ncrafting\ntalking')


class Money:
    def __init__(self):
        self.money = 0.0

    def raiseMoney(self, desired):
        self.money += desired

    def setMoney(self, desired):
        self.money = desired

    def getMoney(self):
        return self.money

    def deductMoney(self, desired):
        self.money -= desired


class Info:
    def __init__(self, name):
        self.name = name

    def getName(self) -> str: return self.name

    def setName(self, name): self.name = name
