# TCP是建立可靠的连接，通信双方可以通过流的形式发送数据
# 相对于TCP，UDP无需建立连接，只需要知道对方的ip地址和端口号就可以直接发送数据包
# 特点：不可靠但速度快
# 对于要求不高的数据传输可以使用UDP传输协议，多数情况用于广播数据

import socket

# dragm：数据报
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('10.25.14.68',2425))
# 模拟飞秋程序时，字符串有特定的格式，需百度
str = 'shine law'
s.send(str.encode('utf-8'))
