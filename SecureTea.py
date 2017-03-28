# untuk mendeteksi gerakan mouse dan posting di Twitter
import struct
import sys
import time

# Jika belum terinstal, silahkan men-download & install paket twitter dari
# https://pypi.python.org/pypi/twitter
from twitter import *

debug = 1

API_KEY = 'XXXX'
API_SECRET = 'XXXX'
ACCESS_TOKEN = 'XXXX'
ACCESS_TOKEN_SECRET = 'XXXX'
twitter_username = 'XXXX'

localtime = time.asctime( time.localtime(time.time()) )
auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
twitter = Twitter( auth=auth)
welcome_msg = "\nWelcome to SecureTea..!! Initializing System @ " +localtime
print ( welcome_msg )
twitter.direct_messages.new(user=twitter_username,text=welcome_msg  )

file = open( "/dev/input/mice", "rb" )

def getMouseEvent():
	file = open( "/dev/input/mice", "rb" )
	buf = file.read(3)
	button = ord( buf[0] )
	bLeft = button & 0x1
	bMiddle = ( button & 0x4 ) > 0
	bRight = ( button & 0x2 ) > 0
	x,y = struct.unpack( "bb", buf[1:] )
	file.close();
	return x,y


alert_count = 1
posx = 0
posy = 0
while( 1 ):
	x,y = getMouseEvent()
	posx =  posx + x
	posy =  posy + y

	# Ini harus up to date, ketika mouse bergerak bahkan sedikit
	if ( debug == 1 ) :
		print posx , posy

	# Laptop diakses seseorang dengan menggerakkan mouse/touchpad
	if ( posx>100 or posy>100 or  posx < -100 or posy < -100 ) :
		localtime = time.asctime( time.localtime(time.time()) )

		msg = 'Alert(' + str( alert_count ) + ') : Someone has access your laptop when ' + localtime

		# Menunjukkan msg peringatan pada console
		if ( debug == 1) :
			print msg

		# Kirim pesan peringatan melalui akun twitter
		twitter.direct_messages.new(user=twitter_username,text=msg )

		# Reset / Update counter untuk pergerakan selanjutnya.
		posx = 0
		posy = 0
		alert_count = alert_count + 1

		# Tunggu 10 detik, untuk menghindari terlalu banyak Pesan peringatan
		if ( debug == 1) :
			print ("The program will sleep for 10 seconds")

		time.sleep(10)

		# Siap untuk memantau pergerakan selanjutnya
		if ( debug == 1 ) :
			print ( "Ready to monitor further movement .. !!" )


print ( "End of program")
