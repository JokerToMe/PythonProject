# 通常将json称为轻量级的传输方式
import json

# loads：将字符串转为json格式
# dumps：将json格式转为字符串
# load：将json文件转为json格式
# dumps：将json格式转为转为json文件
# json格式等同于python的dict数据结构

jsonStr = '{"name":"shine","age":18}'

jsonData = json.loads(jsonStr)
print(jsonData)
print(jsonData['name'])
print(type(jsonData))

data = {}

# 可以把.json文件当做类似于.txt格式的文件，读写模式为r和w

# 读取本地的json文件
with open(r'package.json','r') as f:
    data = json.load(f)
    print(type(data))
    print(data)

# 把dict写入文件
with open(r'packageCopy.json','w') as f:
    json.dump(data,f)