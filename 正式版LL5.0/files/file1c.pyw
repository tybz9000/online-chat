import socket
import os
import time

import tkinter###
import threading
threads=[]
root=tkinter.Tk()###
root.title=('等待发送')###
root.option_add("*Font",'华文行楷')###
root['background']='lightblue'###
root.wm_resizable(width = False, height = False)###
root.geometry('420x100+50+50')###
packgel=1024#定义单包大小，单位字节
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#建立tcp连接
hostt=open('c.txt','r')
ipport=hostt.readline()
ip,port=ipport.split(" ",1)
port=int(port)
hostt.close()

s.connect((ip,port))#绑定连接
s.recv(1024)#告诉它连接成功
def get_name(event):
    global fname
    fname=namec.get()
def sendd(event):
    for t in threads:
        t.setDaemon(True)
        t.start()

def main():
    xx=0
    big=os.path.getsize(fname)
    Big=str(big)
    s.send(fname.encode())
    time.sleep(0.1)
    s.send(Big.encode())
    time.sleep(0.1)
    sfile=open(fname,'rb')#二进制格式打开要传输的文件
    while (1):
        time.sleep(0.01)
        data=sfile.read(packgel)
        x=s.send(data)
        xx+=x
        X=str(xx)
        bfs=int(xx*100/big)
        BFS=str(bfs)
        value.set(BFS+'% 文件已传输：'+X+'文件总大小：'+Big)
        if not data:
            break
    s.close()
    sfile.close()
t1=threading.Thread(target=main)
threads.append(t1)

lb2=tkinter.Label(root,text='文件名',background='lightblue',fg='green').place(x = 0,y = 10, anchor = tkinter.NW)
namec = tkinter.Entry(root,width = 36)
namec.bind("<KeyRelease>",get_name)
namec.place(x =0,y =40, anchor = tkinter.NW)

bt1=tkinter.Button(root,width=18,text='发送')
bt1.bind("<Button-1>",sendd)
bt1.place(x=260,y=40)

value = tkinter.StringVar()
value.set('等待传输ing.......')
res = tkinter.Entry(root,width = 60, textvariable = value)
res.place(x=0,y=70)

root.mainloop()

