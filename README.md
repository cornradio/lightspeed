# lightspeed
for english reader , please check [README_EN.md](README_EN.md)

它是一个快捷键工具，可以启动/唤醒程序、打开文件夹，文件，网址，打开配置文件等。

lightspeed 的名字取自 “光速启动” 灵感来源于另一个快捷键工具。

## 使用方法

- 安装[ ahk v1 ](https://www.autohotkey.com/download/ahk-install.exe)
- 下载 [release/lightspeed.exe](https://github.com/cornradio/lightspeed/releases/) 解压到任意目录，双击运行



## 使用技巧
- 程序会自动生成 1-9 文件夹
- 鼠标点击任务栏/桌面，然后使用快捷键，没有快捷键就拖一些快捷方式到 1-9 文件夹，使用哲学看[这里](https://powerkeys.github.io/launcher.html)
- 快捷键可以自定义，比如中文名的快捷方式，改成，比如 `[w]微信`会分配快捷键 w ,否则会不分配任何快捷键，英文的快捷方式，会自动分配快捷键为首字母

---

- 用 1-9 + enter 打开文件夹 1-9 
- 在config中可以自定义文件夹位置
- 一个文件夹中有重复的快捷键，会报错
- 在命令行界面按下 enter 可以快速重载
- 配置好 windows terminal 的 外观 - 最小化时通知区域隐藏终端 可以自动隐藏命令行界面
 
## 一些截图
![image0.png](https://img.xwyue.com/i/2024/01/15/65a52639efb9f.png)
![image-1.png](https://img.xwyue.com/i/2024/01/15/65a5263bb336c.png)
![image.png](https://img.xwyue.com/i/2024/01/15/65a5264396fdd.png)


## 为什么要做这个工具
因为 我是一个快捷键狂热爱好者   `:)`

市面上大多数快捷键启动程序只有**启动**的功能，没有“**唤醒**”的功能 （唤醒就是，如果程序已经打开，将程序窗口展示出来，而不开启新的程序实例）

唯一我找到拥有**唤醒**功能的就是[光速启动](https://powerkeys.github.io/launcher.html)，光速启动，里面除了启动这功能之外还有不少功能，但我不使用，有的功能占用了空格键。打游戏时还要切换游戏模式非常不方便，并且光速启动需要占用空格键。

所以我做了这个工具，相当于简化版的“[光速启动](https://powerkeys.github.io/launcher.html)”。

## 实现
这个工具是用 python 写的，使用 python 创建、读取文件夹、配置文件等。并且生成一个 ahk 脚本；ahk 脚本负责监听快捷键，打开程序、文件夹、文件、网址等；并且监听程序窗口的标题，实现**唤醒**功能。
**唤醒** 的功能也是通过ahk的标题匹配实现的

so，这个工具需要 python 和 ahk。

幸运的是,目前我已经把这个工具打包成了 exe 文件，所以不需要安装 python 也可以使用，但是仍然需要自行安装 ahk v1。