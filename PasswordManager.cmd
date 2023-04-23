@echo off
::start /B "" pyw .\PasswordManager_Improved.py
start /min "" .\dist\PasswordManager_Improved.exe --SAVED_PASSWORDS_FILE_PATH ./file1.txt --MOST_COMMONLY_USED_EMAIL "mypersonalemail.gmail.com"  --STARTING_WEBSITE_TEXT "www.StartingWebsite.com"
::pause
