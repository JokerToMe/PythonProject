# 进程模块
import win32process

import win32gui,win32con,win32api
# c语言模块
import ctypes

processAllAccess = (0x000F0000|0x00100000|0xFFF)
# 找窗体
win = win32gui.FindWindow('TXGuiFoundation','TIM')
# 根据窗体找到进程号
hid, pid = win32process.GetWindowThreadProcessId(win)
# 以最高权限打开进程
p = win32api.OpenProcess(processAllAccess,False,pid)

data = ctypes.c_long()
# 加载内核模块
md = ctypes.windll.LoadLibrary(r'C:\Windows\System32\kernel32')
# 读取内存
md.ReadProcessMemory(int(p))