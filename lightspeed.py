import os
import subprocess
import json
import pyautogui
import time
from console_color_writer import *
from datetime import datetime


class lightspeed_obj:
    def __init__(self, title, path, hotkeystr):
        self.title = title
        self.hotkeystr = hotkeystr
        # initpath
        if config_data['folder_root_path'] == "":
            self.path = os.getcwd() + "\\" + path
        else:
            self.path = path
        if ',' in self.path: # 兼容 ahk 语法 逗号转义
            self.path = self.path.replace(',','`,')
            
        self.add_hotkey_to_ahk()

    def add_hotkey_to_ahk(self):
        '''添加快捷键到ahk'''
        content = f'''
{self.hotkeystr}::
open_or_activate("{self.title}","{self.path}")
return
'''
        write_ahk(content)
        print_green(f"{self.hotkeystr}",f"{self.title}")

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

    def __str__(self):
        return f"lightspeed_obj: {self.name} {self.path} {self.hotkeystr}"

# config--------------------------------------------------------------------------------

config_path = "assests\\config.json"
config_data = {
    "folder_root_path": "",
    "open_floder_key": "enter",
    "auto_hide": "on",
    "auto_exit": "off",
    "open_config_key_ahk": "^+F12",
}

def try_create_config():
    '''尝试创建配置文件,仅在第一次运行时创建'''
    try:
        with open(config_path, encoding='utf-8') as file:
            tmp = json.load(file)
    except FileNotFoundError:
        # 如果文件夹不存在，创建文件夹
        if not os.path.exists("assests"):
            os.makedirs("assests")

        print("do you want to choose a folder to store your shortcuts?(Y/n)")
        x = input()
        if x == "Y" or x == "y" or x == "":
            print("input the folder path (like C:\lightspeed\):")
            folder_root_path = input()
            config_data['folder_root_path'] = folder_root_path
            with open(config_path, "w", encoding='utf-8') as file:
                json.dump(config_data, file, indent=4)
                print("created config.json - custom folder")
        else:
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



# ahk floder add =-------------------------------

def loop_add_hotkey():
    init_ahk()
    '''循环添加快捷键'''
    print_cyan('''
|o _ |__|_ _._  _  _  _|
||(_|| ||__>|_)(/_(/_(_|
   _|       |           
''')
    for key in range(0, 10):
        create_folder(f"{key}")# 创建文件夹初始化
        if key != 0:
            load_folder_hotkey(f"{key}")# 加载文件夹内快捷方式快捷键
        # 多行字符串
        path = config_data['folder_root_path']
        if config_data['folder_root_path'] == "":
            path = os.getcwd() + "\\" + path
        content = f'''
{str(key)} & {config_data['open_floder_key']}::
Run, "{path+str(key)}" 
ShowAndHideText({str(key)} floder, 600)
return
'''
        write_ahk(content)

    print_cyan("-"*22+f"[end]"+"-"*22)

def load_folder_hotkey(name):
    '''加载文件夹内快捷方式快捷键'''
    folderpath = os.path.join(config_data['folder_root_path'], name)
    files = os.listdir(folderpath)
    if len(files) > 0:
        print_cyan("-"*23+f"[{name}]"+"-"*23)
    for file in files:
        filepath = os.path.join(folderpath, file)
        if file[0].upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ[]':
            hotkey = f'{name} & ' + file[0].lower()
        else:# 如果有中文（不支持添加快捷键）
            print_red('nope',file)
            continue
        if file.startswith('['):
            hotkey =  f'{name} & '+ file[1].lower()
            file = file[3:]
        if file.startswith('【'):
            hotkey =  f'{name} & '+ file[1].lower()
            file = file[3:]
        title = file.replace('.lnk', '').replace(' - 快捷方式', '').replace(' - 副本', '')  
        lightspeed_obj_list.append(lightspeed_obj(title, filepath, hotkey))
        
