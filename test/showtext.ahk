#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

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

    Sleep, %duration%
    Gui, Destroy
}

F1::
    title := "GPTS.url"
    ShowAndHideText(title, 700)
return