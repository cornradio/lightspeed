#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

ShowAndHideText(text, duration) {
    Gui, +LastFound +AlwaysOnTop -Caption
    WinSet, Transparent, 150 ; 0 is fully transparent, 255 is fully opaque
    ; WinSet, Region, 0-0 %A_ScreenWidth%-0 %A_ScreenWidth%x%A_ScreenHeight%
    
    Gui, Color, 000000 ; 设置背景颜色为黑色
    Gui, Font, s15, Arial ; 设置字体大小为20    
    ; 获取文本的宽度和高度
    textWidth := 400
    textHeight := 40
    winX := 0
    winY := 20
    
    Gui, Add, Text, x%winX% y%winY% w%textWidth% h%textHeight% cFFFFFF Center, %text%
    Gui, Show, NA
    Sleep, %duration%
    Gui, Destroy
}

F1::
    title := "GPTS.url"
    ShowAndHideText(title, 600)
return