import os
import shutil
'''
这段代码的功能是
检测文件夹 icons 中的 1.ico 2.ico ... 文件 
将它们设置为文件夹的图标
'''
def set_folder_icon(folder_name, icon_path):
    desktop_ini_path = os.path.join(folder_name, 'desktop.ini')
    # 如果 desktop.ini 存在，先删除
    if os.path.exists(desktop_ini_path):
        os.remove(desktop_ini_path)
    
    desktop_ini_content = f'''[.ShellClassInfo]
IconResource={icon_path},0
'''
    temp_ini_path = os.path.join(folder_name, 'temp_desktop.ini')

    # 写入临时 desktop.ini 文件
    with open(temp_ini_path, 'w') as f:
        f.write(desktop_ini_content)

    # 移动临时 desktop.ini 到最终位置
    shutil.move(temp_ini_path, desktop_ini_path)

    # 设置 desktop.ini 文件为隐藏和系统文件
    os.system(f'attrib +h +s "{desktop_ini_path}"')

    # 设置文件夹为系统文件夹
    os.system(f'attrib +s "{folder_name}"')


def main():
    current_dir = os.getcwd()
    icons_folder = os.path.join(current_dir, 'icons')
    mylist = list(range(11))
    mylist.append("icons")
    for i in mylist:
        folder_name = os.path.join(current_dir, str(i))
        icon_name = f'{i}.ico'
        icon_path = os.path.join(icons_folder, icon_name)

        if os.path.isdir(folder_name) and os.path.isfile(icon_path):
            set_folder_icon(folder_name, icon_path)
        else:
            print(f"Folder or icon not found: {folder_name}, {icon_path}")
    

if __name__ == "__main__":
    main()
    print("task complete,maybe you should without your computer to make it work")
