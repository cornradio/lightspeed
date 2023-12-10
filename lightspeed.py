import os
import keyboard
import subprocess
import pygetwindow as gw
from pylnk3 import Lnk

lightspeed_obj_list = []
folder_root_path = f"c:\\quick_keys\\"
first_run = True

class lightspeed_obj:
    def __init__(self, title, path, hotkey):
        self.title = title
        self.path = path
        self.hotkey = hotkey
        self.set_hotkey()

    def start_program(self):
        '''打开程序'''
        os.popen(self.path)
        
    def open_or_activate(self):
        '''打开或激活窗口'''
        windows = gw.getWindowsWithTitle(self.title)
        if len(windows) > 0:
            for window in windows:
                window.minimize()
                window.restore()
        else:
            self.start_program()

    def myopen(self):
       self.open_or_activate()
       print(f"按下了快捷键：{self.hotkey}")
                        

    def set_hotkey(self):
        self.hotkey = self.hotkey
        keyboard.add_hotkey(self.hotkey,self.myopen)
        print(f'hotkey: {self.hotkey}\n title: {self.title}\n path: {self.path}\n')

    def __str__(self):
        return f"lightspeed_obj: {self.name} {self.path} {self.hotkey}"



def create_folder(key):
    '''创建文件夹（初始化函数）'''
    folder_path = folder_root_path + key
    os.makedirs(folder_path, exist_ok=True)
    # print("已经创建文件夹 "+folder_path)

def handle_hotkey_number_enter(name):
    '''# 快捷键 数字 + enter 事件处理'''
    key = name
    print(f"按下了快捷键：{key}+enter")
    open_folder(folder_root_path+key)

def open_folder(folder_path):
    '''打开文件夹'''
    subprocess.run(['explorer', folder_path])

def load_folder_hotkey(name):
    '''加载文件夹内快捷方式快捷键'''
    folderpath = os.path.join(folder_root_path, name)
    files = os.listdir(folderpath)
    
    for file in files:
        if file.endswith('.lnk'):
            filepath = os.path.join(folderpath, file)
            hotkey = f'{name}+' + file[0].upper()
            title = file.replace('.lnk', '').replace(' - 快捷方式', '')
            lightspeed_obj_list.append(lightspeed_obj(title, filepath, hotkey))

def loop_add_hotkey():
    '''循环添加快捷键'''
    if first_run:
        print("loading...")
        print("-"*45)
    else:
        keyboard.remove_all_hotkeys()
        print("reloading...")
        print("-"*45)
        
        
    keyboard.add_hotkey(f"1+2+3", loop_add_hotkey) # 重载
    for key in range(1, 10):
        create_folder(f"{key}")# 创建文件夹初始化
        load_folder_hotkey(f"{key}")# 加载文件夹内快捷方式快捷键
        keyboard.add_hotkey(f"{key}+enter", handle_hotkey_number_enter , args=[f"{key}"])# 快捷键 数字 + enter 事件处理
        # 清除注册的快捷键


if __name__ == "__main__":
    # 注册全局快捷键
    loop_add_hotkey()
    first_run = False
    
    
    # 监听快捷键事件
    # keyboard.add_abbreviation("11", "john@stackabuse.com")
    keyboard.wait()
