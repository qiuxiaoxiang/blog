#!/usr/bin/env python3
from socket import *
from time import *

host = ''
port = 21567
bufsiz = 1024
addr = (host,port)

tcpsock = socket(AF_INET,SOCK_STREAM)
tcpsock.bind(addr)
tcpsock.listen(5)

while True:
    print('waiting for connection...')
    sock,addr = tcpsock.accept()
    print('...connected from:' ,addr)
    while True:
        data = sock.recv(bufsiz).decode('utf-8')#接收客户端发来的信息
        sock.send(data.encode('utf-8'))
        print(data)
    sock.close()
tcpsock.close()



"""
首先是创建一个tcp服务器，然后定义好地址，端口，以及各种参数，然后给这个tcp服务器创建一个套接字，
套接字也就是相当于电话线的接口，创建好了套接字之后我们就可以开始来设计tcp服务器的各种功能了，一般
来说tcp服务器的功能就是接受客户端的连接，然后接收客户端发送过来的信息并广播出去，但是砸门这个过程
不可能搞一次就结束了吧，所以需要把各种功能嵌套在循环里面，首先是接收客户端的连接请求，要用到accept()
函数，这个函数是tcp服务器被动的接收客户端的连接，一直等待连接的到达，连接上了之后就可以接收客户端发送
过来的信息了，用到了recv()函数，然后发送广播信息就用到了send()函数，特别要记住的是函数的使用很多都是需要
添加参数的。
"""