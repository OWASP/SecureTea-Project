# SecureTea- How to use TELEGRAM for receiving notification.

### Hello, Today I'll tell you how to use SecureTea with Telegram. The OWASP SecureTea Project is an application designed to help secure a person's laptop or computer / server with IoT (Internet Of Things) and notify users (via various communication mechanisms), whenever someone accesses their computer / server.I will help you to install and use securetea with telegram in this session but first make sure you have installed angular and python and have a telegram account already.Let's get started.

-   Part A: Getting Telegram tokens
you need to create a bot in order to get api keys

visit https://my.telegram.org/auth

-   Part B: Creting a telegram bot and userid

search for "Botfather" and make a bot.
get the bot token and store it somewhere

token = yourtoken
we need this for later steps

search for "userinfobot" and get your user id

userid = youruserid
this will be used later

-   Part C: Installing SecureTea

 -   open terminal

 -   git clone https://github.com/OWASP/SecureTea-Project.git

 -   cd SecureTea-Project

 -   sudo python setup.py install

 -   pip install -r requirements.txt


-   Part D: Running SecureTea with telegram 

 -   sudo SecureTea.py --telegram

Done.

In case of any help needed, please head over to https://github.com/OWASP/SecureTea-Project and 
ask for help. We will respond ASAP.
