from student import Student

s = Student('shine',18,1000,100,'game')
print(s.name,s.age,s.stuId)
# 父类的私有属性无法被子类继承，但可以通过父类的set和get方法去赋值和访问
# s.stuFunc()
s.setMoney(23)
print(s.getMoney())
print(s.hobby)
# 当多个父类中含有相同的方法时的调用情况
# 总结：优先调用放在括号前面的父类的方法，Person先于Child类
s.comFunc()




