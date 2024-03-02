Remove-Item -Path .\dist\* -Recurse -Force
pyinstaller  --exclude=pyinstaller --exclude=pandas --exclude=numpy --exclude=libcrypto --exclude=PIL --onefile --icon=assests\icon.ico  lightspeed.py
xcopy  assests\icon.ico dist\assests\ /y
# //compress \dist\lightspeed to lightspeed.zip using pwsh
Compress-Archive -Path .\dist\ -DestinationPath .\lightspeed_vx.x.zip -Force