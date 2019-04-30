from person import Person

# 在给对象属性命名时不要和类属性重名

def main():
    p = Person('对象属性')
    # 对象属性的优先级比累属性高，在没有对象的属性的情况下才调用类属性
    print(p.name)
    print(Person.name)
    # 在删除对象属性的情况下，同名的类属性依然可以调用
    del p.name
    print(p.name)

if __name__ == '__main__':
    main()