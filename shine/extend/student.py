from person import Person

class Student(Person):

    def __init__(self,name,age,stuId):
        # 继承父类构造方法的写法
        super(Student,self).__init__(name,age)
        # 子类独有的属性
        self.stuId = stuId