#!/usr/bin/python
import os
import gnupg
import sys
#
#SELECT PATH AND UPDATE ALL OTHER .py's scripts
#
def genK():
 os.system('rm -rf /PATH/TO/WHERE/YOU/WANT/GPG/FOLDER')
 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 input_data = gpg.gen_key_input(
     name_email='YOUR@MAIL.COM',
     subkey_type='RSA',
     subley_lenght=2048,
     expire_date=0
     passphrase='YOUR_NEW_GNUPG_PASSWORD_MAKE_THIS_AS_LONG_AS_YOU_CAN'
 key = gpg.gen_key(input_data)
 print key
def main():
 genK()
if __name__ == '__main__':
 main()

