# lightspeed
lightspeed is a `hotkey launcher` written in python

 (inspired by Power Keys: https://powerkeys.github.io/)

only support windows 

the key feature is `speed` and  `wakeup`, wake up the program if it's already running , or open it if it's not running.  

## install
requirements
```
pip install -r requirements.txt
```
run ( run in unimportant floder , script will create floders and config file 😥) 
```
python lightspeed.py
```

after testing , `create_shortcut.bat` can help u create a desktop shortcut . 

and you can put the shortcut in `shell:startup` to run it at startup .

> icon from https://www.macosicongallery.com/

![Imgur](https://i.imgur.com/oVTExMh.png)

## quick start

1. `1 ~ 9 + enter` to open the lightspeed folder 
2. put whatever you want in the folder , then reload hotkey ,
3. now you can open it with `1 ~ 9 + first letter` :
4. use `hard reload` when stuck
![Imgur](https://i.imgur.com/aeDuuGW.png)


##  change the hotkey

e.g. `1 + c` to open chrome , 

change `chrome.lnk` to`[x]chrome.lnk` , then you can use `1 + X` to open chrome now

other hotkey like `ctrl + shift + f12` to open config file , can be change in `assests\config.json`

## config

script will auto generated `assests\config.json`  at first run 

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

> config file will be added more features in the future

## speed test
speed is insine ,  i can't even see the window pop up

https://i.imgur.com/vroF1F1.gif

<a href="https://imgur.com/vroF1F1"><img src="https://i.imgur.com/vroF1F1.gif" title="source: imgur.com" /></a>


---

# development

## features 
100% 

- [x] create floders
- [x] create shortcuts for folders 1 ~ 9
- [x] read lnk files and create shortcuts
- [x] reload shortcuts 
- [x] fix stuck problem , still don't know why (fixed , it because my ahk alt Q have a flaw)
- [x] support custom hotkeys like add [Q] to the start of the lnk name to open it with `number + q`
- [x] support config file -- quick input -- quick typer!
- [x] gui for keymap viewing -- i think view it in terminal is just fine 
- [x] fix stuck problem , added os.Popen() flag for start a "real process" , not a "sub process"
- [x] add sound effect when opening -- added , not perfect , I highly recommend you to turn it off
- [x] add visual effect when opening -- added windwos notification
- [x] easy add a desktop icon shortcut using `create_shortcut.bat`

## bugs
- [x] after open `微信` and login , program will stuck -- added `hard reload` function
- [ ] support fucking `\u200b` for ms edge , dude , why microsoft choose this wired utf8 character in title?
- [ ] package and post on **pypi** -- having a infinate loop , why?  

<!-- # upload
> make sure have twine installed first

1. change `setup.py`
2. testing `py setup.py develop`
3. `py setup.py sdist`
4. `twine upload dist/*`33rrrr如1d1d -->