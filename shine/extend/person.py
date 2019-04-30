class Person(object):

    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.__money = money

    def setMoney(self,money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def comFunc(self):
        print('Func，Person')