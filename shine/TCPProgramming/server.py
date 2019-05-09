import socket,threading

def run(clientSocket):
    data = clientSocket.recv(1024)
    print('客户端说：%s' % (data.decode('utf-8')))
    replyData = input()
    clientSocket.send(replyData.encode('utf-8'))

# 创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定ip和端口
s.bind(('10.25.14.68',8080))
# 监听
s.listen(5)
print('服务器启动成功')



# accept返回的socket是和服务器连接成功而生成的一个用于相互传输数据的新的socket，有多少个客户端连接，就生成多少个socket，address为连接成功的客户端的地址（ip地址和端口号）
# tcp协议由于已经建立了连接，所以采用send和recv方法发送和接收数据



while True:
    # 等待连接
    clientSocket, clientAddress = s.accept()
    print('%s --- %s连接成功' % (clientSocket, clientAddress))
    # 在线程去中去处理不同client的交互
    t = threading.Thread(target=run,args=(clientSocket,))
    t.start()

