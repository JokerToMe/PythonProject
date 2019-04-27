import win32gui,win32con,random

# 参数1：控制的窗体
# 参数2：大致方向 HWND_TOPMOST：上方
# 参数3：位置x
# 参数4：位置y
# 参数5：长度
# 参数6：宽度

while True:
    x = random.randrange(900)
    y = random.randrange(600)
    qqWin = win32gui.FindWindow('TXGuiFoundation','QQ')
    win32gui.SetWindowPos(qqWin,win32con.HWND_TOPMOST,x,y,300,300,win32con.SWP_SHOWWINDOW)