from person import Person

class Worker(Person):

    def __init__(self,name,age):
        # 继承父类构造方法的写法
        super(Worker,self).__init__(name,age)