import pyautogui
import time

# 等待一段时间，确保窗口已经打开
time.sleep(2)

# 获取当前窗口的位置和大小
window = pyautogui.getWindowsWithTitle('lightspeed.py')[0]

# 模拟按下窗口最小化按钮
window.minimize()
