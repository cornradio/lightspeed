#Persistent

Menu, Tray, NoStandard ; remove default tray menu entries
Menu, Tray, Add, Floder, OnShowFloder 
Menu, Tray, Add, 0 , OnShowFloder 
Menu, Tray, Add, 1 ,  OnShowFloder
Menu, Tray, Add, 2 ,  OnShowFloder
Menu, Tray, Add, 3 ,  OnShowFloder
Menu, Tray, Add, 4 ,  OnShowFloder
Menu, Tray, Add, 5 ,  OnShowFloder
Menu, Tray, Add, 6 ,  OnShowFloder
Menu, Tray, Add, 7 ,  OnShowFloder
Menu, Tray, Add, 8 ,  OnShowFloder
Menu, Tray, Add, 9 ,  OnShowFloder
Menu, Tray, Add, Exit, Exit ; add another tray menu entry


Exit() {
    ExitApp
}

OnShowFloder(mydir){
    basedir := "C:\lightspeed\"
    If (mydir = "Floder")
        Run, explorer %mydir%
    else{
        mydir := basedir . mydir
        Run, explorer %mydir%
    }
}