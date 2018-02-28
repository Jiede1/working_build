# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:34:10 2018

@author: pangmingyu
"""

#server

import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)
while True:
    c, addr = s.accept()     # 建立客户端连接。
    print('连接地址：', addr)
    c.send('欢迎访问菜鸟教程！')
    c.close()                # 关闭连接