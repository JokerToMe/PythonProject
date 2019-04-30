from person import Person
from child import Child

class Student(Person,Child):

    def __init__(self,name,age,money,stuId,hobby):
        # 父类只有一个的情况下，继承父类构造方法的写法
        # super(Student,self).__init__(name,age,money)
        # 父类有多个的情况下
        Person.__init__(self,name,age,money)
        Child.__init__(self,hobby)
        # 子类独有的属性
        self.stuId = stuId

    def stuFunc(self):
        print(self.__money)