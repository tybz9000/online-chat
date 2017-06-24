import socket#引入网络连接包
import tkinter#导入图形界面包
from tkinter import ttk#导入更精致的tkinter
import time#导入时间包
from PIL import Image, ImageTk#导入pil包，使用外部图片
import random#引入随机函数
import os#引入时间模块
global c,k,k1,CL,b,ab#全局一些变量
c=0
b=1025
k= str(random.randint(1000,b))#一个随机初始头像
k1=k
CL= str(random.randint(1000,9999))#一个随机初始用户名
ab=os.path.dirname(__file__)+'\\files\\'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)#建立连接
root = tkinter.Tk()#主窗口出现
root.title('LL 5.0')#名字
root.option_add("*Font",'华文行楷')#字体
root['background']='lightblue'#背景色
root.wm_resizable(width = False, height = False)#窗口禁止缩放
root.geometry('490x495+100+100')#定义窗口大小
def get_ip(event):#获取ip函数
    global host
    host= et1.get()
def get_dk(event):#获取端口
    global dk
    if et2.get().isdigit() is True:
        dk= int(et2.get())#防止因为端口不是数字爆掉
def get_nm(event):#获取昵称函数
    global name
    name= et3.get()
def get_string(event):#获取输入的玩意的函数
    global data
    data= et4.get()
def contract(event):#主连接
    global k
    data= et4.get()
    if len(et4.get()) == 0 or data=='请输入内容':#防止用户什么都不输刷屏
        et4.delete(0,tkinter.END)
        et4.insert(tkinter.END,'请输入内容')
    else:
        data=k+'^'+name+' ( '+ 'hereisthetime\n' + ' )'+'\n '+"      "+data+'\n'
        sock.sendto(data.encode(),(host,dk))#发送给服务器
        et4.delete(0,tkinter.END)#清空输入端
def receive(event):#定义接收函数
    global p,imt2,name,ab#全局变量，防止未定义情况出现
    if len(et3.get()) == 0:
        et3.insert(tkinter.END,'游客'+CL)
        name='游客'+CL#防止没输入昵称出错
    data='idliketoconnecttheserver'
    et3.bind("<KeyPress-Return>",change)
    sock.sendto(data.encode(),(host,dk))#发送连接信号
    data=name
    sock.sendto(data.encode(),(host,dk))#再次发送，发送昵称
    p=-1
    imt2=[]
    def cout(i):#递归防止程序挂起
        global imt2,p,ab#引用全局变量，防止出现未定义的情况
        time.sleep(0.2)#引入人工延迟
        bt2.destroy()#删除按钮
        lb100=tkinter.Label(root,bg='lightblue',text=' 欢迎光临\n 请文明上网')#欢迎语
        lb100.place(x=355,y=20)#放置按钮
        et1.config(state='disabled')
        et2.config(state='disabled')#让这两个按钮暂时不能再按，防止出现bug
        if(i==20000):
            et3.config(state='disabled')#同上
        if(i>0):
            try:
                sock.settimeout(0.1)#定义防阻塞延迟
                recvdata,recvaddr=sock.recvfrom(4096)#接受信息
                datad=recvdata.decode()#解压
                if datad=='ok':#如果信息是ok
                    recvdata,recvaddr=sock.recvfrom(4096)#打开文件传输模块
                    dk2=recvdata.decode()
                    hostt=open('c.txt','w')
                    hostt.write(str(host)+' '+str(dk2))
                    hostt.close()
                    os.startfile('file1c.pyw')
                elif datad=="sbwanttosendyouafile":#或者秘钥是我想发文件
                    recvdata,recvaddr=sock.recvfrom(4096)#以写的形式打开cr.txt文件，用以传递参数
                    dk2=recvdata.decode()
                    hostt2=open('cr.txt','w')
                    hostt2.write(str(host)+' '+str(dk2))#写入ip和端口
                    hostt2.close()#关闭文件
                    os.startfile('file1cr.pyw')#打开送文件程序
                elif datad=='开始聊天吧\n':#如果密码是开始聊天
                    bt3.config(state='normal',cursor="arrow")
                    et4.config(state='normal')
                    bt1.config(state='normal',cursor="arrow")#调节按钮状态
                    t.see(tkinter.END)#让text一直显示在末尾
                    t2.delete(0,tkinter.END)#删除输入的东西
                    recvdata,recvaddr=sock.recvfrom(4096)#接受信息 
                    datad=recvdata.decode()
                    global ammount
                    ammount=int(datad.count('\n'))#记录用户人数
                    datadsp=datad.split('\n')
                    for kl in datadsp:#创建在线列表
                        t2.insert(tkinter.END,kl)
                        t2.see(tkinter.END)
                else:
                    data=datad.split('^')#表情系统
                    for m in range(0, len(data)):
                        if str(data[m]).isdigit() is True:#对于每一个表情如果它是数字
                            image = Image.open("pics/"+str(data[m])+".jpg")#插入表情
                            if(int(data[m])<5000):#如果小于5000
                                imt=image.resize((30,30))#插入图片
                            else:#否则
                                imt=image.resize((25,25))
                            p+=1#计数
                            imt2.append(ImageTk.PhotoImage(imt))#插入表情
                            t.image_create(tkinter.END,image = imt2[p])
                        else:#如果它不是表情
                            t.insert(tkinter.END,str(data[m]))#把它按照正常文字插入
                            t.see(tkinter.END)#一直在底部显示
            except socket.timeout:#防阻塞
                pass
            t.after(100,cout,i-1)
    cout(20000)#安全运行20000s
