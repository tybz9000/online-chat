import socket
addrl=[0,0]#地址列表
packgel=1024#单包大小
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#定义连接
hostt=open('s.txt','r')
ipport=hostt.readline()
ip,port=ipport.split(" ",1)
port=int(port)
print(port)
hostt.close()
s.bind((ip,port))#绑定连接
s.listen(5)#设置监听
print('链接等待中......')
con1,addrl[0] = s.accept()
print('链接来自',addrl[0])
con2,addrl[1] = s.accept()
print('链接来自',addrl[1])
data='2333'#防止发送端抢先发送
con1.send(data.encode())
data=con1.recv(1024)
con2.send(data)
data=con1.recv(1024)
con2.send(data)
while (1):
    data=con1.recv(packgel)
    con2.send(data)
    if not data:
        break
con1.close()
con2.close()

