# SecureTea
Small IOT (Internet of Things) to notify users via twitter, whenever anyone accessing his laptop. This small application using the touchpad / mouse / wireless mouse and developed in python and tested on a linux (TeaLinuxOS)

Tujuan dari aplikasi ini adalah untuk memperingatkan pengguna (on twitter) setiap kali laptop nya Diakses.
Aplikasi kecil ini dikembangkan dan diuji di python pada mesin linux [TeaLinuxOS](http://tealinuxos.org/) Kemungkinan besar bisa bekerja dengan baik di Raspberry Pi juga.


Target User:
=============

Ini ditulis untuk digunakan oleh siapa saja yang tertarik pada Security IoT (Internet of Things) dan masih perlu pengembangan lagi.

Bagaimana fungsinya :

- Melacak gerakan dari Mouse/Touchpad
- Mendeteksi akses laptop dengan Mouse/Touchpad yang terpasang
- Mengirimkan pesan peringatan pada Twitter


Objective:
===========

Untuk memperingatkan pengguna via twitter, setiap kali laptop-nya telah diakses.


Pre-requisites:
================

I. HARDWARE :

- Linux OS / Raspberry Pi - memiliki akses sudo pada terminal / console
- Mouse / Wireless Mouse / Touchpad bawaan laptop
- Ponsel yang sudah terinstall aplikasi Twitter (Optional)

II. SOFTWARE :

- Python - https://www.python.org/ ( `sudo apt-get install python` )
- Paket Twitter Python - https://pypi.python.org/pypi/twitter ( sudah ada dalam repo:`twitter-1.17.1` )
- Akun Twitter - https://twitter.com
- Ponsel yang sudah terinstall aplikasi Twitter (Optional)


Procedure:
==========

1. Python harus sudah di install. (jika belum terpasang:  `sudo apt-get install python` )

2. Install twitter package dari repo ini:
	 - `cd SecureTea/twitter-1.17.1/`
	 - `sudo python setup.py build install`

3. Kunjungi https://apps.twitter.com & "Create new app" untuk mendapatkan authentication codes dan token.

4. Buka "SecureTea.py" dengan teks editor dan edit variabel berikut ini:

	 - API_KEY = 'XXXX'
	 - API_SECRET = 'XXXX'
	 - ACCESS_TOKEN = 'XXXX'
	 - ACCESS_TOKEN_SECRET = 'XXXX'
	 - twitter_username = 'XXXX'

5. Opsional dalam "SecureTea.py" Anda dapat mengatur `debug = 1` untuk mengaktifkan console log (default:aktif). atau `set debug = 0` tanpa logging di console.

6. Pasang Mouse / Wireless Mouse apabila Touchpad tidak berfungsi dengan baik (Linux/Raspberry machine).

7. Oke, Jalankan program -->  `sudo python SecureTea.py`

8. Perhatikan welcome_msg nya Seperti ini :
`Selamat Datang di SecureTea..!! Initializing System @ Mon Mar 20 17:06:28 2017`

9. Akses laptop dengan menggerakkan mouse/touchpad untuk melihat kumulatif koordinat X & Y pada console. Jika Anda memiliki aplikasi twitter terinstal di ponsel Anda, Anda bisa mendapatkan update di "pesan" dari akun twitter Anda.

10. Cek pesan Alert pada console & inbox di twitter Anda.
`Alert(4) : Seseorang telah mengakses laptop anda waktu Mon Mar 20 17:04:13 2017`


For Suggestions and Contributing :
==================================

- Developer : @idbmb - Bambang Rahmadi K.P
- Email     : bmb.router@gmail.com
- Telegram  : +6285342854277
