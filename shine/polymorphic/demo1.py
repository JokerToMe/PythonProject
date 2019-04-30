# 多态：一种事物的多种形态
# 案例：人可以喂任何一种动物

from cat import Cat
from mouse import Mouse
from person import Person

def main():
    tom = Cat('Tom')
    jerry = Mouse('Jerry')
    tom.eat()
    jerry.eat()
    p = Person()
    p.feedAnimal(tom)
    p.feedAnimal(jerry)

if __name__ == '__main__':
    main()