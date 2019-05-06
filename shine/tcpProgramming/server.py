import socket

# 创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定ip和端口
s.bind(('10.25.14.68',8080))
# 监听
s.listen(5)

print('服务器启动成功')

# 等待连接
clientSocket,clientAddress = s.accept()

print('%s --- %s连接成功' % (clientSocket,clientAddress))

while True:
    data = clientSocket.recv(1024)
    print('客户端说：%s' % (data.decode('utf-8')))
    replyData = input()
    clientSocket.send(replyData.encode('utf-8'))
