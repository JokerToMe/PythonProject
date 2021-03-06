# 思考：如果不同的人编写模块同名怎么办？
# 解决：为了解决模块命名的冲突，引入了按目录来组织模块的方法，成为包
# 特点：引入了包以后，只要顶层的包不与其他人发生冲突，模块都不会发生冲突

import law
# 加上报名进行引用，调用才会成功
import test.law

# 仅有此方法会执行成功，因为查找模块的原则是就近选择
law.sayGoodOuter()
test.law.sayGoodInner()
# law.sayGood()

# 注意，目录只有包含了__init__.py文件才被认作一个包，主要为了避免一些滥竽充数的名字，目前未知，这个文件中什么都不用写


