from animal import Animal

class Mouse(Animal):

    def __init__(self,name):
        Animal.__init__(self,name)

    def eat(self):
        print('%s在吃' % self.name)