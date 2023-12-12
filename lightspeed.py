import os
import keyboard
import subprocess
import json
import pyautogui
import time
from console_color_writer import *
from datetime import datetime
from plyer import notification
from playsound import playsound


class lightspeed_obj:
    def __init__(self, title, path, hotkeystr):
        self.title = title
        self.hotkeystr = hotkeystr
        self.hotkey = self.set_hotkey()
        # initpath
        if config_data['folder_root_path'] == "":
            self.path = os.getcwd() + "\\" + path
        else:
            self.path = path

    def start_program(self):
        '''打开程序'''
        try:
            creation_flags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP |subprocess.CREATE_BREAKAWAY_FROM_JOB
            # subprocess.STARTUPINFO
            subprocess.Popen(self.path, shell=True, creationflags=creation_flags,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # subprocess.Popen(self.path, shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # os.startfile(self.path)
            # process = subprocess.Popen(self.path, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            print_red("start_program",e)
            pass

    def open_or_activate(self):
        '''打开或激活窗口'''
        show_notification(self.hotkeystr,self.title)
        play_sound()
        windows = pyautogui.getWindowsWithTitle(self.title)
        if len(windows) > 0:
            for window in windows:
                window.minimize()
                window.restore()
        else:
            self.start_program()
    def myopen(self):
       self.open_or_activate()
       print_green(f"\r{datetime.now().strftime(time_format)}",f"{self.hotkeystr} -- open or activate [{self.title}]")
                        
    
    def set_hotkey(self):
        print_yellow(f"{self.hotkeystr}",f"{self.title}")
        return keyboard.add_hotkey(self.hotkeystr,self.myopen)

    def __str__(self):
        return f"lightspeed_obj: {self.name} {self.path} {self.hotkeystr}"

# config--------------------------------------------------------------------------------

config_path = "assests\\config.json"
config_data = {
    "folder_root_path": "",
    "open_floder_key": "enter",
    "notifiction": "on",
    "auto_hide": "on",
    "playsound": "off",
    "soundeffect": "effect2.wav",
    "reload_key": "ctrl+f12",
    "open_config_key": "ctrl+shift+f12",
}

def try_create_config():
    '''尝试创建配置文件,仅在第一次运行时创建'''
    try:
        with open(config_path, encoding='utf-8') as file:
            tmp = json.load(file)
    except FileNotFoundError:
        with open(config_path, "w", encoding='utf-8') as file:
            json.dump(config_data, file, indent=4)
            print("created config.json")

def check_config():
    '''检查配置文件'''
    global config_data
    
    with open(config_path, encoding='utf-8') as file:
        json_config = json.load(file)
        for k,v in config_data.items():
            if k not in json_config:
                print_red("Config Error",f"missing {k}")
                print_red("example",f'"{k}": "{v}"')
                print_red("try remove assests/config.json")
                exit()
        

def load_json_config():
    '''加载配置文件'''
    try_create_config()
    global config_data
    with open(config_path, encoding='utf-8') as file:
        json_config = json.load(file)
        check_config()
        config_data.update(json_config) # 更新配置文件


# --------------------------------------------------------------------------------


lightspeed_obj_list = []
first_run = True
time_format = "%Y-%m-%d %H:%M:%S"
datetime.now().strftime(time_format)


def create_folder(key):
    '''创建文件夹（初始化函数）'''
    folder_path = config_data['folder_root_path'] + key
    os.makedirs(folder_path, exist_ok=True)
    # print("已经创建文件夹 "+folder_path)

def handle_hotkey_number_enter(name):
    '''# 快捷键 数字 + enter 事件处理'''
    key = name
    print_green(f"\r{datetime.now().strftime(time_format)} ",f"{key}+{config_data['open_floder_key']} -- open folder [{config_data['folder_root_path']+key}]")
    open_folder(config_data['folder_root_path']+key)

def open_folder(folder_path):
    '''打开文件夹'''
    show_notification("open folder",folder_path)
    play_sound()
    # windows = gw.getWindowsWithTitle(folder_path)
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
    folderpath = os.path.join(config_data['folder_root_path'], name)
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
        keyboard.add_hotkey(f"{key}+{config_data['open_floder_key']}", handle_hotkey_number_enter , args=[f"{key}"])# 快捷键 数字 + enter 事件处理
    print_cyan("-"*22+f"[end]"+"-"*22)

def reload_all():
    load_json_config()
    loop_add_hotkey()
    keyboard.add_hotkey(config_data['reload_key'], reload_all) # 重载快捷键
    keyboard.add_hotkey(config_data['open_config_key'], open_folder , args=[f"{os.getcwd()}\\{config_path}"]) # 打开config快捷键
    
    
    print_white("reload:",f"{config_data['reload_key']}")
    print_white("edit config:",f"{config_data['open_config_key']}")
    play_sound()

def hide_window():
    '''隐藏窗口'''
    if config_data['auto_hide'] == 'on':
        try:
            # 等待一段时间，确保窗口已经打开
            time.sleep(0.1)
            # 获取当前窗口的位置和大小
            window = pyautogui.getWindowsWithTitle('lightspeed.py')[0]
            # 模拟按下窗口最小化按钮
            window.minimize()
        except Exception as e:
            print_red("hide_window",e)
            pass

def check_if_running():
    window = pyautogui.getWindowsWithTitle('lightspeed.py')
    if len(window) > 1:
        print_yellow_tag("info","another lightspeed.py might running")
        x = input(' sure you want to run this? [y/n]')
        if x == 'y' or x =="":
            return
        else:
            exit()
# notify --------------------------------------------------------------------------------

def show_notification(title,message):
    if config_data['notifiction'] == 'on':
        notification.notify(
            title=title,
            message=message,
            app_name='lightspeed.py',
            app_icon='',
            timeout=0.3,
        )
        
def play_sound():
    try:
        if config_data['playsound'] == 'on':
            sound_file=f"{os.getcwd()}\\assests\\"+config_data['soundeffect']
            playsound(sound_file)
    except Exception as e:
        print_red("play_sound",e)
        pass

# --------------------------------------------------------------------------------

if __name__ == "__main__":
    check_if_running()
    reload_all()
    first_run = False
    hide_window()
    # keyboard.add_abbreviation("11", "john@stackabuse.com")
    # 监听快捷键事件
    ticker = 0
    ticker2 = 0
    while True:
        time.sleep(0.1)
        ticker += 1
        if ticker% 6 == 0:
            ticker2 += 1
            print("\r key waiting"+str("."*(ticker2%3+1)+" "*5),end="")
            # print("\r "+"-"*(ticker2%45)+f"[{str(ticker2%60).zfill(2)}]"+"-"*(45-ticker2%45),end="")
    keyboard.wait()
