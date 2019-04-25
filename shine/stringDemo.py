str1 = 'a'
print(ord(str1))
str2 = 'hello,python,hello,python'
print(str2.split(','))
# 截取2个字符串
print(str2.split('o',2))
# 按照 '\r' '\r\n'和'\n'来截取
str3 = 'hello\npython'
print(str3)
print(str3.splitlines())
# 用指定字符串连接字符串数组
print(' '.join(['hello','python','you','are','welcome']))
str4 = 'abcdefg123456'
# 用ASC码值比较大小
print(max(str4))
print(min(str4))
# 字符串替换
print(str4.replace('123456','hijk'))
# 在指定的范围内，判断是否以某段字符串开头 startswith(str,start=0,end=len(str))
print(str4.startswith('abc'))
print(str4.startswith('def',3))
print(str4.startswith('def',3,7))
# 以某段字符串结尾
print(str4.endswith('456'))
# 编码 ignore:错误忽略不处理
data = '你好'.encode('utf-8','ignore')
print(data)
print(type(data))
print(data.decode('utf-8','ignore'))
# 字符串长度大于1，且所有字符都不能为空格
print('abcdef'.isalpha())
print('abcdef '.isalpha())
# 字符串长度大于1，且所有字符都是数字或者字母
print('abcdef','isalnum','abcdef'.isalnum())
print('abcdef*','isalnum','abcdef*'.isalnum())
# 字符串长度大于1，且至少有一个字母，且所有的字母都必须大写
print('abcef'.isupper())
print('ABC*','isupper','ABC*'.isupper())
print('1','isupper','1'.isupper())
# 验证小写
print('abc','islower','abc'.islower())
# 标题化(所有的单词首字母必须大写)
print('Hello,World'.istitle())
print('Hello,world'.istitle())
print('hello,world'.istitle())
# 只包含数字字符
print('123'.isdigit())
# 判断是否只包含空格
print(''.isspace())
print(' '.isspace())
print('\n'.isspace())