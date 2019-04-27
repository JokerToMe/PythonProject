import win32gui,win32con,time

while True:
    qqWin = win32gui.FindWindow('TXGuiFoundation','QQ')
    win32gui.ShowWindow(qqWin,win32con.SW_HIDE)
    time.sleep(1)
    win32gui.ShowWindow(qqWin,win32con.SW_SHOW)
    time.sleep(1)