def change(event):#定义各种按钮可点不可点机制，防止bug，开始改名系统
    global c,name#全局变量，防未定义
    if(c==1):#c作为状态变量
        if len(et3.get()) == 0:#如果用户没有输入昵称
            et3.insert(tkinter.END,'游客'+CL)#系统为用户添加一个昵称
            name='游客'+CL
        data='iwanttochangemyname'#发送改名秘钥
        sock.sendto(data.encode(),(host,dk))#发送给服务器
        data=name
        sock.sendto(data.encode(),(host,dk))#发送要改的昵称
        c=2#状态2
        et3.config(state='disabled')#调整各按钮状态
        bt1.config(state='normal',cursor="arrow")
        et4.config(state='normal')
    if(c==0):#状态0
        et3.config(state='normal')#调整各按钮状态
        bt1.config(state='disabled',cursor="circle")
        et4.config(state='disabled')
        c=1
    if(c==2):#跳跃执行命令
        c=0
def refresh(event):#头像随机化函数
    global im,image,im2,canva,k1,k#全局变量，防止未定义情况出现
    canva.delete(im)
    k= str(random.randint(1000,b))#设置随机机制
    while(k==k1):
       k= str(random.randint(1000,b))#如果重了，再随机
    k1=k
    image = Image.open("pics/"+k+".jpg")#随机打开头像
    im2=image.resize((170,145))#调整头像大小
    im = ImageTk.PhotoImage(im2)#插入头像
    canva.create_image(70,70,image = im)
def pic_next(event):#下一个头像
    global im,image,im2,canva,k1,k
    canva.delete(im)
    k=int(k)
    if(k<=b-1):
        k=k+1
    else:
        k=1000
    k=str(k)
    image = Image.open("pics/"+k+".jpg")
    im2=image.resize((170,145))
    im = ImageTk.PhotoImage(im2)
    canva.create_image(70,70,image = im)
def pic_prev(event):#上一个头像
    global im,image,im2,canva,k1,k
    k=int(k)
    canva.delete(im)
    if(k>=1001):
        k=k-1
    else:
        k=b
    k=str(k)
    image = Image.open("pics/"+k+".jpg")
    im2=image.resize((170,145))
    im = ImageTk.PhotoImage(im2)
    canva.create_image(70,70,image = im)
def smile(event):#微笑表情函数
    et4.insert(tkinter.END,'^9000^')
def sad(event):#悲伤表情函数
    et4.insert(tkinter.END,'^9001^')
def begging(event):#求求 表情函数
    et4.insert(tkinter.END,'^9002^')
def bad_smile(event):#坏笑表情插入函数
    et4.insert(tkinter.END,'^9003^')
def angry(event):#愤怒表情插入函数
    et4.insert(tkinter.END,'^9004^')
