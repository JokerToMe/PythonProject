import socket

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.bind(('10.25.14.68',8900))

while True:
    # 1024：接收数据的量
    data,addr = udp.recvfrom(1024)
    print('客户端说：'+data.decode('utf-8'))
    reply = input()
    # UDP协议由于没有和客户端建立连接，所以发送和接收数据采用sendto和recvfrom方法，必须明确发送对象和接收对象
    # addr是从recvfrom中接收到的客户端的地址信息，从哪里接收就从哪里发出
    udp.sendto(reply.encode('utf-8'),addr)