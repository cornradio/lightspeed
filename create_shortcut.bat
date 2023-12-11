@echo off
set shortcut_path=%USERPROFILE%\Desktop\lightspeed.lnk
set target_path=%CD%\run.bat
set icon_path=%CD%\assests\icon.ico
set start_in=%CD%

:: 创建 PowerShell 脚本文件
echo $shortcut = (New-Object -ComObject WScript.Shell).CreateShortcut('%shortcut_path%') > CreateShortcut.ps1
echo $shortcut.TargetPath = '%target_path%' >> CreateShortcut.ps1
echo $shortcut.IconLocation = '%icon_path%' >> CreateShortcut.ps1
echo $shortcut.WorkingDirectory = '%start_in%' >> CreateShortcut.ps1
echo $shortcut.Save() >> CreateShortcut.ps1

:: 运行 PowerShell 脚本创建快捷方式
powershell.exe -ExecutionPolicy Bypass -File CreateShortcut.ps1

:: 删除临时 PowerShell 脚本文件
del CreateShortcut.ps1