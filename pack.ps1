pyinstaller --exclude=pandas --exclude=numpy --exclude=libcrypto --exclude=PIL --onefile --icon=assests\icon.ico  lightspeed.py
# //copy assests to dist
xcopy assests dist\assests\ /e /y
xcopy README.md dist\ /e /y
# //compress \dist\lightspeed to lightspeed.zip using pwsh
Compress-Archive -Path .\dist\ -DestinationPath .\lightspeed.zip -Force