import win32gui
# import win32api
import pyautogui
import time
# from pymouse import PyMouse
hwnd_title = {}

def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd) and
        win32gui.IsWindowEnabled(hwnd) and
        win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)


for h, t in hwnd_title.items():
    if t :
        print(h, t)
        if t == '无慕等5个会话':
            left, top, right, bottom = win32gui.GetWindowRect(h)
            print(left,top,right,bottom)
            num = 0
            while 1 :
                num += 1
                print("点击完成")

                pyautogui.click(right-206,bottom-31)
                time.sleep(10)
                if num > 3:
                    break


            