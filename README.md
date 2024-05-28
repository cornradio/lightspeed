# lightspeed
[README_EN.md](README_EN.md)  
它是一个快捷键工具，可以启动/唤醒程序、打开文件夹，文件，网址，打开配置文件等。   
lightspeed 的名字取自 “[光速启动]( https://powerkeys.github.io/launcher.html)”  

## 一些截图
![image.png](https://img.xwyue.com/i/2024/01/15/65a5264396fdd.png)

![image2.png](https://img2.imgtp.com/2024/05/28/2COIewZa.png)

![image3.png](https://img2.imgtp.com/2024/05/28/8mIiPzhZ.png)

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