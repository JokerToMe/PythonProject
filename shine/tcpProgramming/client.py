import socket

# # 创建一个socket
# # 参数1：AF_INET：协议ipv AF_INET6：ipv6
# # 参数2：SOCK_STREAM：执行面向流的TCP协议
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 建立连接
# # 参数是一个元组
# s.connect(('www.sina.com.cn',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 等待接收数据
# data = []
# while True:
#     # 每次接收一次
#     tempData = s.recv(1024)
#     if tempData:
#         data.append(tempData)
#     else:
#         break
#
# dataStr = b''.join(data).decode('utf-8')
# print(dataStr)
# # 断开连接
# s.close()

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.25.14.68',8080))

count = 0
while True:
    count += 1
    data = input()
    s.send(data.encode('utf-8'))
    info = s.recv(1024)
    print('服务器说：%s' % info.decode('utf-8'))