def dizzy(event):#困 表情插入函数
    et4.insert(tkinter.END,'^9005^')
def shuai(event):#衰 表情插入函数
     et4.insert(tkinter.END,'^9006^')
def relax(event):#放松表情插入函数
    et4.insert(tkinter.END,'^9007^')
def pen(event):#喷 表情插入函数
    et4.insert(tkinter.END,'^9008^')
def file_send(event):#定义文件发送函数
    global ab,ammount,address#全局变量，防止未定义情况出现
    root2=tkinter.Tk()
    root2.title("准备发送")#题目
    root2['background']='lightblue'#背景色
    root2.geometry('180x60+150+150')
    address=str(t2.curselection())[1]
    def confirm(event):#确认对话框
        global address,host,dk,data#全局变量，防止未定义情况出现
        time.sleep(0.4)
        data='Iwanttosendsomething'#秘钥
        sock.sendto(data.encode(),(host,dk))
        sock.sendto(address.encode(),(host,dk))
        root2.destroy()#关闭此窗口
    def destroy(event):#定义关闭函数
        time.sleep(0.4)
        root2.destroy()
    lb1=ttk.Label(root2,text='确认向对方传输文件？')#label 提示语
    lb1.place(x=30,y=0)
    btq=ttk.Button(root2,width=4,text='确定')#确定按钮
    btq.bind("<Button-1>",confirm)
    btq.place(x=30,y=30)
    btq2=ttk.Button(root2,width=4,text='取消')#取消按钮
    btq2.bind("<Button-1>",destroy)
    btq2.place(x=110,y=30)
    root2.mainloop()#窗体循环

