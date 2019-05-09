import tkinter

def startService():
    pass

win = tkinter.Tk()
win.title('QQ服务器')
win.geometry('400x400+200+20')
labelIp = tkinter.Label(win,text='ip').grid(row=0,column=0)
labelPort = tkinter.Label(win,text='port').grid(row=1,column=0)
eip = tkinter.Variable()
eport = tkinter.Variable()
entryIp = tkinter.Entry(win,textvariable=eip).grid(row=0,column=1)
entryPort = tkinter.Entry(win,textvariable=eport).grid(row=1,column=1)
button = tkinter.Button(win,text='启动',command=startService).grid(row=2,column=0)

win.mainloop()