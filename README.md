# PasswordManager
A python based password manager which generates a random password and saves the user name and password in a json file. There is a functionality to search for the username and password  for a given website

Steps To Configure:
1. Open the PasswordManager.cmd file and add the configurations.
	a. Set a File Name which will save all the passwords (Add the extension .json at the end of the file name)
	b. Set the Most Common user name and most common website that you want to see preloaded in the app
	c. Save this file and then run this file.
2. After the UI for password manager appears, just click on save and close it.
3. Check whether the file given in the path 1a has been created or not. If not then try again doing step 2 with some random website, username and password.
4. Create a Shortcut for the file PasswordManager.cmd at any suitable place.

Steps to use:
1. Generate and Save a Password:
		1. Double Click on the PasswordManager.cmd
		2. A gui will open, where you can give any website name and user name
		3. Click on Generate Password, which generates a random password. You can generate password multiple times.
		4. The password is automatically copied to the clipboard
		5. Click on save button. And Confirm if all the details are correct
		6. The password is saved correctly

2. Retrieve a password:
		1. Type the Website name and click on "Search"
		2. If the website exists then it will give a popup with the username and password of that website.
		
Caution : All the Three Fields Website , Username and PAssword are all case sensitive
