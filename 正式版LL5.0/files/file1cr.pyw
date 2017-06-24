import socket
import os
import tkinter###
import threading
threads=[]
root=tkinter.Tk()###
root.title=('等待接收')###
root.option_add("*Font",'华文行楷')###
root['background']='lightblue'###
root.wm_resizable(width = False, height = False)###
root.geometry('420x100+100+100')###

packgel=1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostt=open('cr.txt','r')
ipport=hostt.readline()
ip,port=ipport.split(" ",1)
port=int(port)
hostt.close()
s.connect((ip,port))

def main():
    filename=(s.recv(1024)).decode()
    filebig=(s.recv(1024)).decode()
    filebig=int(filebig)
    sfile=open('c'+filename,'wb')
    i=0
    while True:
        if(i%100==0):
            big=os.path.getsize('c'+filename)
            BIG=str(big)
            FILEBIG=str(filebig)
            bfs=int(big*100/filebig)
            BFS=str(bfs)
            value.set(BFS+'% 文件已传输：'+BIG+'文件总大小：'+FILEBIG)
        i+=1
        data=s.recv(packgel)
        sfile.write(data)
        if not data:
            break
    s.close()
    sfile.close()
t1=threading.Thread(target=main)
threads.append(t1)
for t in threads:
        t.setDaemon(True)
        t.start()


value = tkinter.StringVar()
value.set('等待传输ing.......')
res = tkinter.Entry(root,width = 60, textvariable = value)
res.place(x=0,y=70)

root.mainloop()
