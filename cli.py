#!/usr/bin/env python3
from socket import *
host = 'localhost'
port = 21567
bufsiz = 1024
addr = (host,port)

tcpclient = socket(AF_INET,SOCK_STREAM)
tcpclient.connect(addr)

while True:
    data = input('>>>')
    tcpclient.send(data.encode('utf-8'))
    data = tcpclient.recv(bufsiz).decode('utf-8')
    #这里的recv此时是没有任何作用的，因为此时是半双工聊天，所以只有服务器和一个客户端在进行通信，没有其他客户端发送信息
    #给服务端，所以客户端不会接收到信息。
    print(data)
tcpclient.close()
