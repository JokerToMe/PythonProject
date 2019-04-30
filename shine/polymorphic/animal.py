class Animal(object):

    def __init__(self,name):
        self.name = name

    def eat(self):
        print('%s在吃' % self.name)