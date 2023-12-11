import os
import keyboard
import subprocess
import pygetwindow as gw
import json
from console_color_writer import *
from datetime import datetime
import pyautogui
import time

class lightspeed_obj:
    def __init__(self, title, path, hotkeystr):
        self.title = title
        self.path = path
        self.hotkeystr = hotkeystr
        self.hotkey = self.set_hotkey()

    def start_program(self):
        '''打开程序'''
        # os.popen(self.path) # 会阻塞主进程
        subprocess.Popen(self.path, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
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
       print_green(f"{datetime.now().strftime(time_format)}",f"{self.hotkeystr} -- open or activate [{self.title}]")
                        
    
    def set_hotkey(self):
        print_yellow(f"{self.hotkeystr}",f"{self.title}")
        return keyboard.add_hotkey(self.hotkeystr,self.myopen)

    def __str__(self):
        return f"lightspeed_obj: {self.name} {self.path} {self.hotkeystr}"

# --------------------------------------------------------------------------------

global lightspeed_obj_list 
global folder_root_path 
global first_run 

lightspeed_obj_list = []
folder_root_path = f"c:\\quick_keys\\"
folder_root_path = f""
first_run = True
time_format = "%Y-%m-%d %H:%M:%S"
datetime.now().strftime(time_format)


def create_folder(key):
    '''创建文件夹（初始化函数）'''
    folder_path = folder_root_path + key
    os.makedirs(folder_path, exist_ok=True)
    # print("已经创建文件夹 "+folder_path)

def handle_hotkey_number_enter(name):
    '''# 快捷键 数字 + enter 事件处理'''
    key = name
    print_green(f"{datetime.now().strftime(time_format)} ",f"{key}+enter -- open folder [{folder_root_path+key}]")
    open_folder(folder_root_path+key)

def open_folder(folder_path):
    '''打开文件夹'''
    windows = gw.getWindowsWithTitle(folder_path)
    # if folder_path == "0":
    #     subprocess.run(['explorer', folder_path]) # 本来打算如果开启1的时候就强制打开。因为很多界面名字都叫1，可能需要让文件夹改名
    # elif len(windows) > 0:
    #     for window in windows:
    #         window.minimize()
    #         window.restore()
    # else:
    subprocess.run(['explorer', folder_path])

def load_folder_hotkey(name):
    '''加载文件夹内快捷方式快捷键'''
    folderpath = os.path.join(folder_root_path, name)
    files = os.listdir(folderpath)
    if len(files) > 0:
        print_cyan("-"*23+f"[{name}]"+"-"*23)
    for file in files:
        # if file.endswith('.lnk'):
        filepath = os.path.join(folderpath, file)
        if file[0].upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ[]':
            hotkey = f'{name}+' + file[0].upper()
        else:# 如果有中文（不支持添加快捷键）
            print_red('nope',file)
            continue
            # hotkey = f'{name}+' + '/' #file[0].upper()
        title = file.replace('.lnk', '').replace(' - 快捷方式', '').replace(' - 副本', '') # todo needed english version 
        #  custom hotkeys like add [Q]
        if file.startswith('['):
            hotkey =  f'{name}+'+ file[1].upper()
            file = file[3:]
        lightspeed_obj_list.append(lightspeed_obj(title, filepath, hotkey))

def loop_add_hotkey():
    '''循环添加快捷键'''
    if first_run:
        print("loading...")
    else:
        keyboard.remove_all_hotkeys()
        # for lightspeed_obj in lightspeed_obj_list:
        #     keyboard.remove_hotkey(lightspeed_obj.hotkey)
        #     lightspeed_obj = None
        lightspeed_obj_list.clear()
        print_red("reloading...")
        
    for key in range(1, 10):
        
        create_folder(f"{key}")# 创建文件夹初始化
        load_folder_hotkey(f"{key}")# 加载文件夹内快捷方式快捷键
        keyboard.add_hotkey(f"{key}+enter", handle_hotkey_number_enter , args=[f"{key}"])# 快捷键 数字 + enter 事件处理
    print_cyan("-"*22+f"[end]"+"-"*22)
    keyboard.add_hotkey(f"ctrl+f12", loop_add_hotkey) # 重载
    
    
def load_json_config():
    '''加载配置文件'''
    try:
        with open("config.json", encoding='utf-8') as file:
            config_data = json.load(file)
    except FileNotFoundError:
        config_data = {
            "folder_root_path": "",
            "hint": "you can define folder_root_path , like c:\\quick_keys\\, or leave it empty"
        }
        with open("config.json", "w", encoding='utf-8') as file:
            json.dump(config_data, file, indent=4)
            print("created config.json")
        
    json_config = json.loads(open("config.json", encoding='utf-8').read())
    folder_root_path = json_config["folder_root_path"]


def hide_window():
    '''隐藏窗口'''
    try:
        # 等待一段时间，确保窗口已经打开
        time.sleep(1)
        # 获取当前窗口的位置和大小
        window = pyautogui.getWindowsWithTitle('lightspeed.py')[0]
        # 模拟按下窗口最小化按钮
        window.minimize()
    except Exception as e:
        print_red("hide_window",e)
        pass
    
# --------------------------------------------------------------------------------

if __name__ == "__main__":
    load_json_config()
    loop_add_hotkey()
    first_run = False
    hide_window()
    # keyboard.add_abbreviation("11", "john@stackabuse.com")
    # 监听快捷键事件
    keyboard.wait()
