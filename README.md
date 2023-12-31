# lightspeed
lightspeed is a `hotkey launcher` written in python.

Put shortcuts in quick floders 1~9 (quick floders will generate by first run)

![Imgur](https://i.imgur.com/4OSyWob.png)

Use short cut when on desktop or task bar ~

![Imgur](https://i.imgur.com/PiBOKGX.png)

---


things behind： `lightspeed.py` will regenerate `lightspeed.ahk` , ahk handle the hotkeys

![Imgur](https://i.imgur.com/lj1ZFxH.png)

---



After first start , program will create quick floders 1~9;

Use `1~9`+ `enter` hotkey to open quick floders , and alt+drag any shourtcut in "quick floder". 

Then restart `lightspeed.py` , now you can try hotkeys.

![Imgur](https://i.imgur.com/aeDuuGW.png)

# how to use
1. install [python 3](https://www.python.org/downloads/)  and [autohotkey v1](https://www.autohotkey.com/)
2. install python packages using ：`pip install -r requirements.txt`
3. run `py lightspeed.py` , will generate `lightspeed.ahk` and auto run it.

# Hints

`create_shortcut.bat` can help u create a desktop shortcut .

Highly recommand u use different floders for different purpose , like 1 for chatting , 2 for tools , 3 for files etc.

after update , python go stuck may cause of `assests\config.json` not right , delete it.


##  change the hotkey

e.g. `1 + c` to open chrome , 

change `chrome.lnk` to`[x]chrome.lnk` , then you can use `1 + X` to open chrome now

other hotkey like `ctrl + shift + f12` to open config file , can be change in `assests\config.json`

## config

script will auto generated `assests\config.json`  at first run 

edit config in vscode and restart will take effects 

```
{
    "folder_root_path": "",
    "notifiction": "off",
    "auto_hide": "off",
    "open_floder_key": "enter",
    "reload_key": "ctrl+f12",
    "open_config_key": "ctrl+shift+f12"
}
```

