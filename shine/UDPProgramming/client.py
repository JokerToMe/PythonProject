import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = input()
    s.sendto(data.encode('utf-8'),('10.25.14.68',8900))
    info = s.recv(1024)
    print('服务器回答说：'+info.decode('utf-8'))