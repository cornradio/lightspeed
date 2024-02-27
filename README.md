# lightspeed
for english reader , please check [README_EN.md](README_EN.md)

它是一个快捷键工具，可以启动/唤醒程序、打开文件夹，文件，网址，打开配置文件等。

lightspeed 的名字取自 “光速启动” 灵感来源于另一个快捷键工具。

## 使用方法

- 安装[ ahk v1 ](https://www.autohotkey.com/download/ahk-install.exe)
- 打包版：下载exe [release/lightspeed.exe](https://github.com/cornradio/lightspeed/releases/) 
- 源码版：pull后使用 create_shortcut.bat 创建快捷方式，使用快捷方式启动

## 功能
- 程序会自动生成 1-9 9个快速文件夹
- 鼠标点击任务栏/桌面，然后使用快捷键 1-9 + enter 打开快速文件夹（文件夹如何用？ 参考[这里](https://powerkeys.github.io/launcher.html)）
- 快捷键可以自定义，比如中文名的快捷方式，改成，比如 `[w]微信`会分配快捷键 w ,否则会不分配任何快捷键，英文的快捷方式，会自动分配快捷键为首字母

## 技巧
- 在config中可以自定义文件夹位置
- 在命令行界面按下 enter 可以快速重载
- 配置好 windows terminal 的 外观 - 最小化时通知区域隐藏终端 可以自动隐藏命令行界面
- [最小化到托盘](#最小化到托盘)

## 图示


![Imgur](https://i.imgur.com/4OSyWob.png)


![Imgur](https://i.imgur.com/PiBOKGX.png)


![Imgur](https://i.imgur.com/lj1ZFxH.png)



 
## 一些截图
![image.png](https://img.xwyue.com/i/2024/01/15/65a5264396fdd.png)

## 最小化到托盘
using win11 + windows terminal , and turn on this setting:
- 外观 - 最小化时再通知区域隐藏终端
- 外观 - 始终再通知区域显示图标

⚠️ for exe user:
you have to make a desktop shortcut of `lightspeed.exe` , and rename it to `lightspeed.py` 

![Imgur](https://i.imgur.com/56q7hSf.png)