#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

Menu, Tray, Icon,../assests/icon.ico

F1::
    Send, {F1}
    return