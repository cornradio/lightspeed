# lightspeed
lightspeed is a `hotkey launcher` written in python

 (inspired by Power Keys: https://powerkeys.github.io/)



only support windows for now , sorry mac and linux users , i will try to make it cross platform in the future

## install
requirements
```
pip install -r requirements.txt
```
run ( run in unimportant floder ,this script will create 9 floders and 1 config file 😥) 
```
python lightspeed.py
```


or use windows `task scheduler` to run the script at startup (choose run with highest privileges if you want)

![Imgur](https://i.imgur.com/zwhjR2g.png)



## quick start

![Imgur](https://i.imgur.com/9wYUkGS.png)

1. `1 ~ 9 + enter` to open the lightspeed folder 
2. `1 ~ 9 + first letter` of the lnk name to open the lnk file (windows shortcut file) , e.g. `1 + c` to open chrome)
3. `ctrl F12` to reload the hotkeys (in case you add new files)
4. just `alt + drag` to create new lnk files, dont change name of the lnk files ,script uses name to decide to reopen or wake up program

## cool
speed is insine ,  i can't even see the window pop up
![Imgur](https://i.imgur.com/vroF1F1.gifv)


##  change the hotkey

you see this is pretty floder based ....
just use `1 ~ 9 + enter` to open the folder , put whatever you want in the folder


e.g. `1 + c` to open chrome , 

change `chrome.lnk` to`[x]chrome.lnk` , then you can use `1 + X` to open chrome now

it's easy to understand


## config

there will be a `config.json` auto generated if not exist, you can change the `folder_root_path` 

but the `config.json`  must be in the program start folder 
```
{
    "folder_root_path": "",
    "hint": "you can define folder_root_path , like c:\\quick_keys\\, or leave it empty"
}
```

> config file will be added more features in the future
> 
> eg . input @@ for emailaddress , or choose a hotkey u want  for input 


## progress 
- [x] create floders
- [x] create shortcuts for folders 1 ~ 9
- [x] read lnk files and create shortcuts
- [x] reload shortcuts 
- [x] fix stuck problem , still don't know why (fixed , it because my ahk alt Q have a flaw)
- [x] support custom hotkeys like add [Q] to the start of the lnk name to open it with `number + q`
- [x] support config file -- quick input -- quick typer!
- [x] gui for keymap viewing -- i think view it in terminal is just fine 
- [ ] more features for config file


- [ ] support fucking `\u200b` for ms edge , dude , why microsoft choose this wired utf8 character in title?
- [ ] package and post on **pypi** -- having a infinate loop , why? can't figure out .

<!-- # upload
> make sure have twine installed first

1. change `setup.py`
2. testing `py setup.py develop`
3. `py setup.py sdist`
4. `twine upload dist/*`33rrrr如1d1d -->