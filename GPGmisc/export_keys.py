#!/usr/bin/python
import gnupg
import sys

def asci():
 key='YOUR_PUB_KEY_FINGERPRINT_EX.234305453040ERJVIOSDMVO4'
 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 ascii_armored_public_keys = gpg.export_keys(key)
 ascii_armored_private_keys = gpg.export_keys(key, True)
 with open('key_file.asc', 'w') as f:
     f.write(ascii_armored_public_keys)
     f.write(ascii_armored_private_keys)
def main():
 asci()
if __name__ == '__main__':
 main()