def init_ahk():
    '''初始化ahk文件'''
    if os.path.exists("lightspeed.ahk"):
        os.remove("lightspeed.ahk")
    content = '''

Menu, Tray, Icon,./assests/icon.ico

#If WinActive("ahk_class Shell_TrayWnd") or WinActive("ahk_class Shell_SecondaryTrayWnd") or WinActive("python  lightspeed.py") or WinActive("ahk_class WorkerW")  or WinActive("ahk_class Progman")

SetTitleMatchMode, 2

ShowAndHideText(text, duration) {
    Gui, +LastFound +AlwaysOnTop -Caption
    WinSet, Transparent, 150 ; 0 is fully transparent, 255 is fully opaque
    ; WinSet, Region, 0-0 %A_ScreenWidth%-0 %A_ScreenWidth%x%A_ScreenHeight%
    
    Gui, Color, 000000 ; 设置背景颜色为黑色
    Gui, Font, s15, Arial ; 设置字体大小为20    
    ; 获取文本的宽度和高度
    textWidth := 400
    textHeight := 40
    winX := 0
    winY := 20
    
    Gui, Add, Text, x%winX% y%winY% w%textWidth% h%textHeight% cFFFFFF Center, %text%
    Gui, Show, NA
    Sleep, %duration%
    Gui, Destroy
}


open_or_activate(title,path)
{
    ShowAndHideText(title, 600)
    if (WinExist(title))
    {
        WinActivate, %title% 
    }
    else
    {
        Run, %path%   
    }
}
'''
    write_ahk(content)


def write_ahk(ahkstr):
    '''写入ahk文件'''
    with open("lightspeed.ahk", "a", encoding='GBK') as file:
        file.write(ahkstr)


def reload_all():
    load_json_config()
    loop_add_hotkey()
    content = f'''
{config_data['open_config_key_ahk']}::
Run, "{os.getcwd()}\\{config_path}"
return
'''
    write_ahk(content)
    print_white("open config:",f"{config_data['open_config_key_ahk']}")

def hide_window():
    '''隐藏窗口'''
    if config_data['auto_hide'] == 'on':
        try:
            # 等待一段时间，确保窗口已经打开
            time.sleep(0.1)
            # 获取当前窗口的位置和大小
            if os.path.exists("lightspeed.py"):
                window = pyautogui.getWindowsWithTitle('lightspeed.py')[0]
            else:
                window = pyautogui.getWindowsWithTitle('lightspeed')[0]
            # 模拟按下窗口最小化按钮
            window.minimize()
        except Exception as e:
            print_red("hide_window",e)
            pass

def click_ok_on_lightspeedahk_popup():
    '''自动点击lightspeed.ahk弹窗的ok按钮'''
    try:
        # 等待一段时间，弹窗窗口已经打开
        time.sleep(0.8)
        # 获取目标窗口的句柄
        window = pyautogui.getWindowsWithTitle('lightspeed.ahk')[0]
        # 切换焦点到目标窗口
        window.minimize()
        window.restore()
        print_green("click_ok_on_lightspeedahk_popup", "click ok")
        # 模拟按下ok按钮
        pyautogui.press('enter')

    except Exception as e:
        print_red("hide_window",e)
        pass

# def check_if_running():
#     window = pyautogui.getWindowsWithTitle('lightspeed.py')
#     if len(window) > 1:
#         print_yellow_tag("info","another lightspeed.py might running")
#         x = input(' sure you want to run this? [y/n]')
#         if x == 'y' or x =="" or x:
#             return
#         else:
#             exit()
            
def runinsubprocess(thing):
    creation_flags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP |subprocess.CREATE_BREAKAWAY_FROM_JOB
    subprocess.Popen(thing, shell=True, creationflags=creation_flags,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def if_not_installed_requirments():
    '''检查是否安装了依赖库'''
    try:
        import pyautogui
        import console_color_writer
    except ModuleNotFoundError:
        print_red("ModuleNotFoundError","please run 'pip install -r requirements.txt'")
        exit()
# --------------------------------------------------------------------------------

if __name__ == "__main__":
    if_not_installed_requirments()
    reload_all()
    first_run = False
    hide_window()
    runinsubprocess("lightspeed.ahk")
    print_green("start ahk", "lightspeed.ahk")
    click_ok_on_lightspeedahk_popup()


    # keyboard.add_abbreviation("11", "john@stackabuse.com")
    # 监听快捷键事件
    while True:
        time.sleep(0.1)
        print_yellow("1. focus on Task Bar/Desktop")
        print_yellow("2. USE HOTKEYS")
        print_yellow("3. floder 0 for any thing(no hotkey)")
        print_yellow("Press Enter to [$reload]")
        if config_data['auto_exit'] == 'on':
            exit()
        x= input()
        if x == "":
            print_cyan("hard reload")
            # 检查是否存在lightspeed.py 如果存在，启动python ，如果不存在 启动exe
            if os.path.exists("lightspeed.py"):
                runinsubprocess("python lightspeed.py")
            else:
                runinsubprocess("lightspeed.exe")
            exit()
        # print("\r key waiting"+str("."*(ticker2%3+1)+" "*5),end="")
        # print("\r "+"-"*(ticker2%45)+f"[{str(ticker2%60).zfill(2)}]"+"-"*(45-ticker2%45),end="")
