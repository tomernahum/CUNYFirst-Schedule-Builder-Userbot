

# CUNYFirst Schedule Builder Userbot to automatically try to register for classes
Simple script that uses selenium to automatically use the CUNYFirst Schedule Builder tool on your behalf to try registering for a schedule every 120 seconds so that you get in to any empty seats that arise in that class before anyone else.
Use at your own risk

Usually there are waitlists which make this program not needed (unless you're trying to get on the end of a waitlist), but sometimes they close all the waitlists for some reason, which is what happened when I wrote this.

I didn't want to make this but I had to because it's like nuclear armament - what if the other side already has this them? Same with this tool.

# How to Use
1) Go to cunyfirst schedule builder and select your schedule that you wan't this bot to autoregister for
2) Click the "save as favorite" button
3) Note the name of your saved favorite in the favorites tab

.

4) Download the code
5) Rename secrets_and_config.py.example to secrets_and_config.py
6) edit the secrets_and_config.py to include your username and password, and the name of your desired schedule
   
.

7) Navigate to this folder in the command terminal
8) install the right packages, I'm using pipenv
   1) install pipenv by running `pip install --user pipenv`
   2) install the dependencies by running `pipenv install` while in the code directory
9) Run the code
   1)  If using pipenv run the command  `pipenv run python main.py` or `pipenv run python3 main.py`

.

10) Leave the code running until your classes are all signed up for or you're done. 
11) Periodically check cunyfirst yourself to see if you have signed up for the classes and then stop the program (no automatic stopping yet)
12) Exit the program by pressing control+C on the terminal

I am not responsible if cunyfirst bans your ip or something like that. Use at your own risk.

.

please note that the userbot basically breaks if your internet is being really slow, but it will keep attempting to sign up every interval.

note that I did not reasearch how selenium actually works before writing this, I just tried to get something made quickly, so don't judge me too hard for the quality. It also only works 90% of the time but it runs every X seconds so it evens out