image = Image.open("pics/"+k+".jpg")#各组件及其摆放
im2=image.resize((170,145))
im = ImageTk.PhotoImage(im2)
imt=image.resize((20,20))
imt2 = ImageTk.PhotoImage(imt)
frame = tkinter.Frame(root,width=330,height=220)
frame.place(x=0,y=60)
frame2 = tkinter.Frame(root,width=180,height=160)
frame2.place(x=336,y=309)
canva=tkinter.Canvas(root,width=150,height=120)
canva.create_image(70,70,image = im)
canva.place(x=336,y=70)
lb1=tkinter.Label(root,text='IP(192.168.191.1)',background='lightblue',fg='green').place(x = 0,y = 10, anchor = tkinter.NW)
et1 = ttk.Entry(root,width = 20)
et1.bind("<KeyRelease>",get_ip)
et1.place(x = 0,y = 30, anchor = tkinter.NW)
lb2=tkinter.Label(root,text='端口',background='lightblue',fg='green').place(x = 170,y = 10, anchor = tkinter.NW)
et2 = ttk.Entry(root,width = 20)
et2.bind("<KeyRelease>",get_dk)
et2.place(x =170,y =30, anchor = tkinter.NW)
lb3=tkinter.Label(root,text='聊天室',background='lightblue').place(x = 130,y = 52, anchor = tkinter.NW)
lb4=tkinter.Label(root,text='昵称',background='lightblue').place(x=340,y=228)
lb5=tkinter.Label(root,text='当前在线',background='lightblue').place(x=339,y=284)
lb6=tkinter.Label(root,text='添加表情',background='lightblue').place(x=0,y=446)
et3=ttk.Entry(root,width = 20)
et3.bind("<KeyRelease>",get_nm)
et3.place(x = 340,y = 247, anchor = tkinter.NW)
et4 = ttk.Entry(root,width = 47)
et4.bind("<KeyRelease>",get_string)
et4.bind("<KeyPress-Return>",contract)
et4.place(x = 0,y = 471, anchor = tkinter.NW)
et4.config(state='disabled')
t = tkinter.Text(frame,width=45,height=22,cursor='arrow',fg='blue')
t.grid(row=0,column=0)
t2 = tkinter.Listbox(frame2,width=19,height=9,cursor='arrow',fg='red')
t2.grid(row=0,column=0)
t2.bind('<Double-Button-1>',file_send) 
bt1=ttk.Button(root,width=21,text='发送')
bt1.bind("<Button-1>",contract)
bt1.place(x=336,y=468)
bt1.config(state='disabled',cursor="circle")
bt2=ttk.Button(root,width=20,text='连接')
bt2.bind("<Button-1>",receive)
bt2.place(x=335,y=30)
bt3=ttk.Button(root,width=4,text='更改')
bt3.bind("<Button-1>",change)
bt3.place(x=447,y=273)
bt3.config(state='disabled',cursor="circle")
bt4=ttk.Button(root,width=4,text='随机')
bt4.bind("<Button-1>",refresh)
bt4.place(x=397,y=200)
bt5=ttk.Button(root,width=6,text='下一张')
bt5.bind("<Button-1>",pic_next)
bt5.place(x=437,y=200)
bt6=ttk.Button(root,width=6,text='上一张')
bt6.bind("<Button-1>",pic_prev)
bt6.place(x=342,y=200)
image9000 = Image.open("pics/9000.jpg")
imt9000 = ImageTk.PhotoImage(image9000.resize((20,20)))
lb7=tkinter.Label(root,image=imt9000)
lb7.bind("<Button-1>",smile)
lb7.place(x=70,y=445)
image9001 = Image.open("pics/9001.jpg")
imt9001 = ImageTk.PhotoImage(image9001.resize((20,20)))
lb8=tkinter.Label(root,image=imt9001)
lb8.bind("<Button-1>",sad)
lb8.place(x=100,y=445)
image9002 = Image.open("pics/9002.jpg")
imt9002 = ImageTk.PhotoImage(image9002.resize((20,20)))
lb9=tkinter.Label(root,image=imt9002)
lb9.bind("<Button-1>",begging)
lb9.place(x=130,y=445)
image9003 = Image.open("pics/9003.jpg")
imt9003 = ImageTk.PhotoImage(image9003.resize((20,20)))
lb10=tkinter.Label(root,image=imt9003)
lb10.bind("<Button-1>",bad_smile)
lb10.place(x=160,y=445)
image9004 = Image.open("pics/9004.jpg")
imt9004 = ImageTk.PhotoImage(image9004.resize((20,20)))
lb11=tkinter.Label(root,image=imt9004)
lb11.bind("<Button-1>",angry)
lb11.place(x=190,y=445)
image9005 = Image.open("pics/9005.jpg")
imt9005 = ImageTk.PhotoImage(image9005.resize((20,20)))
lb12=tkinter.Label(root,image=imt9005)
lb12.bind("<Button-1>",dizzy)
lb12.place(x=220,y=445)
image9006 = Image.open("pics/9006.jpg")
imt9006 = ImageTk.PhotoImage(image9006.resize((20,20)))
lb13=tkinter.Label(root,image=imt9006)
lb13.bind("<Button-1>",shuai)
lb13.place(x=250,y=445)
image9007 = Image.open("pics/9007.jpg")
imt9007 = ImageTk.PhotoImage(image9007.resize((20,20)))
lb14=tkinter.Label(root,image=imt9007)
lb14.bind("<Button-1>",relax)
lb14.place(x=280,y=445)
image9008 = Image.open("pics/9008.jpg")
imt9008 = ImageTk.PhotoImage(image9008.resize((20,20)))
lb15=tkinter.Label(root,image=imt9008)
lb15.bind("<Button-1>",pen)
lb15.place(x=310,y=445)
s = ttk.Scrollbar(frame)
s.grid(row=0, column=1, sticky='nsew') 
s.config(command=t.yview) 
t.config(yscrollcommand=s.set)
s2 = ttk.Scrollbar(frame2)
s2.grid(row=0, column=1, sticky='nsew') 
s2.config(command=t2.yview) 
t2.config(yscrollcommand=s2.set)
root.mainloop()
root2 = tkinter.Tk()
root2.title('欢迎下次光临')
root2.geometry('300x50+200+200')
root2['background']='lightblue'
def close(event):
    time.sleep(0.3)
    root2.destroy()
lb=tkinter.Label(root2,text='人生苦短，我用PYTHON!',fg='orange').pack()
bt=ttk.Button(root2,text='确定')
bt.bind("<Button-1>",close)
bt.pack()
root2.mainloop()
data='iwanttoleave'
sock.sendto(data.encode(),(host,dk))
