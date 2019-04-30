from animal import Animal

class Cat(Animal):

    def __init__(self,name):
        Animal.__init__(self,name)

    def eat(self):
        print('%s在吃' % self.name)