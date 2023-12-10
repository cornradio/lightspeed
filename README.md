# lightspeed
lightspeed is a `hotkey launcher` written in python

 (inspired by Power Keys: https://powerkeys.github.io/)



only support windows for now , sorry mac and linux users , i will try to make it cross platform in the future

## install
```
pip install -r requirements.txt
```

use windows `task scheduler` to run the script at startup (choose run with highest privileges if you want)

![Imgur](https://i.imgur.com/zwhjR2g.png)

## Usage

![Imgur](https://i.imgur.com/9wYUkGS.png)

1. `1 ~ 9 + enter` to open the lightspeed folder 
2. `1 ~ 9 + first letter` of the lnk name to open the lnk file (windows shortcut file) , e.g. `1 + c` to open chrome)
3. `ctrl F12` to reload the hotkeys (in case you add new files)
4. just `alt + drag` to create new lnk files, dont change name of the lnk files ,script uses name to decide to reopen or wake up program


## progress 
- [x] create floders
- [x] create shortcuts for folders 1 ~ 9
- [x] read lnk files and create shortcuts
- [x] reload shortcuts 
- [x] fix stuck problem , still don't know why (fixed , it because my ahk alt Q have a flaw)
- [x] support custom hotkeys like add [Q] to the start of the lnk name to open it with `number + q`
- [x] support config file -- quick input -- quick typer!
- [x] gui for keymap viewing -- i think view it in terminal is just fine 
- [ ] 


- [ ] support fucking `\u200b` for ms edge , dude , why ?
- [ ] package and post on **pypi** -- having a infinate loop , why?

<!-- # upload
> make sure have twine installed first

1. change `setup.py`
2. testing `py setup.py develop`
3. `py setup.py sdist`
4. `twine upload dist/*`33rrrr如1d1d -->