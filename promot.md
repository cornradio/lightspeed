# gpt prompt 

我希望开发一个软件
使用F1~F12键来快速启动快捷方式
1. 按下F1~F12键+enter，启动内置文件夹*如果没有文件夹则创建：c:\quickkeys\F1~F12
2. 实时监控文件夹内的文件，如果有文件则刷新快捷键绑定配置列表
    例如现在 我在F1文件夹内创建了一个快捷方式，名字为：`b百度.lnk`
3. 按下 F1+b 则启动`b百度.lnk`
4. 所有的快捷方式都是可以动态添加的，只要在文件夹内创建快捷方式，快捷键绑定就会重载

1. 使用python开发
按下F1~F12键+enter，启动文件（如果没有文件夹则创建）：文件夹位置为:c:\quick_keys\F1~F12
2. 需要监听全局快捷键，即使没有打开程序 

---

帮助我完成这个函数 ： 
def load_floder_hotkey(name):
    folderpath=folder_root_path+key
    ...

假设 folderpath =  C:\quick_keys\1 
且当前文件夹内有两个快捷方式：
C:\quick_keys\1
    Microsoft Edge.lnk
    notepad.lnk

程序应该动态的绑定快捷键：
    1+M 启动 Microsoft Edge.lnk
    1+N 启动 notepad.lnk

使用 keyboard.add_hotkey 绑定快捷键


=---

已注册快捷键：1+E 打开文件：c:\quick_keys\1\Everything - 快捷方式.lnk
已注册快捷键：1+M 打开文件：c:\quick_keys\1\Microsoft Edge.lnk

# 加载文件夹内快捷方式快捷键
def load_folder_hotkey(name):
    folderpath = os.path.join(folder_root_path, name)
    files = os.listdir(folderpath)
    
    for file in files:
        if file.endswith('.lnk'):
            filepath = os.path.join(folderpath, file)
            hotkey = f'{name}+' + file[0].upper()
            keyboard.add_hotkey(hotkey, lambda: os.startfile('"' + filepath + '"'))
            print(f'已注册快捷键：{hotkey} 打开文件：{filepath}')

但是实际情况会按下快捷键后1+e，打开的是microsoftEdge，而不是everything快捷方式

如何让我的程序可以判断，如果当前edge已经启动，则把窗口唤起，而不是打开新的实例?