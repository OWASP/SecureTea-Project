# SecureTea- How to use TWILIO SMS for receiving notification.

### Hello, Today I'll tell you how to use SecureTea with Twilio SMS. The OWASP SecureTea Project is an application designed to help secure a person's laptop or computer / server with IoT (Internet Of Things) and notify users (via various communication mechanisms), whenever someone accesses their computer / server.I will help you to install and use securetea with telegram in this session but first make sure you have installed angular and python and have a telegram account already. Let's get started.

## Part A
Visit https://www.twilio.com/

Log in into your Twillio account( create if don't have any already)

## Part B 

Then visit https://www.twilio.com/console

On the dashboard,Create a project with any name and get

1: Account SID : 
2: Auth Token :
3: Your twilio phone number (you will get a new number on trial basis initially)

## Part C
Goto terminal
change directory where SecureTea files are stored

```sudo SecureTea.py --twilio_sms```

input AUTH TOKEN
then  twilio phone number(make sure its in format)
then your other phone number on which you want to recieve notification alerts.
and finally yout ACCOUNT SID
hit enter

Done.
After a few seconds you will receive SMS notifications from your SecureTea running device.

Here I am gtting message on my number but make sure you dont have dnd.

Thanks.

This happens in case of DND is enabled. So it is working for now. Thanks for following. Bye till the next one.

Thanks for watching. In case of any help-please head over to https://github.com/OWASP/SecureTea-Project and 
ask for help or GIYF.com

to exit...simply close the terminal.

Thats it for today, See you in the next one.
