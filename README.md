# lightspeed
[README_EN.md](README_EN.md)  
它是一个快捷键工具，可以启动/唤醒程序、打开文件夹，文件，网址，打开配置文件等。   
lightspeed 的名字取自 “[光速启动]( https://powerkeys.github.io/launcher.html)”  

## 功能
- 程序会自动生成 1-9 9个快速文件夹
- 鼠标点击任务栏/桌面，然后使用快捷键 1-9 + enter
- 快捷键为 文件夹编号 + 首字母
- 快捷键根据文件名生成，例如：
    - `Google Chrome` > G
    - `[w]微信` > W
    - `腾讯QQ` > none

> 更重要的是程序/文件分类的逻辑。  


## 入门

- 安装[ ahk v1 ](https://www.autohotkey.com/download/ahk-install.exe) 这是程序的依赖
- 打包版：下载exe [release/lightspeed.exe](https://github.com/cornradio/lightspeed/releases/) 
- python 版：下载本项目，安装python依赖，建立桌面快捷方式，运行。
- 非常建议配合 [startsallback](https://www.google.com/search?q=StartAllBack+2024) 一起使用,可以实现 图2 的效果



## 技巧
- 在config中可以自定义文件夹位置
- 在命令行界面按下 enter 可以快速重载
- 配置好 windows terminal 的 外观 - 最小化时通知区域隐藏终端 可以自动隐藏命令行界面
- [最小化到托盘](#最小化到托盘)

## 最小化到托盘的方法
此方法需要使用吗 windows terminal 
- 外观 - 最小化时再通知区域隐藏终端
- 外观 - 始终再通知区域显示图标

## lightspeed-UI
这是一个独立的小ui程序，基于winform编写，调用资源管理器。
可以使用如下ahk代码*快速启动* 使用ctrl alt z 在任何位置启动ui界面。
默认图标效果是list-view ，想要实现如图效果需跑脚本：seticons/icon4floders.py , 相当于把文件夹类型设置为“图片”。
![image](https://github.com/user-attachments/assets/b086c16b-051e-45de-9c89-2c70597b4cf1)


```ahk
; OPEN OR ACTIVATE
ShowAndHideText(text, duration) {
    Gui, +LastFound +AlwaysOnTop -Caption +ToolWindow +Disabled
    Gui, Color, 000000 ; background black
    Gui, Font, s15, Verdana ; fontsize and fontname


    textWidth := 400
    textHeight := 40
    winX := 0
    winY := 20

    Gui, Add, Text, x%winX% y%winY% w%textWidth% h%textHeight% cFFFFFF Center, %text%
    Gui, Show, NA
    WinSet, Transparent, 180 ; 0 is fully transparent, 255 is fully opaque

    SetTimer, DestroyGui, %duration%
    return

    DestroyGui:
    Gui, Destroy
    return
}


open_or_activate(title,path)
{
    SetTitleMatchMode, 2

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
^!z::open_or_activate("ahk_exe lightspeed-UI.exe","lightspeed-UI.exe")
```

